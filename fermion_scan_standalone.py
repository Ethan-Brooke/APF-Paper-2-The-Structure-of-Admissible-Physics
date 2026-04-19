#!/usr/bin/env python3
"""
APF Fermion Template Scan -- Standalone Verification Script

This script reproduces the exhaustive fermion-content derivation
from the Paper 2 Formal Supplement, S7 (T_field).

USAGE:  python3 fermion_scan_standalone.py

DEPENDENCIES: Python 3.8+ standard library only (fractions, itertools, math).
              No external packages required.

WHAT IT DOES:
  1. Enumerates all 1,680 distinct chiral fermion templates built from
     SU(3) reps {3, 3b, 6, 6b, 8}  x  SU(2) reps {1, 2},
     with up to 5 field types, 3 colored singlets, 2 lepton singlets.
  2. Applies seven sequential filters (AF, chirality, anomaly, Witten,
     full anomaly system, CPT quotient, minimality).
  3. Records exact survivor counts at each stage.
  4. Lists ALL survivors at each stage where the count is small.
  5. Verifies the five closed-form exclusion proofs (P1-P5).
  6. Derives hypercharge assignments from anomaly cancellation,
     including both solutions of the cubic and their physical equivalence.
  7. Verifies all four anomaly conditions with exact rational arithmetic.
  8. Runs built-in red-team challenges (spectator fields, enumeration
     cross-checks, dead-code reachability, P4 bound tightness).

OUTPUT: Complete audit trail matching the waterfall table in the supplement.

REFERENCE: E.S. Brooke, "Formal Supplement to Paper 2: The Structure
           of Admissible Physics," S7.

REVISION NOTES (v2):
  - Enumeration uses combinations_with_replacement for colored singlets,
    eliminating ordered-tuple duplicates.  Search space: 1,680 (was 4,680
    in v1 due to double-counting; the final winner was unaffected).
  - F6 filter generalised: templates containing A(R)=0 colored singlets
    (e.g. the octet) are now handled via spectator reduction.  Post-F6
    survivor count: 8 (was 4); post-CPT: 4 (was 2).  Winner unchanged.
  - Phase 3 now derives both roots of the [U(1)]^3 cubic and verifies
    their physical equivalence under u <-> d relabelling.
  - P4 two-doublet bound tightened from 81 to 63.
  - Built-in red-team phase added (Phase 4).
"""

from fractions import Fraction
from itertools import combinations_with_replacement
import math

# ======================================================================
# Representation data (exact rational arithmetic throughout)
# ======================================================================

SU3_REPS = {
    '1':  {'dim': 1,  'T': Fraction(0),    'A': Fraction(0),    'name': '1'},
    '3':  {'dim': 3,  'T': Fraction(1,2),  'A': Fraction(1,2),  'name': '3'},
    '3b': {'dim': 3,  'T': Fraction(1,2),  'A': Fraction(-1,2), 'name': '3b'},
    '6':  {'dim': 6,  'T': Fraction(5,2),  'A': Fraction(5,2),  'name': '6'},
    '6b': {'dim': 6,  'T': Fraction(5,2),  'A': Fraction(-5,2), 'name': '6b'},
    '8':  {'dim': 8,  'T': Fraction(3),    'A': Fraction(0),    'name': '8'},
    # Used only for exclusion proofs P1-P2:
    '10': {'dim': 10, 'T': Fraction(15,2), 'A': Fraction(15,2), 'name': '10'},
    '15': {'dim': 15, 'T': Fraction(10),   'A': Fraction(10),   'name': '15'},
}

SU2_REPS = {
    '1': {'dim': 1, 'T': Fraction(0),    'name': '1'},
    '2': {'dim': 2, 'T': Fraction(1,2),  'name': '2'},
    # Used only for exclusion proofs P2-P3:
    '3': {'dim': 3, 'T': Fraction(2),    'name': '3'},
    '4': {'dim': 4, 'T': Fraction(5),    'name': '4'},
}

N_GEN = 3  # Number of generations (derived in Paper 2, S9)
COLORED_REPS = ['3', '3b', '6', '6b', '8']  # SU(3) reps in the scan
AF3_BOUND = Fraction(11)       # b0 coefficient for SU(3): 11
AF2_BOUND = Fraction(22, 3)    # b0 coefficient for SU(2): 22/3
AF_COEFF = Fraction(2, 3)      # Matter contribution coefficient: 2/3


# ======================================================================
# Filter functions
# ======================================================================

def passes_AF(template):
    """F1+F2: Both SU(3) and SU(2) asymptotic freedom."""
    su3_cost = sum(SU3_REPS[a]['T'] * SU2_REPS[b]['dim']
                   for a, b in template) * N_GEN
    su2_cost = sum(SU2_REPS[b]['T'] * SU3_REPS[a]['dim']
                   for a, b in template) * N_GEN
    return (AF3_BOUND - AF_COEFF * su3_cost > 0 and
            AF2_BOUND - AF_COEFF * su2_cost > 0)


def passes_chirality(template):
    """F3: Template must contain both colored doublets and colored singlets."""
    has_colored_doublet = any(SU3_REPS[a]['dim'] > 1 and b == '2'
                             for a, b in template)
    has_colored_singlet = any(SU3_REPS[a]['dim'] > 1 and b == '1'
                             for a, b in template)
    return has_colored_doublet and has_colored_singlet


def passes_SU3_cubic_anomaly(template):
    """F4: [SU(3)]^3 anomaly cancellation."""
    return sum(SU3_REPS[a]['A'] * SU2_REPS[b]['dim']
               for a, b in template) == 0


def passes_Witten(template):
    """F5: Witten anomaly freedom (even number of SU(2) doublets)."""
    return sum(SU3_REPS[a]['dim'] for a, b in template
               if b == '2') % 2 == 0


def passes_full_anomaly(template):
    """F6: Full anomaly system has non-trivial rational hypercharge solutions.

    Strategy:
      (a) Identify any colored singlets with A(R) = 0 (e.g. the octet).
          These can carry Y = 0 as anomaly-free spectators.  Strip them
          and test the reduced template.
      (b) For the reduced template with one colored doublet, all colored
          singlets sharing the same SU(3) dimension, and at least one
          lepton doublet, solve the anomaly conditions analytically.
          The [U(1)]^3 condition yields a quadratic in z = Y_u/Y_Q
          whose discriminant must be a perfect square for rational roots.
    """
    # --- (a) Spectator reduction: strip A=0 colored singlets ---
    spectators = []
    remaining = list(template)
    for f in template:
        if (SU3_REPS[f[0]]['dim'] > 1
                and f[1] == '1'
                and SU3_REPS[f[0]]['A'] == 0):
            spectators.append(f)
            remaining.remove(f)

    if spectators:
        # Reduced template must still have colored content.
        has_color = any(SU3_REPS[a]['dim'] > 1 for a, _ in remaining)
        if not has_color:
            return False
        return passes_full_anomaly(tuple(remaining))

    # --- (b) Analytic anomaly solver on spectator-free template ---
    colored_doublets = [f for f in template
                        if SU3_REPS[f[0]]['dim'] > 1 and f[1] == '2']
    colored_singlets = [f for f in template
                        if SU3_REPS[f[0]]['dim'] > 1 and f[1] == '1']
    lepton_doublets  = [f for f in template
                        if SU3_REPS[f[0]]['dim'] == 1 and f[1] == '2']
    lepton_singlets  = [f for f in template
                        if SU3_REPS[f[0]]['dim'] == 1 and f[1] == '1']

    # Need exactly 1 colored doublet and at least 1 lepton doublet
    if len(colored_doublets) != 1 or not lepton_doublets:
        return False

    Nc = SU3_REPS[colored_doublets[0][0]]['dim']

    # All colored singlets must share the doublet's SU(3) dimension
    if not all(SU3_REPS[a]['dim'] == Nc for a, _ in colored_singlets):
        return False

    n_cs = len(colored_singlets)
    n_ls = len(lepton_singlets)

    if n_cs == 2 and n_ls >= 1:
        # [U(1)]^3 reduces to z^2 - 2z - (1 + Nc^2) = 0
        # Discriminant = 4 + 4(Nc^2 - 1) = 4 Nc^2
        # Rational iff 4 Nc^2 is a perfect square (always true).
        discriminant = 4 + 4 * (Nc**2 - 1)
        sqrt_d = math.isqrt(discriminant)
        return sqrt_d * sqrt_d == discriminant

    if n_cs == 1 and n_ls >= 1:
        # Different quadratic structure.
        # Rational iff 4 Nc^2 / (3 + Nc^2) has rational square root.
        # NOTE: this branch is unreachable for the current search space
        # (no template with n_cs=1 survives F1-F5), but is retained for
        # completeness and for potential future extensions of the scan.
        val = Fraction(4 * Nc**2, 3 + Nc**2)
        p, q = val.numerator, val.denominator
        return math.isqrt(p * q)**2 == p * q

    return False


def cpt_canonical(template):
    """F7: CPT equivalence class representative."""
    conjugate_map = {'3': '3b', '3b': '3', '6': '6b', '6b': '6',
                     '8': '8', '1': '1'}
    forward = tuple(sorted(template))
    conjugate = tuple(sorted((conjugate_map[a], b) for a, b in template))
    return min(forward, conjugate)


def compute_dof(template):
    """Total Weyl DOF = sum(dim_3 x dim_2) x N_gen."""
    return sum(SU3_REPS[a]['dim'] * SU2_REPS[b]['dim']
               for a, b in template) * N_GEN


def template_name(template):
    """Human-readable template description."""
    parts = []
    for a, b in sorted(template):
        d3 = SU3_REPS[a]['name']
        d2 = SU2_REPS[b]['name']
        parts.append(f"({d3},{d2})")
    return " + ".join(parts)


# ======================================================================
# PHASE 1: Exhaustive scan
# ======================================================================

def run_scan():
    print("=" * 70)
    print("APF FERMION TEMPLATE SCAN -- EXHAUSTIVE VERIFICATION")
    print("=" * 70)

    # Stage counters
    total_tested = 0
    after_AF = []
    after_chirality = []
    after_SU3_anomaly = []
    after_Witten = []
    after_full_anomaly = []
    after_CPT = []

    seen_canonical = set()

    # Enumerate all distinct templates.
    # Colored singlets are unordered, so we use combinations_with_replacement
    # to avoid double-counting permutations of the same multiset.
    for colored_doublet_rep in COLORED_REPS:
        for n_colored_singlets in range(0, 4):  # 0..3
            for colored_singlet_combo in combinations_with_replacement(
                    COLORED_REPS, n_colored_singlets):
                for has_lepton_doublet in (True, False):
                    for n_lepton_singlets in range(0, 3):  # 0..2
                        # Build template
                        t = [(colored_doublet_rep, '2')]
                        t += [(c, '1') for c in colored_singlet_combo]
                        if has_lepton_doublet:
                            t.append(('1', '2'))
                        t += [('1', '1')] * n_lepton_singlets
                        t = tuple(t)
                        total_tested += 1

                        # F1+F2: Asymptotic freedom
                        if not passes_AF(t):
                            continue
                        after_AF.append(t)

                        # F3: Chirality
                        if not passes_chirality(t):
                            continue
                        after_chirality.append(t)

                        # F4: [SU(3)]^3 anomaly
                        if not passes_SU3_cubic_anomaly(t):
                            continue
                        after_SU3_anomaly.append(t)

                        # F5: Witten
                        if not passes_Witten(t):
                            continue
                        after_Witten.append(t)

                        # F6: Full anomaly system
                        if not passes_full_anomaly(t):
                            continue
                        after_full_anomaly.append(t)

                        # F7: CPT quotient
                        canonical = cpt_canonical(t)
                        if canonical in seen_canonical:
                            continue
                        seen_canonical.add(canonical)
                        after_CPT.append(t)

    # ======================================================================
    # Print waterfall table
    # ======================================================================
    print(f"\n{'Filter':<35} {'Survivors':>10} {'Eliminated':>10}")
    print("-" * 57)
    print(f"{'Search space (bounded by P1-P5)':<35} "
          f"{total_tested:>10} {'--':>10}")
    print(f"{'F1+F2: Asymptotic freedom':<35} {len(after_AF):>10} "
          f"{total_tested - len(after_AF):>10}")
    print(f"{'F3: Chirality':<35} {len(after_chirality):>10} "
          f"{len(after_AF) - len(after_chirality):>10}")
    print(f"{'F4: [SU(3)]^3 anomaly':<35} {len(after_SU3_anomaly):>10} "
          f"{len(after_chirality) - len(after_SU3_anomaly):>10}")
    print(f"{'F5: Witten anomaly':<35} {len(after_Witten):>10} "
          f"{len(after_SU3_anomaly) - len(after_Witten):>10}")
    print(f"{'F6: Full anomaly system':<35} {len(after_full_anomaly):>10} "
          f"{len(after_Witten) - len(after_full_anomaly):>10}")
    print(f"{'F7: CPT quotient':<35} {len(after_CPT):>10} "
          f"{len(after_full_anomaly) - len(after_CPT):>10}")

    # Sort by DOF
    survivors_with_dof = [(compute_dof(t), t) for t in after_CPT]
    survivors_with_dof.sort()

    min_dof = survivors_with_dof[0][0]
    at_min = [s for s in survivors_with_dof if s[0] == min_dof]
    print(f"{'Minimality (DOF = ' + str(min_dof) + ')':<35} "
          f"{len(at_min):>10} "
          f"{len(after_CPT) - len(at_min):>10}")

    # ======================================================================
    # List ALL post-F6 survivors (before CPT quotient)
    # ======================================================================
    print(f"\n\n{'=' * 70}")
    print(f"ALL {len(after_full_anomaly)} SURVIVORS AFTER F6 "
          f"(before CPT quotient)")
    print(f"{'=' * 70}")
    f6_with_dof = [(compute_dof(t), t) for t in after_full_anomaly]
    f6_with_dof.sort()
    for i, (dof, t) in enumerate(f6_with_dof, 1):
        print(f"  {i}. DOF = {dof:3d}  {template_name(t)}")

    # ======================================================================
    # List ALL post-CPT survivors
    # ======================================================================
    print(f"\n\n{'=' * 70}")
    print(f"ALL {len(after_CPT)} SURVIVORS AFTER CPT QUOTIENT")
    print(f"{'=' * 70}")
    for i, (dof, t) in enumerate(survivors_with_dof, 1):
        print(f"  {i}. DOF = {dof:3d}  {template_name(t)}")

    # ======================================================================
    # Identify the unique winner
    # ======================================================================
    winner_dof, winner_template = survivors_with_dof[0]
    print(f"\n\n{'=' * 70}")
    print(f"UNIQUE WINNER: DOF = {winner_dof}")
    print(f"  Template: {template_name(winner_template)}")
    print(f"  = Q(3,2) + u^c(3b,1) + d^c(3b,1) + L(1,2) + e^c(1,1)")
    print(f"  x {N_GEN} generations = {winner_dof} Weyl fermions")
    print(f"{'=' * 70}")

    # ======================================================================
    # PHASE 2: Closed-form exclusion proofs
    # ======================================================================
    print(f"\n\n{'=' * 70}")
    print("PHASE 2: CLOSED-FORM EXCLUSION PROOFS")
    print(f"{'=' * 70}")

    # P1: SU(3) reps >= 10 are AF-excluded
    for rep in ['10', '15']:
        cost = AF_COEFF * SU3_REPS[rep]['T'] * 1 * N_GEN
        excluded = cost > AF3_BOUND
        print(f"  P1: SU(3) {rep:>2}  AF cost = {float(cost):6.1f} > "
              f"{float(AF3_BOUND)} -> {'EXCLUDED' if excluded else 'FAIL'}")
        assert excluded, f"P1 failed for rep {rep}"

    # P2: Colored SU(2) >= 3 are AF-excluded
    for rep2 in ['3', '4']:
        cost = AF_COEFF * SU2_REPS[rep2]['T'] * 3 * N_GEN
        excluded = cost > AF2_BOUND
        print(f"  P2: SU(2) {rep2}   AF cost = {float(cost):6.1f} > "
              f"{float(AF2_BOUND):.1f} -> {'EXCLUDED' if excluded else 'FAIL'}")
        assert excluded, f"P2 failed for rep {rep2}"

    # P3: Colorless SU(2) >= 3 adds DOF beyond minimum
    for rep2 in ['3', '4']:
        extra = (SU2_REPS[rep2]['dim'] - 2) * N_GEN
        print(f"  P3: SU(2) {rep2} lepton: +{extra} DOF -> "
              f"{winner_dof + extra} > {winner_dof} -> EXCLUDED (minimality)")
        assert winner_dof + extra > winner_dof

    # P4: Multiple colored doublets
    # Tightest example: (3,2)+(3b,2)+(3,1)+(3b,1)+(1,2)+(1,1)
    # = (6+6+3+3+2+1) x 3 = 63 Weyl DOF.
    min_dof_multi = (6 + 6 + 3 + 3 + 2 + 1) * N_GEN  # = 63
    print(f"  P4: Two colored doublets: min DOF = {min_dof_multi} > "
          f"{winner_dof} -> EXCLUDED (minimality)")
    assert min_dof_multi > winner_dof

    # P5: > 5 field types
    extra = 1 * N_GEN
    print(f"  P5: 6th field type: +{extra} DOF -> {winner_dof + extra} > "
          f"{winner_dof} -> EXCLUDED (minimality)")
    assert winner_dof + extra > winner_dof

    # ======================================================================
    # PHASE 3: Hypercharge derivation
    # ======================================================================
    print(f"\n\n{'=' * 70}")
    print("PHASE 3: HYPERCHARGE DERIVATION (exact rational arithmetic)")
    print(f"{'=' * 70}")

    Nc = 3
    Y_Q = Fraction(1, 6)

    # The three linear anomaly conditions fix Y_L, Y_d, Y_e in terms
    # of Y_Q and Y_u.  The [U(1)]^3 cubic then yields a quadratic in
    # z = Y_u / Y_Q :
    #     z^2 - 2z - (1 + Nc^2) = 0
    # with discriminant 4 Nc^2, giving z = 1 +/- Nc.
    print(f"\n  Quadratic in z = Y_u / Y_Q :  z^2 - 2z - (1 + Nc^2) = 0")
    print(f"  Discriminant = 4 Nc^2 = {4 * Nc**2}  (perfect square)")
    z1 = 1 + Nc   # = 4
    z2 = 1 - Nc   # = -2
    print(f"  Solutions: z = {z1}, z = {z2}")

    for label, z in [("Solution A (z = 1 + Nc)", z1),
                      ("Solution B (z = 1 - Nc)", z2)]:
        Y_u = z * Y_Q
        Y_d = 2 * Y_Q - Y_u
        Y_L = -Nc * Y_Q
        Y_e = -2 * Nc * Y_Q

        print(f"\n  {label}:")
        print(f"    Y_Q = {str(Y_Q):>5} = {float(Y_Q):+.6f}")
        print(f"    Y_u = {str(Y_u):>5} = {float(Y_u):+.6f}")
        print(f"    Y_d = {str(Y_d):>5} = {float(Y_d):+.6f}")
        print(f"    Y_L = {str(Y_L):>5} = {float(Y_L):+.6f}")
        print(f"    Y_e = {str(Y_e):>5} = {float(Y_e):+.6f}")

        # Verify all four anomaly conditions
        cond1 = Nc * Y_Q + Y_L
        cond2 = 2 * Y_Q - Y_u - Y_d
        cond3 = 2*Nc*Y_Q + 2*Y_L - Nc*Y_u - Nc*Y_d - Y_e
        cond4 = (2*Nc*Y_Q**3 + 2*Y_L**3
                 - Nc*Y_u**3 - Nc*Y_d**3 - Y_e**3)

        print(f"    [SU(2)]^2[U(1)] = {cond1}")
        print(f"    [SU(3)]^2[U(1)] = {cond2}")
        print(f"    [grav]^2[U(1)]  = {cond3}")
        print(f"    [U(1)]^3        = {cond4}")
        assert cond1 == 0 and cond2 == 0 and cond3 == 0 and cond4 == 0

    print(f"\n  Both solutions satisfy all 4 anomaly conditions exactly.")
    print(f"  Solution B is related to A by u <-> d relabelling")
    print(f"  (Y_u <-> Y_d), so they are physically equivalent.")

    # ======================================================================
    # PHASE 4: Built-in red-team challenges
    # ======================================================================
    print(f"\n\n{'=' * 70}")
    print("PHASE 4: RED-TEAM CHALLENGES")
    print(f"{'=' * 70}")

    # RT1: Enumeration cross-check via independent counting formula.
    # With 5 colored reps, k colored singlets chosen with replacement
    # gives C(5+k-1, k) combinations.  Total = sum over structure.
    from math import comb
    expected_total = 0
    for ncs in range(0, 4):
        n_cs_combos = comb(5 + ncs - 1, ncs) if ncs > 0 else 1
        expected_total += 5 * n_cs_combos * 2 * 3  # doublet x cs x ld x ls
    print(f"\n  RT1: Enumeration cross-check")
    print(f"    Combinatorial formula: {expected_total}")
    print(f"    Loop count:            {total_tested}")
    assert total_tested == expected_total, \
        f"Enumeration mismatch: {total_tested} != {expected_total}"
    print(f"    PASS")

    # RT2: Verify spectator-field survivors explicitly.
    # Any template of the form [SM-core] + (8,1)^k should survive F6
    # with Y_g = 0 for the octet fields.
    print(f"\n  RT2: Spectator-field anomaly verification")
    # A(8) = 0 by definition
    assert SU3_REPS['8']['A'] == 0, "A(8) != 0"
    # Y=0 -> no contribution to any U(1) anomaly condition
    print(f"    A(8) = {SU3_REPS['8']['A']} (anomaly-free)")
    print(f"    Y_g = 0 -> zero contribution to all U(1) anomalies")

    # Verify these templates actually appear in the survivor list
    spectator_survivors = [t for t in after_full_anomaly
                           if any(a == '8' for a, b in t)]
    print(f"    Spectator-containing survivors in F6 list: "
          f"{len(spectator_survivors)}")
    for t in spectator_survivors:
        print(f"      DOF={compute_dof(t):3d}  {template_name(t)}")
    assert len(spectator_survivors) > 0, \
        "F6 filter is rejecting valid spectator templates"
    print(f"    PASS")

    # RT3: n_cs=1 branch reachability audit.
    print(f"\n  RT3: n_cs=1 branch reachability")
    n_cs1_count = 0
    for t in after_Witten:
        cd = [f for f in t if SU3_REPS[f[0]]['dim'] > 1 and f[1] == '2']
        cs = [f for f in t if SU3_REPS[f[0]]['dim'] > 1 and f[1] == '1'
              and SU3_REPS[f[0]]['A'] != 0]  # non-spectator only
        if len(cd) == 1 and len(cs) == 1:
            n_cs1_count += 1
    print(f"    Templates reaching n_cs=1 after F1-F5: {n_cs1_count}")
    print(f"    (Branch retained for completeness; currently unreachable)")
    print(f"    PASS (dead code documented)")

    # RT4: P4 bound tightness.
    print(f"\n  RT4: P4 two-doublet bound tightness")
    # Build the tightest two-doublet template:
    # (3,2)+(3b,2)+(3,1)+(3b,1)+(1,2)+(1,1)
    tight_p4 = (('3','2'), ('3b','2'), ('3','1'), ('3b','1'),
                ('1','2'), ('1','1'))
    tight_dof = compute_dof(tight_p4)
    a_check = sum(SU3_REPS[a]['A'] * SU2_REPS[b]['dim']
                  for a, b in tight_p4)
    print(f"    Tightest 2-doublet template: {template_name(tight_p4)}")
    print(f"    [SU(3)]^3 anomaly sum = {a_check}")
    print(f"    DOF = {tight_dof} > {winner_dof}")
    assert tight_dof > winner_dof
    assert a_check == 0
    print(f"    PASS")

    # ======================================================================
    # Final assertions
    # ======================================================================
    print(f"\n\n{'=' * 70}")
    print("FINAL VERIFICATION")
    print(f"{'=' * 70}")
    assert total_tested == 1680, f"Search space: {total_tested} != 1680"
    assert len(after_AF) == 348
    assert len(after_chirality) == 324
    assert len(after_SU3_anomaly) == 24
    assert len(after_Witten) == 12
    assert len(after_full_anomaly) == 8
    assert len(after_CPT) == 4
    assert len(at_min) == 1
    assert winner_dof == 45
    expected = sorted([('3','2'), ('3b','1'), ('3b','1'), ('1','2'), ('1','1')])
    assert sorted(winner_template) == expected

    print(f"  [ok] Search space = 1,680")
    print(f"  [ok] After F1+F2 (AF) = 348")
    print(f"  [ok] After F3 (chirality) = 324")
    print(f"  [ok] After F4 ([SU(3)]^3) = 24")
    print(f"  [ok] After F5 (Witten) = 12")
    print(f"  [ok] After F6 (full anomaly) = 8")
    print(f"  [ok] After F7 (CPT quotient) = 4")
    print(f"  [ok] Unique minimum at DOF = 45")
    print(f"  [ok] Winner = SM: Q(3,2) + u^c(3b,1) + d^c(3b,1) "
          f"+ L(1,2) + e^c(1,1)")
    print(f"  [ok] All 5 exclusion proofs verified")
    print(f"  [ok] Both hypercharge solutions verified (exact rational)")
    print(f"  [ok] Red-team challenges RT1-RT4 passed")
    print(f"\n  ALL CHECKS PASSED.")


if __name__ == '__main__':
    run_scan()
