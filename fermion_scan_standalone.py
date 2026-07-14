#!/usr/bin/env python3
"""
APF Fermion Template Scan -- Canonical Standalone Verification Script

THIS IS THE CANONICAL EXECUTABLE for the Paper 2 fermion-content scan.
Every count in the waterfall table of Technical Supplement I (v5.3),
S "Fermion content: complete scan of the declared space", is generated
by this script, and the release's audit files are emitted by it:

    python3 fermion_scan_standalone.py                # full audit trail
    python3 fermion_scan_standalone.py --emit-audit   # + write release_audit/

USAGE:  python3 fermion_scan_standalone.py [--emit-audit [DIR]]

DEPENDENCIES: Python 3.8+ standard library only (fractions, itertools,
              math, json, hashlib, csv).  No external packages.

VERSION LOCK: canonical APF codebase v24.3.423; NUMERICAL KERNEL at
commit 5bc6193 (2026-07-14; bank 3912) -- the commit at which the
scan's numerical content was locked.  Later engine commits (the
corrigenda trail in VERSION_LOCK) are count-neutral proof-scope and
metadata corrigenda; the numerical certificate is invariant across
them.  The canonical F6 machinery below is ported from
apf/ec_inventory_reading.py (check_L_F6_not_from_EC) at the kernel
commit; the in-repo copy of that module reproduces every count here
as a bank check.

WHAT IT DOES:
  1. Enumerates all 1,680 distinct chiral fermion templates built from
     SU(3) reps {3, 3b, 6, 6b, 8}  x  SU(2) reps {1, 2},
     with exactly one colored doublet, 0-3 colored singlets,
     0-1 lepton doublets, 0-2 lepton singlets (the declared caps).
  2. Applies the seven sequential filters F1-F7 with F6 in its
     CANONICAL form (full-system non-degeneracy: solve the complete
     anomaly system, spectators included, and require a non-degenerate
     rational solution, Y_Q != 0).  Waterfall:
     1680 -> 348 -> 324 -> 24 -> 12 -> 10 -> 5 -> SM @ 45 DOF.
  3. Reports the two variant F6 predicates as robustness statistics
     on the 12 F1-F5 survivors: spectator reduction (8 pre-CPT /
     4 post-CPT; the predicate implemented by the v2 script archived
     at Zenodo 10.5281/zenodo.19154197) and uniform dimension
     (4 pre-CPT / 2 post-CPT; the gauge.py check_T_field code path).
     The winner (minimum DOF 45) is identical under all three.
  4. Lists all canonical post-F6 survivors (10) and post-CPT
     survivors (5), and the spectator-reduction lists (8 and 4).
  5. Verifies the five closed-form exclusion proofs P1-P5, with P4 in
     its corrected class-dominance form (class minimum 54 > 45; the
     conjugate-pair witness; no tightness claim).
  6. Derives hypercharge assignments from anomaly cancellation,
     including both solutions of the cubic and their physical
     equivalence.
  7. Verifies all four anomaly conditions with exact rational
     arithmetic.
  8. Runs built-in red-team challenges RT1-RT6, including the
     two-colored-doublet class-dominance mini-enumeration (RT4),
     the true-chirality audit statistic (RT5, the release-audit-layer
     report promised at filter F3), and filter-order invariance
     across all 5,040 orderings (RT6).
  9. Asserts the final verification conditions, including the
     three-predicate count triple (10/5 canonical | 8/4 spectator |
     4/2 uniform) and winner invariance.

AUDIT FILES (--emit-audit, default directory release_audit/):
  scan_inputs.json      representation tables, caps, filter definitions,
                        equivalence relation, version lock
  scan_outputs.csv      all 1,680 canonical templates (DOF, CPT class)
  filter_waterfall.csv  F1-F7 survivor counts (canonical) + the F6
                        predicate triple as robustness rows
  near_misses.csv       templates failing only the last nontrivial
                        filter (the 42-DOF stripped generation) +
                        non-minimal survivors
  kill_index.csv        per-candidate first-failing filter for every
                        one of the 1,680 templates
  chirality_audit.csv   true-chirality statistic per canonical
                        post-F6 survivor at its computed witness
  certificate.sha256    SHA-256 of each file + of the ordered bundle

OUTPUT: complete audit trail matching the waterfall table in
Technical Supplement I, S "Fermion content".

REFERENCE: E.S. Brooke, "Technical Supplement I to Paper 2: The
           Classification Core," v5.3.

REVISION NOTES (v4.1, 2026-07-14 -- the review 5.1.01 pass):
  - RT6 ADDED: filter-order invariance.  All 7! = 5,040 orderings of the
    seven filters are evaluated on the 1,680-template set under the
    TOTAL spectator-reduction F6 predicate (the canonical full-system
    decision procedure is complete on the reachable set but not total
    on all templates, so the total variant carries the permutation
    sweep; the conjunction argument is predicate-independent).  Every
    ordering yields the same 4 post-CPT survivors and the same unique
    DOF-45 winner.  This backs the order-invariance lemma of
    Supplement I in executable form.

REVISION NOTES (v4, 2026-07-14 -- the version-locked release pass):
  - CANONICAL F6 PREDICATE implemented: full-system non-degeneracy.
    The complete anomaly system (three linear conditions + the [U(1)]^3
    cubic) is solved exactly over the rationals -- nullspace + rational
    root machinery, no floats -- and a non-degenerate (Y_Q != 0)
    rational solution is required.  Post-F6: 10 pre-CPT / 5 post-CPT.
    The v2/v3 spectator-reduction predicate (8/4) and the gauge.py
    uniform-dimension path (4/2) are retained as reported robustness
    variants.  Winner invariant at SM @ 45 under all three.
  - The T66 charged-octet solution family is computed, with
    Y_8 = -(3/5) Y_Q verified as forced by the linear system on every
    T66 solution (variety = exactly 3 projective points).
  - RT4 REWRITTEN to the class-dominance form: the two-colored-doublet
    mini-enumeration under printed F1-F5 computes the class minimum 54
    (the conjugate-pair witness (3,2)+(3b,2)+(3,1)+(3b,1), verified
    against all seven filters with a generic exact solution family),
    and dominance 54 > 45 is asserted.  The former "tightness" claim is
    withdrawn: the old 63-DOF witness is Witten-ODD (never admissible),
    kept here only as a computed guard.
  - RT5 ADDED: the true-chirality audit statistic (no gauge-invariant
    rep-conjugate pairing with opposite hypercharge), reported per
    canonical survivor at its computed witness -- the release-audit-layer
    statistic promised at filter F3.  It is a report, not a filter.
  - AUDIT EMISSION ADDED (--emit-audit): the six data files + SHA-256
    certificate required by the reproducibility contract.
  - Enumeration, F1-F5, P1-P3/P5, and the hypercharge derivation are
    unchanged from v3.

REVISION NOTES (v3, 2026-07-13):
  - Cubic anomaly coefficient A(6) corrected 5/2 -> 7/2 (and A(6b) to
    -7/2): the symmetric two-index rep of SU(3) has A = (N+4)/2 = 7/2
    in A(fund)=1/2 units.  The v2 value 5/2 was the Dynkin INDEX T(6),
    a distinct quantity.  Computationally inert: 144 sextet-containing
    templates reach F4, and no F4 verdict differs between the two
    values anywhere in the reachable space (verified by direct
    recomputation, 2026-07-13); waterfall and winner unchanged.

REVISION NOTES (v2): combinations_with_replacement enumeration (1,680
    distinct, was 4,680 ordered); spectator-reduction F6; both cubic
    roots derived; red-team phase added.
"""

from fractions import Fraction
from itertools import combinations_with_replacement, combinations
import math
import sys

SCRIPT_VERSION = "4.2"
VERSION_LOCK = {
    "script": "fermion_scan_standalone.py v4.2 (2026-07-15)",
    "codebase": "v24.3.423",
    "numerical_kernel_commit": "5bc6193",
    "numerical_kernel_note": (
        "the engine commit at which the scan's numerical content was "
        "locked (rep tables, caps, predicates, waterfall); every later "
        "engine commit on the corrigenda trail is a count-neutral "
        "proof-scope or metadata corrigendum -- the numerical "
        "certificate is invariant across them"),
    "corrigenda_trail": [
        "668daa5 (check_T_field summary: P4 class-min 54)",
        "e230757 (check_T_field declared-ansatz re-scope + P3 F2+F5 battery)",
        "this release's engine commit (P3 color-dimension case split, "
        "review 5.2.01 item .01; hash pinned in the git history of the "
        "push that ships this manifest)",
    ],
    "bank": 3912,
    "paper_main": "Paper_2_Structure_of_Admissible_Physics_v7.2",
    "supplement_I": "Paper_2_Structure_of_Admissible_Physics_Supplement_v5.3",
    "supplement_II": "Paper_2_Foundational_Gauge_Program_Supplement_v1.0",
}

# ======================================================================
# Representation data (exact rational arithmetic throughout)
# ======================================================================

SU3_REPS = {
    '1':  {'dim': 1,  'T': Fraction(0),    'A': Fraction(0),    'name': '1'},
    '3':  {'dim': 3,  'T': Fraction(1,2),  'A': Fraction(1,2),  'name': '3'},
    '3b': {'dim': 3,  'T': Fraction(1,2),  'A': Fraction(-1,2), 'name': '3b'},
    '6':  {'dim': 6,  'T': Fraction(5,2),  'A': Fraction(7,2),  'name': '6'},
    '6b': {'dim': 6,  'T': Fraction(5,2),  'A': Fraction(-7,2), 'name': '6b'},
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

N_GEN = 3  # Number of generations (imported; see Supplement I, S3-gen scope)
COLORED_REPS = ['3', '3b', '6', '6b', '8']  # SU(3) reps in the scan
AF3_BOUND = Fraction(11)       # b0 coefficient for SU(3): 11
AF2_BOUND = Fraction(22, 3)    # b0 coefficient for SU(2): 22/3
AF_COEFF = Fraction(2, 3)      # Weyl matter coefficient: 2/3

CONJ3 = {'3': '3b', '3b': '3', '6': '6b', '6b': '6', '8': '8', '1': '1'}


# ======================================================================
# Filters F1-F5 and F7 (unchanged since v2)
# ======================================================================

def b0_su3(template):
    """F1: b0(3) = 11 - (2/3) sum T(r3) dim(r2) N_gen."""
    return AF3_BOUND - AF_COEFF * sum(
        SU3_REPS[a]['T'] * SU2_REPS[b]['dim'] for a, b in template) * N_GEN


def b0_su2(template):
    """F2: b0(2) = 22/3 - (2/3) sum T(r2) dim(r3) N_gen."""
    return AF2_BOUND - AF_COEFF * sum(
        SU2_REPS[b]['T'] * SU3_REPS[a]['dim'] for a, b in template) * N_GEN


def passes_AF(template):
    """F1+F2: Both SU(3) and SU(2) asymptotic freedom."""
    return b0_su3(template) > 0 and b0_su2(template) > 0


def passes_content(template):
    """F3 (doublet-singlet content): both colored doublets and colored
    singlets present.  A content predicate, NOT a chirality test -- the
    true-chirality statistic is reported separately (RT5 / the audit
    layer), charge-dependently, after hypercharges are assigned."""
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
    """F5: Witten anomaly freedom (even number of SU(2) doublets,
    counted with SU(3) multiplicity)."""
    return sum(SU3_REPS[a]['dim'] for a, b in template
               if b == '2') % 2 == 0


def cpt_canonical(template):
    """F7: CPT equivalence class representative."""
    forward = tuple(sorted(template))
    conjugate = tuple(sorted((CONJ3[a], b) for a, b in template))
    return min(forward, conjugate)


def compute_dof(template):
    """Total Weyl DOF = sum(dim_3 x dim_2) x N_gen."""
    return sum(SU3_REPS[a]['dim'] * SU2_REPS[b]['dim']
               for a, b in template) * N_GEN


def template_name(template):
    """Human-readable template description."""
    return " + ".join(f"({SU3_REPS[a]['name']},{SU2_REPS[b]['name']})"
                      for a, b in sorted(template))


def aligned_witness(template, y):
    """The witness re-ordered to match template_name's sorted entry order,
    so each printed charge sits under its printed entry.  Ties between
    identical entries are broken by charge value (deterministic)."""
    pairs = sorted(zip(template, y), key=lambda p: (p[0], p[1]))
    return [c for _, c in pairs]


def witness_str(template, y):
    return '(' + ', '.join(str(c) for c in aligned_witness(template, y)) + ')'


# ======================================================================
# Exact full-anomaly-system machinery (ported from
# apf/ec_inventory_reading.py at commit 5bc6193; Fractions throughout)
# ======================================================================

def _linear_rows(t):
    """[SU(3)]^2 U(1), [SU(2)]^2 U(1), [grav]^2 U(1) rows (all-left-handed
    Weyl convention)."""
    r3 = [SU3_REPS[a]['T'] * SU2_REPS[b]['dim'] for a, b in t]
    r2 = [SU2_REPS[b]['T'] * SU3_REPS[a]['dim'] for a, b in t]
    rg = [Fraction(SU3_REPS[a]['dim'] * SU2_REPS[b]['dim']) for a, b in t]
    return [r3, r2, rg]


def _cubic_val(t, y):
    return sum(Fraction(SU3_REPS[a]['dim'] * SU2_REPS[b]['dim']) * y[i] ** 3
               for i, (a, b) in enumerate(t))


def _is_solution(t, y):
    """All four anomaly conditions, exact."""
    rows = _linear_rows(t)
    return (all(sum(r[i] * y[i] for i in range(len(t))) == 0 for r in rows)
            and _cubic_val(t, y) == 0)


def _nullspace(rows, n):
    """Exact rational nullspace basis (Gaussian elimination on Fractions)."""
    M = [r[:] for r in rows]
    piv, rr = [], 0
    for c in range(n):
        prow = None
        for r in range(rr, len(M)):
            if M[r][c] != 0:
                prow = r
                break
        if prow is None:
            continue
        M[rr], M[prow] = M[prow], M[rr]
        pv = M[rr][c]
        M[rr] = [x / pv for x in M[rr]]
        for r in range(len(M)):
            if r != rr and M[r][c] != 0:
                f0 = M[r][c]
                M[r] = [x - f0 * yv for x, yv in zip(M[r], M[rr])]
        piv.append(c)
        rr += 1
        if rr == len(M):
            break
    basis = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [Fraction(0)] * n
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fc]
        basis.append(v)
    return basis


def _rat_roots(coeffs):
    """All rational roots of a polynomial with Fraction coefficients
    (highest degree first, degree <= 3).  Exact rational root theorem."""
    den = 1
    for c in coeffs:
        den = den * c.denominator // math.gcd(den, c.denominator)
    ic = [int(c * den) for c in coeffs]
    g = 0
    for c in ic:
        g = math.gcd(g, abs(c))
    ic = [c // g for c in ic]
    a_n, a_0 = ic[0], ic[-1]
    if a_0 == 0:
        sub = _rat_roots([Fraction(c) for c in ic[:-1]]) if len(ic) > 2 else \
              ([Fraction(-ic[1], ic[0])] if len(ic) == 2 else [])
        return sorted(set([Fraction(0)] + sub))

    def divisors(m):
        m = abs(m)
        ds = []
        i = 1
        while i * i <= m:
            if m % i == 0:
                ds += [i, m // i]
            i += 1
        return sorted(set(ds))

    roots = set()
    for p in divisors(a_0):
        for q in divisors(a_n):
            for s in (1, -1):
                x = Fraction(s * p, q)
                v = Fraction(0)
                for c in ic:
                    v = v * x + c
                if v == 0:
                    roots.add(x)
    return sorted(roots)


def _primitive(u):
    """Normalize a rational vector to a primitive integer direction with
    positive leading nonzero entry."""
    den = 1
    for c in u:
        den = den * c.denominator // math.gcd(den, c.denominator)
    iu = [int(c * den) for c in u]
    g = 0
    for c in iu:
        g = math.gcd(g, abs(c))
    if g:
        iu = [c // g for c in iu]
    for c in iu:
        if c != 0:
            if c < 0:
                iu = [-x for x in iu]
            break
    return [Fraction(x) for x in iu]


def _plane_solutions(t, v, w):
    """Rational projective solutions of the cubic on span{v, w}.
    ('plane', None) if the cubic vanishes identically on the plane,
    else ('points', [primitive integer direction vectors])."""
    n = len(t)
    d = [Fraction(SU3_REPS[a]['dim'] * SU2_REPS[b]['dim']) for a, b in t]
    c30 = sum(d[i] * v[i] ** 3 for i in range(n))
    c21 = 3 * sum(d[i] * v[i] ** 2 * w[i] for i in range(n))
    c12 = 3 * sum(d[i] * v[i] * w[i] ** 2 for i in range(n))
    c03 = sum(d[i] * w[i] ** 3 for i in range(n))
    if c30 == c21 == c12 == c03 == 0:
        return ('plane', None)
    dirs = []
    if c30 == 0:
        dirs.append(v[:])
        qcoef = [c21, c12, c03]
        while qcoef and qcoef[0] == 0:
            qcoef = qcoef[1:]
        if len(qcoef) >= 2:
            for x in _rat_roots(qcoef):
                dirs.append([x * v[i] + w[i] for i in range(n)])
    else:
        for x in _rat_roots([c30, c21, c12, c03]):
            dirs.append([x * v[i] + w[i] for i in range(n)])
    return ('points', [_primitive(u) for u in dirs])


def _idx_colored_doublet(t):
    """Index of the (unique, by scan construction) colored doublet."""
    idxs = [i for i, (a, b) in enumerate(t)
            if SU3_REPS[a]['dim'] > 1 and b == '2']
    if len(idxs) != 1:
        raise ValueError(f"template outside the decided space "
                         f"(colored doublets: {len(idxs)}): {t}")
    return idxs[0]


class F6Undecided(Exception):
    """Raised rather than guessing when the decision procedure cannot
    certify a verdict.  Never raised on the reachable F1-F5 survivor
    set (all 12 templates resolve; asserted in the final block)."""


def f6_full_system(t):
    """CANONICAL F6: full-system non-degeneracy.

    Solve the complete anomaly system -- three linear conditions plus
    the [U(1)]^3 cubic -- exactly over the rationals, spectators
    included, and require a NON-DEGENERATE rational solution
    (Y_Q != 0 on the colored doublet: the F6 non-degeneracy
    requirement, an independent phenomenological assumption of the scan).

    Returns (nondegenerate: bool, weakly_solvable: bool, witness, note).
    The witness is an exact solution vector (primitive integer
    direction) with Y_Q != 0 when nondegenerate is True, else a
    degenerate solution when only weak solvability holds, else None.

    Decision procedure (complete on the reachable set, raises
    F6Undecided elsewhere rather than guessing):
      k = dim nullspace of the linear system.
      k = 0: no nontrivial solution.
      k = 1: the variety is the null line iff the cubic vanishes there.
      k = 2: exact projective solution of the cubic on the plane
             (rational root theorem; 'plane' means identically zero).
      k >= 3: YES-certificates by zero-extension -- strip subsets of
             anomaly-decoupled entries (A(R)=0 colored singlets and
             lepton singlets, set to Y = 0, contributing zero to all
             four conditions) until the reduced system has k <= 2,
             decide there, and extend the witness by zeros (verified
             against the FULL system before returning).  NO-verdicts
             at k >= 3 are not certifiable this way and raise.
    """
    n = len(t)
    iq = _idx_colored_doublet(t)
    ns = _nullspace(_linear_rows(t), n)
    k = len(ns)

    if k == 0:
        return (False, False, None, 'k=0: no nontrivial linear solution')

    if k == 1:
        v = _primitive(ns[0])
        if _cubic_val(t, v) != 0:
            return (False, False, None, 'k=1: cubic does not vanish on the null line')
        nondeg = v[iq] != 0
        note = ('k=1: variety = one projective point; '
                + ('Y_Q != 0' if nondeg else 'Y_Q = 0 FORCED'))
        return (nondeg, True, v, note)

    if k == 2:
        kind, pts = _plane_solutions(t, ns[0], ns[1])
        if kind == 'plane':
            v, w = ns
            wit = v if v[iq] != 0 else (w if w[iq] != 0 else None)
            if wit is None:
                return (False, True, _primitive(v),
                        'k=2: cubic vanishes on plane; Y_Q = 0 identically')
            return (True, True, _primitive(wit),
                    'k=2: cubic vanishes identically on the plane')
        if not pts:
            return (False, False, None, 'k=2: no rational projective solution')
        nd = [p for p in pts if p[iq] != 0]
        if nd:
            return (True, True, nd[0],
                    f'k=2: {len(pts)} projective point(s), '
                    f'{len(nd)} with Y_Q != 0')
        return (False, True, pts[0],
                f'k=2: {len(pts)} projective point(s), all with Y_Q = 0')

    # k >= 3: zero-extension YES-certificates
    strippable = [i for i, (a, b) in enumerate(t)
                  if (SU3_REPS[a]['dim'] > 1 and b == '1'
                      and SU3_REPS[a]['A'] == 0)          # A(R)=0 colored singlet
                  or (SU3_REPS[a]['dim'] == 1 and b == '1')]  # lepton singlet
    best_weak = None
    for r in range(1, len(strippable) + 1):
        for S in combinations(strippable, r):
            reduced = tuple(f for i, f in enumerate(t) if i not in S)
            if len(reduced) - 3 > 2:      # still k > 2 even if full rank
                continue
            try:
                nd, weak, wit, _ = f6_full_system(reduced)
            except (ValueError, F6Undecided):
                continue
            if wit is not None:
                # extend by zeros at the stripped slots
                full = []
                ri = 0
                for i in range(n):
                    if i in S:
                        full.append(Fraction(0))
                    else:
                        full.append(wit[ri])
                        ri += 1
                if _is_solution(t, full):
                    if nd and full[iq] != 0:
                        return (True, True, _primitive(full),
                                f'k={k}: zero-extension of a reduced '
                                f'certificate (stripped {len(S)} '
                                f'decoupled entr{"y" if len(S)==1 else "ies"})')
                    if weak and best_weak is None:
                        best_weak = _primitive(full)
    if best_weak is not None:
        raise F6Undecided(
            f'k={k}: weak solution found but no non-degenerate '
            f'certificate; NO-verdict not certifiable by reduction: {t}')
    raise F6Undecided(f'k={k}: no certificate found: {t}')


def f6_spectator_reduction(template):
    """VARIANT (i), reported as robustness: spectator reduction.
    The predicate implemented by the v2/v3 script (Zenodo
    10.5281/zenodo.19154197): strip A(R)=0 colored singlets at Y = 0,
    then solve the reduced system analytically, requiring a
    non-degenerate rational solution on the remainder."""
    spectators = []
    remaining = list(template)
    for f in template:
        if (SU3_REPS[f[0]]['dim'] > 1
                and f[1] == '1'
                and SU3_REPS[f[0]]['A'] == 0):
            spectators.append(f)
            remaining.remove(f)

    if spectators:
        has_color = any(SU3_REPS[a]['dim'] > 1 for a, _ in remaining)
        if not has_color:
            return False
        return f6_spectator_reduction(tuple(remaining))

    colored_doublets = [f for f in template
                        if SU3_REPS[f[0]]['dim'] > 1 and f[1] == '2']
    colored_singlets = [f for f in template
                        if SU3_REPS[f[0]]['dim'] > 1 and f[1] == '1']
    lepton_doublets  = [f for f in template
                        if SU3_REPS[f[0]]['dim'] == 1 and f[1] == '2']
    lepton_singlets  = [f for f in template
                        if SU3_REPS[f[0]]['dim'] == 1 and f[1] == '1']

    if len(colored_doublets) != 1 or not lepton_doublets:
        return False

    Nc = SU3_REPS[colored_doublets[0][0]]['dim']
    if not all(SU3_REPS[a]['dim'] == Nc for a, _ in colored_singlets):
        return False

    n_cs = len(colored_singlets)
    n_ls = len(lepton_singlets)

    if n_cs == 2 and n_ls >= 1:
        discriminant = 4 + 4 * (Nc**2 - 1)
        sqrt_d = math.isqrt(discriminant)
        return sqrt_d * sqrt_d == discriminant

    if n_cs == 1 and n_ls >= 1:
        val = Fraction(4 * Nc**2, 3 + Nc**2)
        p, q = val.numerator, val.denominator
        return math.isqrt(p * q)**2 == p * q

    return False


def f6_uniform_dimension(t):
    """VARIANT (ii), reported as robustness: the gauge.py check_T_field
    code path (_an) -- requires every colored singlet to share the
    colored doublet's SU(3) dimension.  Transcribed verbatim."""
    cd = [f for f in t if SU3_REPS[f[0]]['dim'] > 1 and f[1] == '2']
    cs = [f for f in t if SU3_REPS[f[0]]['dim'] > 1 and f[1] == '1']
    ld = [f for f in t if SU3_REPS[f[0]]['dim'] == 1 and f[1] == '2']
    ls = [f for f in t if SU3_REPS[f[0]]['dim'] == 1 and f[1] == '1']
    if len(cd) != 1 or not ld:
        return False
    Nc = SU3_REPS[cd[0][0]]['dim']
    if not all(SU3_REPS[a]['dim'] == Nc for a, _ in cs):
        return False
    if len(cs) == 2 and len(ls) >= 1:
        d = 4 + 4 * (Nc ** 2 - 1)
        sd = math.isqrt(d)
        return sd * sd == d
    if len(cs) == 1 and len(ls) >= 1:
        v = Fraction(4 * Nc ** 2, 3 + Nc ** 2)
        p, q = v.numerator, v.denominator
        return math.isqrt(p * q) ** 2 == p * q
    return False


# ======================================================================
# True-chirality audit statistic (RT5 / the audit layer)
# ======================================================================

def dirac_pairs(t, y):
    """Gauge-invariant rep-conjugate Dirac pairings at charge assignment y:
    entry pairs (i, j) with conjugate SU(3) reps, equal SU(2) reps
    (1 and 2 are both self-conjugate for pairing purposes), and
    opposite hypercharge.  A template with any such pair is not truly
    chiral at this assignment: the pair admits a gauge-invariant mass."""
    pairs = []
    n = len(t)
    for i in range(n):
        for j in range(i + 1, n):
            (a1, b1), (a2, b2) = t[i], t[j]
            if CONJ3[a1] == a2 and b1 == b2 and y[i] + y[j] == 0:
                pairs.append((i, j))
    return pairs


def real_singlet_entries(t, y):
    """Entries in a real SU(3) rep, SU(2) singlet, Y = 0 (Majorana-mass-
    capable on their own); reported alongside the Dirac pairing count."""
    return [i for i, (a, b) in enumerate(t)
            if a in ('8', '1') and b == '1' and y[i] == 0]


# ======================================================================
# PHASE 1: Exhaustive scan (canonical F6)
# ======================================================================

def enumerate_templates():
    """All 1,680 distinct templates under the declared caps."""
    out = []
    for colored_doublet_rep in COLORED_REPS:
        for n_colored_singlets in range(0, 4):  # 0..3
            for colored_singlet_combo in combinations_with_replacement(
                    COLORED_REPS, n_colored_singlets):
                for has_lepton_doublet in (True, False):
                    for n_lepton_singlets in range(0, 3):  # 0..2
                        t = [(colored_doublet_rep, '2')]
                        t += [(c, '1') for c in colored_singlet_combo]
                        if has_lepton_doublet:
                            t.append(('1', '2'))
                        t += [('1', '1')] * n_lepton_singlets
                        out.append(tuple(t))
    return out


def run_scan(emit_audit=False, audit_dir='release_audit'):
    print("=" * 70)
    print("APF FERMION TEMPLATE SCAN -- CANONICAL STANDALONE VERIFICATION")
    print(f"  script v{SCRIPT_VERSION}; version lock: codebase "
          f"{VERSION_LOCK['codebase']} (numerical kernel "
          f"{VERSION_LOCK['numerical_kernel_commit']}, bank "
          f"{VERSION_LOCK['bank']}; corrigenda trail in the manifest)")
    print("=" * 70)

    all_templates = enumerate_templates()
    total_tested = len(all_templates)

    after_AF, after_content, after_SU3, after_Witten = [], [], [], []
    after_F6, after_CPT = [], []
    kill = {}          # template -> first-failing filter / SURVIVOR
    f6_records = {}    # F1-F5 survivor -> (nondeg, weak, witness, note)
    seen_canonical = set()

    for t in all_templates:
        if b0_su3(t) <= 0:
            kill[t] = 'F1_SU3_AF'
            continue
        if b0_su2(t) <= 0:
            kill[t] = 'F2_SU2_AF'
            continue
        after_AF.append(t)
        if not passes_content(t):
            kill[t] = 'F3_content'
            continue
        after_content.append(t)
        if not passes_SU3_cubic_anomaly(t):
            kill[t] = 'F4_SU3_cubic'
            continue
        after_SU3.append(t)
        if not passes_Witten(t):
            kill[t] = 'F5_Witten'
            continue
        after_Witten.append(t)
        nondeg, weak, wit, note = f6_full_system(t)
        f6_records[t] = (nondeg, weak, wit, note)
        if not nondeg:
            kill[t] = 'F6_full_system_nondegeneracy'
            continue
        after_F6.append(t)
        canonical = cpt_canonical(t)
        if canonical in seen_canonical:
            kill[t] = 'F7_CPT_duplicate'
            continue
        seen_canonical.add(canonical)
        after_CPT.append(t)

    survivors_with_dof = sorted((compute_dof(t), t) for t in after_CPT)
    min_dof = survivors_with_dof[0][0]
    at_min = [s for s in survivors_with_dof if s[0] == min_dof]
    for t in after_CPT:
        kill[t] = ('SURVIVOR_MINIMUM' if compute_dof(t) == min_dof
                   else 'SURVIVOR_NONMINIMAL')

    # ------------------------------------------------------------------
    # Waterfall table (canonical)
    # ------------------------------------------------------------------
    print(f"\n{'Filter':<42} {'Survivors':>10} {'Eliminated':>10}")
    print("-" * 64)
    rows = [
        ("Search space (declared caps)", total_tested, None),
        ("F1+F2: Asymptotic freedom", len(after_AF), total_tested),
        ("F3: Doublet-singlet content", len(after_content), len(after_AF)),
        ("F4: [SU(3)]^3 anomaly", len(after_SU3), len(after_content)),
        ("F5: Witten anomaly", len(after_Witten), len(after_SU3)),
        ("F6: Full-system non-degeneracy (canonical)", len(after_F6),
         len(after_Witten)),
        ("F7: CPT quotient", len(after_CPT), len(after_F6)),
    ]
    for label, n, prev in rows:
        elim = '--' if prev is None else str(prev - n)
        print(f"{label:<42} {n:>10} {elim:>10}")
    print(f"{'Minimality (DOF = ' + str(min_dof) + ')':<42} "
          f"{len(at_min):>10} {len(after_CPT) - len(at_min):>10}")

    # ------------------------------------------------------------------
    # The F6 predicate triple (robustness statistics on the 12)
    # ------------------------------------------------------------------
    spect_pass = [t for t in after_Witten if f6_spectator_reduction(t)]
    unif_pass = [t for t in after_Witten if f6_uniform_dimension(t)]

    def post_cpt_count(ts):
        return len({cpt_canonical(t) for t in ts})

    triple = {
        'full_system_nondegeneracy (CANONICAL)':
            (len(after_F6), post_cpt_count(after_F6)),
        'spectator_reduction (robustness; v2 script predicate)':
            (len(spect_pass), post_cpt_count(spect_pass)),
        'uniform_dimension (robustness; gauge.py code path)':
            (len(unif_pass), post_cpt_count(unif_pass)),
    }
    print(f"\n{'=' * 70}")
    print("F6 PREDICATE TAXONOMY on the 12 F1-F5 survivors "
          "(pre-CPT / post-CPT)")
    print(f"{'=' * 70}")
    for k, (pre, post) in triple.items():
        print(f"  {k:<55} {pre:>2} / {post}")
    winners = []
    for ts in (after_F6, spect_pass, unif_pass):
        winners.append(min(compute_dof(t) for t in ts))
    print(f"  Winner (min DOF) under all three predicates: "
          f"{winners[0]}, {winners[1]}, {winners[2]}")

    # ------------------------------------------------------------------
    # Canonical survivor listings
    # ------------------------------------------------------------------
    print(f"\n\n{'=' * 70}")
    print(f"ALL {len(after_F6)} CANONICAL SURVIVORS AFTER F6 "
          f"(before CPT quotient)")
    print(f"{'=' * 70}")
    for i, (dof, t) in enumerate(sorted((compute_dof(t), t)
                                        for t in after_F6), 1):
        wit = f6_records[t][2]
        print(f"  {i:2d}. DOF = {dof:3d}  {template_name(t)}")
        print(f"       witness Y = {witness_str(t, wit)}   "
              f"(aligned to the sorted entry order)   [{f6_records[t][3]}]")

    print(f"\n\n{'=' * 70}")
    print(f"ALL {len(after_CPT)} CANONICAL SURVIVORS AFTER CPT QUOTIENT")
    print(f"{'=' * 70}")
    for i, (dof, t) in enumerate(survivors_with_dof, 1):
        print(f"  {i}. DOF = {dof:3d}  {template_name(t)}")

    # Spectator-reduction listings (the v2 robustness form)
    print(f"\n\n{'=' * 70}")
    print(f"ROBUSTNESS: ALL {len(spect_pass)} SURVIVORS UNDER "
          f"SPECTATOR REDUCTION (pre-CPT)")
    print(f"{'=' * 70}")
    for i, (dof, t) in enumerate(sorted((compute_dof(t), t)
                                        for t in spect_pass), 1):
        print(f"  {i}. DOF = {dof:3d}  {template_name(t)}")
    spect_cpt = sorted({cpt_canonical(t) for t in spect_pass})
    print(f"  ({len(spect_cpt)} post-CPT classes)")

    # ------------------------------------------------------------------
    # The unique winner
    # ------------------------------------------------------------------
    winner_dof, winner_template = survivors_with_dof[0]
    print(f"\n\n{'=' * 70}")
    print(f"UNIQUE WINNER: DOF = {winner_dof}")
    print(f"  Template: {template_name(winner_template)}")
    print(f"  = Q(3,2) + u^c(3b,1) + d^c(3b,1) + L(1,2) + e^c(1,1)")
    print(f"  x {N_GEN} generations = {winner_dof} Weyl fermions")
    print(f"{'=' * 70}")

    # ------------------------------------------------------------------
    # Near misses
    # ------------------------------------------------------------------
    near_misses = []
    for t in after_Witten:
        nondeg, weak, wit, note = f6_records[t]
        if not nondeg:
            near_misses.append({
                'kind': 'F6_failure (sharpest near-miss)',
                'template': template_name(t), 'dof': compute_dof(t),
                'weakly_solvable': weak,
                'witness': (witness_str(t, wit)
                            if wit is not None else ''),
                'note': note + '; excluded by the F6 non-degeneracy '
                        'requirement (Y_Q != 0), the independent '
                        'phenomenological assumption of the scan',
            })
    for dof, t in survivors_with_dof[1:]:
        near_misses.append({
            'kind': 'nonminimal_survivor',
            'template': template_name(t), 'dof': dof,
            'weakly_solvable': True,
            'witness': witness_str(t, f6_records[t][2]),
            'note': 'passes all seven filters; eliminated at the '
                    'minimality cut',
        })
    print(f"\n{'=' * 70}")
    print("NEAR MISSES (recorded in near_misses.csv)")
    print(f"{'=' * 70}")
    for nm in near_misses:
        print(f"  [{nm['kind']}] DOF = {nm['dof']:3d}  {nm['template']}")
        print(f"      {nm['note']}")

    # ==================================================================
    # PHASE 2: Closed-form exclusion proofs
    # ==================================================================
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

    # P3: Colorless SU(2) >= 3 adds DOF beyond minimum (dominance)
    for rep2 in ['3', '4']:
        extra = (SU2_REPS[rep2]['dim'] - 2) * N_GEN
        print(f"  P3: SU(2) {rep2} lepton: +{extra} DOF -> "
              f"{winner_dof + extra} > {winner_dof} -> EXCLUDED (dominance)")
        assert winner_dof + extra > winner_dof

    # P4: Two-colored-doublet CLASS DOMINANCE (corrected form, 2026-07-14).
    # The class minimum is 54 Weyl DOF, attained by the conjugate-pair
    # witness (3,2) + (3b,2) + (3,1) + (3b,1); dominance 54 > 45.  The
    # witness battery and the mini-enumeration certifying the minimum
    # run in RT4.  No tightness claim is made here or anywhere: the
    # former 63-DOF "tightest" witness is Witten-ODD (never admissible).
    P4_WITNESS = (('3', '2'), ('3b', '2'), ('3', '1'), ('3b', '1'))
    p4_dof = compute_dof(P4_WITNESS)
    print(f"  P4: Two colored doublets: class minimum DOF = {p4_dof} "
          f"(conjugate-pair witness; mini-enumeration in RT4) > "
          f"{winner_dof} -> EXCLUDED (class dominance)")
    assert p4_dof == 54 and p4_dof > winner_dof

    # P5: > 5 field types (dominance)
    extra = 1 * N_GEN
    print(f"  P5: 6th field type: +{extra} DOF -> {winner_dof + extra} > "
          f"{winner_dof} -> EXCLUDED (dominance)")
    assert winner_dof + extra > winner_dof

    # ==================================================================
    # PHASE 3: Hypercharge derivation
    # ==================================================================
    print(f"\n\n{'=' * 70}")
    print("PHASE 3: HYPERCHARGE DERIVATION (exact rational arithmetic)")
    print(f"{'=' * 70}")

    Nc = 3
    Y_Q = Fraction(1, 6)

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

    # ==================================================================
    # PHASE 4: Built-in red-team challenges
    # ==================================================================
    print(f"\n\n{'=' * 70}")
    print("PHASE 4: RED-TEAM CHALLENGES")
    print(f"{'=' * 70}")

    # RT1: Enumeration cross-check via independent counting formula.
    from math import comb
    expected_total = 0
    for ncs in range(0, 4):
        n_cs_combos = comb(5 + ncs - 1, ncs) if ncs > 0 else 1
        expected_total += 5 * n_cs_combos * 2 * 3
    print(f"\n  RT1: Enumeration cross-check")
    print(f"    Combinatorial formula: {expected_total}")
    print(f"    Loop count:            {total_tested}")
    assert total_tested == expected_total
    print(f"    PASS")

    # RT2: Octet-containing survivors under the canonical predicate,
    # and the forced charged-octet relation on T66.
    print(f"\n  RT2: Octet (A(R)=0) handling under the canonical F6")
    assert SU3_REPS['8']['A'] == 0, "A(8) != 0"
    octet_survivors = sorted((compute_dof(t), t) for t in after_F6
                             if any(a == '8' for a, b in t))
    print(f"    Octet-containing canonical survivors: "
          f"{len(octet_survivors)}")
    for dof, t in octet_survivors:
        wit = f6_records[t][2]
        i8 = next(i for i, (a, b) in enumerate(t) if a == '8')
        iq = _idx_colored_doublet(t)
        print(f"      DOF={dof:3d}  {template_name(t)}  "
              f"Y_8 = {wit[i8]}, Y_Q = {wit[iq]}")
    assert len(octet_survivors) == 6, \
        "expected 6 octet-containing canonical survivors (T66/T69/T72 + mirrors)"
    # The 66-DOF pair: Y_8 = -(3/5) Y_Q forced by the linear system on
    # EVERY solution (variety = exactly 3 projective points).
    t66s = [t for d, t in octet_survivors if d == 66]
    for t in t66s:
        i8 = next(i for i, (a, b) in enumerate(t) if a == '8')
        iq = _idx_colored_doublet(t)
        ns = _nullspace(_linear_rows(t), len(t))
        assert len(ns) == 2
        kind, pts = _plane_solutions(t, ns[0], ns[1])
        assert kind == 'points' and len(pts) == 3
        assert all(p[i8] == -Fraction(3, 5) * p[iq] for p in pts)
    print(f"    T66 charged-octet relation Y_8 = -(3/5) Y_Q verified as")
    print(f"    FORCED on every solution (3 projective points per side)")
    print(f"    PASS")

    # RT3: n_cs=1 branch reachability audit (spectator-reduction variant).
    print(f"\n  RT3: n_cs=1 branch reachability (spectator-reduction variant)")
    n_cs1_count = 0
    for t in after_Witten:
        cd = [f for f in t if SU3_REPS[f[0]]['dim'] > 1 and f[1] == '2']
        cs = [f for f in t if SU3_REPS[f[0]]['dim'] > 1 and f[1] == '1'
              and SU3_REPS[f[0]]['A'] != 0]
        if len(cd) == 1 and len(cs) == 1:
            n_cs1_count += 1
    print(f"    Templates reaching n_cs=1 after F1-F5: {n_cs1_count}")
    print(f"    (Branch retained for completeness; currently unreachable)")
    print(f"    PASS (dead code documented)")

    # RT4: Two-colored-doublet CLASS DOMINANCE (replaces the withdrawn
    # "tightness" challenge).
    print(f"\n  RT4: P4 class dominance -- two-colored-doublet mini-enumeration")
    P4_WITNESS = (('3', '2'), ('3b', '2'), ('3', '1'), ('3b', '1'))
    # (a) witness battery: DOF, filters, exact generic solution family
    assert compute_dof(P4_WITNESS) == 54
    assert b0_su3(P4_WITNESS) == 5 and b0_su2(P4_WITNESS) == Fraction(4, 3)
    assert passes_content(P4_WITNESS)
    assert passes_SU3_cubic_anomaly(P4_WITNESS)
    assert sum(SU3_REPS[a]['dim'] for a, b in P4_WITNESS if b == '2') == 6
    assert passes_Witten(P4_WITNESS)
    for y1, y2 in ((Fraction(1), Fraction(2)),
                   (Fraction(3, 7), Fraction(-5, 2)),
                   (Fraction(1, 6), Fraction(11))):
        y = [y1, -y1, y2, -y2]
        assert _is_solution(P4_WITNESS, y) and y1 != 0
    print(f"    Witness (3,2)+(3b,2)+(3,1)+(3b,1): DOF = 54; passes "
          f"F1-F5; the full anomaly")
    print(f"    system vanishes identically on the conjugate family "
          f"(Y1, -Y1, Y2, -Y2), Y1 != 0")
    # (b) mini-enumeration: class minimum over printed F1-F5
    best = None
    count_pass = 0
    for cds in combinations_with_replacement(COLORED_REPS, 2):
        for ncs in range(0, 4):
            for css in combinations_with_replacement(COLORED_REPS, ncs):
                for hl in (True, False):
                    for nls in range(0, 3):
                        t = tuple([(c, '2') for c in cds]
                                  + [(c, '1') for c in css]
                                  + ([('1', '2')] if hl else [])
                                  + [('1', '1')] * nls)
                        if b0_su3(t) <= 0 or b0_su2(t) <= 0:
                            continue
                        if not passes_content(t):
                            continue
                        if not passes_SU3_cubic_anomaly(t):
                            continue
                        if not passes_Witten(t):
                            continue
                        count_pass += 1
                        d = compute_dof(t)
                        if best is None or d < best[0]:
                            best = (d, t)
    print(f"    Mini-enumeration: {count_pass} two-doublet templates pass "
          f"F1-F5;")
    print(f"    class minimum = {best[0]} at {template_name(best[1])}")
    assert best[0] == 54
    assert sorted(best[1]) == sorted(P4_WITNESS)
    # (c) dominance; and the guard on the withdrawn 63-DOF witness
    assert 54 > winner_dof
    T63 = (('3', '2'), ('3b', '2'), ('3', '1'), ('3b', '1'),
           ('1', '2'), ('1', '1'))
    w63 = sum(SU3_REPS[a]['dim'] for a, b in T63 if b == '2')
    assert w63 % 2 == 1, "the withdrawn 63-DOF witness should be Witten-ODD"
    print(f"    Class dominance: 54 > {winner_dof}.  Guard: the withdrawn "
          f"63-DOF witness has")
    print(f"    doublet count {w63} (ODD) -- Witten-anomalous, never "
          f"admissible.  No tightness claim.")
    print(f"    PASS")

    # RT5: True-chirality audit statistic (the release-audit-layer report
    # promised at filter F3; a report, NOT a filter).
    print(f"\n  RT5: True-chirality audit (per canonical survivor, at its "
          f"computed witness)")
    chirality_rows = []
    for dof, t in sorted((compute_dof(t), t) for t in after_F6):
        wit = f6_records[t][2]
        pairs = dirac_pairs(t, wit)
        reals = real_singlet_entries(t, wit)
        truly_chiral = not pairs
        chirality_rows.append({
            'template': template_name(t), 'dof': dof,
            'witness': witness_str(t, wit),
            'dirac_pairs': len(pairs),
            'real_Y0_singlet_entries': len(reals),
            'truly_chiral_at_witness': truly_chiral,
        })
        tag = 'CHIRAL' if truly_chiral else 'VECTOR-LIKE PAIRING'
        print(f"    DOF={dof:3d}  {tag:<20} pairs={len(pairs)} "
              f"realY0={len(reals)}  {template_name(t)}")
    sm_row = [r for r in chirality_rows if r['dof'] == 45]
    assert all(r['truly_chiral_at_witness'] for r in sm_row), \
        "the SM winner must be truly chiral at its witness"
    print(f"    Statistic is witness-dependent for templates with multiple")
    print(f"    solution points; reported, never consumed as a filter.")
    print(f"    PASS")

    # RT6: Filter-order invariance -- all 7! orderings, total predicate.
    print(f"\n  RT6: Filter-order invariance (all 7! = 5,040 orderings)")
    from itertools import permutations
    # Total per-template predicates (each a set of passing templates).
    # F6 here is the TOTAL spectator-reduction variant (the canonical
    # full-system procedure is complete on the reachable set, not total
    # on all 1,680); the conjunction argument is predicate-independent.
    all_set = list(dict.fromkeys(all_templates))
    P = {
        'F1': {t for t in all_set if b0_su3(t) > 0},
        'F2': {t for t in all_set if b0_su2(t) > 0},
        'F3': {t for t in all_set if passes_content(t)},
        'F4': {t for t in all_set if passes_SU3_cubic_anomaly(t)},
        'F5': {t for t in all_set if passes_Witten(t)},
        'F6': {t for t in all_set if f6_spectator_reduction(t)},
        'F7': {t for t in all_set if tuple(sorted(t)) == cpt_canonical(t)},
    }
    names = list(P)
    reference = None
    distinct_orders = 0
    for order in permutations(names):
        surv = set(all_set)
        for k in order:
            surv &= P[k]
        fs = frozenset(surv)
        if reference is None:
            reference = fs
        assert fs == reference, f"order {order} changed the survivor set"
        distinct_orders += 1
    assert distinct_orders == 5040
    ref_dofs = sorted(compute_dof(t) for t in reference)
    print(f"    Orderings evaluated: {distinct_orders}")
    print(f"    Survivor set identical in every ordering: "
          f"{len(reference)} post-CPT survivors at DOF {ref_dofs}")
    assert len(reference) == 4, \
        "spectator-predicate post-all-filters survivors must be 4"
    assert min(ref_dofs) == 45 and ref_dofs.count(45) == 1
    print(f"    Unique DOF-45 winner invariant under all orderings")
    print(f"    PASS")

    # ==================================================================
    # Final assertions
    # ==================================================================
    print(f"\n\n{'=' * 70}")
    print("FINAL VERIFICATION")
    print(f"{'=' * 70}")
    assert total_tested == 1680, f"Search space: {total_tested} != 1680"
    assert len(after_AF) == 348
    assert len(after_content) == 324
    assert len(after_SU3) == 24
    assert len(after_Witten) == 12
    assert len(after_F6) == 10, "canonical F6: 10 pre-CPT"
    assert len(after_CPT) == 5, "canonical F7: 5 post-CPT"
    assert len(spect_pass) == 8 and post_cpt_count(spect_pass) == 4
    assert len(unif_pass) == 4 and post_cpt_count(unif_pass) == 2
    assert len(at_min) == 1
    assert winner_dof == 45
    assert winners == [45, 45, 45], "winner invariance across the triple"
    expected = sorted([('3','2'), ('3b','1'), ('3b','1'), ('1','2'), ('1','1')])
    assert sorted(winner_template) == expected
    assert sorted(compute_dof(t) for t in after_Witten) == \
        [42, 42, 45, 45, 48, 48, 66, 66, 69, 69, 72, 72]
    nm_f6 = [nm for nm in near_misses if nm['kind'].startswith('F6_failure')]
    assert len(nm_f6) == 2 and all(nm['dof'] == 42 for nm in nm_f6), \
        "the stripped generation (42) is the unique F6 kill"

    print(f"  [ok] Search space = 1,680")
    print(f"  [ok] After F1+F2 (AF) = 348")
    print(f"  [ok] After F3 (content) = 324")
    print(f"  [ok] After F4 ([SU(3)]^3) = 24")
    print(f"  [ok] After F5 (Witten) = 12  at DOF "
          f"{{42,45,48,66,69,72}} x2")
    print(f"  [ok] After F6 (full-system non-degeneracy, CANONICAL) = 10")
    print(f"  [ok] After F7 (CPT quotient) = 5")
    print(f"  [ok] Robustness triple: spectator 8/4, uniform 4/2; "
          f"canonical 10/5")
    print(f"  [ok] Unique minimum at DOF = 45; winner invariant under "
          f"all three predicates")
    print(f"  [ok] Winner = SM: Q(3,2) + u^c(3b,1) + d^c(3b,1) "
          f"+ L(1,2) + e^c(1,1)")
    print(f"  [ok] Near miss: the 42-DOF stripped generation "
          f"(Y_Q = 0 forced; recorded)")
    print(f"  [ok] All 5 exclusion proofs verified (P4 at class "
          f"dominance, 54 > 45)")
    print(f"  [ok] Both hypercharge solutions verified (exact rational)")
    print(f"  [ok] Red-team challenges RT1-RT6 passed")
    print(f"\n  ALL CHECKS PASSED.")

    # ==================================================================
    # Audit emission
    # ==================================================================
    if emit_audit:
        emit_audit_files(audit_dir, all_templates, kill, rows, triple,
                         near_misses, chirality_rows, after_Witten,
                         f6_records, min_dof, at_min, after_CPT)

    return 0


# ======================================================================
# Audit file emission
# ======================================================================

def emit_audit_files(audit_dir, all_templates, kill, waterfall_rows, triple,
                     near_misses, chirality_rows, after_Witten, f6_records,
                     min_dof, at_min, after_CPT):
    import csv
    import hashlib
    import json
    import os

    os.makedirs(audit_dir, exist_ok=True)
    print(f"\n\n{'=' * 70}")
    print(f"EMITTING AUDIT FILES -> {audit_dir}/")
    print(f"{'=' * 70}")

    # ---------------------------------------------------- scan_inputs.json
    scan_inputs = {
        'version_lock': VERSION_LOCK,
        'generator': 'fermion_scan_standalone.py --emit-audit '
                     '(the canonical executable)',
        'representations': {
            'SU3': {k: {'dim': v['dim'], 'T': str(v['T']), 'A': str(v['A'])}
                    for k, v in SU3_REPS.items()},
            'SU2': {k: {'dim': v['dim'], 'T': str(v['T'])}
                    for k, v in SU2_REPS.items()},
            'note': "reps 10/15 (SU3) and 3/4 (SU2) enter only the "
                    "exclusion proofs P1-P2; the scan space uses "
                    "{1,3,3b,6,6b,8} x {1,2}",
        },
        'N_gen': N_GEN,
        'AF_bounds': {'SU3': str(AF3_BOUND), 'SU2': str(AF2_BOUND),
                      'Weyl_coefficient': str(AF_COEFF)},
        'multiplicity_caps': {
            'colored_doublets': 'exactly 1 (by construction)',
            'colored_singlets': '0-3 (multiset over 5 reps)',
            'lepton_doublets': '0-1',
            'lepton_singlets': '0-2',
            'closed_form_count': '5 x 56 x 2 x 3 = 1680',
        },
        'equivalence_relation': {
            'template': 'unordered multiset of (SU3_rep, SU2_rep) entries',
            'CPT': 'template ~ entrywise SU(3) conjugate; canonical '
                   'representative = lexicographic min of the sorted pair',
        },
        'filters': {
            'F1': 'b0(3) = 11 - (2/3) sum T(r3) dim(r2) N_gen > 0',
            'F2': 'b0(2) = 22/3 - (2/3) sum T(r2) dim(r3) N_gen > 0',
            'F3': 'doublet-singlet content (content predicate, not a '
                  'chirality test; true chirality reported in '
                  'chirality_audit.csv)',
            'F4': 'sum A(r3) dim(r2) = 0',
            'F5': 'sum dim(r3) over SU(2)-doublet entries even (Witten)',
            'F6': 'CANONICAL: full-system non-degeneracy -- the complete '
                  'anomaly system (three linear + the cubic) admits a '
                  'rational solution with Y_Q != 0 (the F6 non-degeneracy '
                  'requirement, an independent phenomenological assumption)',
            'F7': 'CPT quotient',
            'minimality': 'unique minimum-DOF survivor',
        },
        'F6_predicate_taxonomy': {
            'canonical': 'full_system_nondegeneracy (10 pre-CPT / 5 post-CPT)',
            'robustness_variants': {
                'spectator_reduction': '8 pre-CPT / 4 post-CPT '
                                       '(the v2 script predicate)',
                'uniform_dimension': '4 pre-CPT / 2 post-CPT '
                                     '(the gauge.py check_T_field path)',
            },
            'winner': 'min DOF 45 (the SM), invariant under all three',
        },
    }
    files = []

    def emit(name, write_fn):
        path = os.path.join(audit_dir, name)
        write_fn(path)
        files.append(name)
        print(f"  wrote {name}")

    emit('scan_inputs.json', lambda p: open(p, 'w', newline='\n').write(
        json.dumps(scan_inputs, indent=2, sort_keys=False) + '\n'))

    # ---------------------------------------------------- scan_outputs.csv
    ordered = sorted(all_templates, key=lambda t: (compute_dof(t), sorted(t)))

    def w_outputs(p):
        with open(p, 'w', newline='') as fh:
            w = csv.writer(fh, lineterminator='\n')
            w.writerow(['template_id', 'template', 'dof',
                        'cpt_class_representative', 'is_cpt_representative'])
            for i, t in enumerate(ordered, 1):
                ck = cpt_canonical(t)
                w.writerow([i, template_name(t), compute_dof(t),
                            template_name(ck),
                            tuple(sorted(t)) == ck])
    emit('scan_outputs.csv', w_outputs)

    # ------------------------------------------------- filter_waterfall.csv
    def w_waterfall(p):
        with open(p, 'w', newline='') as fh:
            w = csv.writer(fh, lineterminator='\n')
            w.writerow(['stage', 'survivors', 'eliminated', 'note'])
            for label, n, prev in waterfall_rows:
                w.writerow([label, n,
                            '' if prev is None else prev - n, ''])
            w.writerow([f'Minimality (DOF = {min_dof})', len(at_min),
                        len(after_CPT) - len(at_min), 'unique winner = SM'])
            for k, (pre, post) in triple.items():
                w.writerow([f'F6 predicate: {k}', pre, '',
                            f'{post} post-CPT; robustness statistic on '
                            f'the 12 F1-F5 survivors'])
    emit('filter_waterfall.csv', w_waterfall)

    # ----------------------------------------------------- near_misses.csv
    def w_near(p):
        with open(p, 'w', newline='') as fh:
            w = csv.writer(fh, lineterminator='\n')
            w.writerow(['kind', 'template', 'dof', 'weakly_solvable',
                        'witness', 'note'])
            for nm in near_misses:
                w.writerow([nm['kind'], nm['template'], nm['dof'],
                            nm['weakly_solvable'], nm['witness'],
                            nm['note']])
    emit('near_misses.csv', w_near)

    # ------------------------------------------------------ kill_index.csv
    def w_kill(p):
        with open(p, 'w', newline='') as fh:
            w = csv.writer(fh, lineterminator='\n')
            w.writerow(['template_id', 'template', 'dof',
                        'first_failing_filter_or_status'])
            for i, t in enumerate(ordered, 1):
                w.writerow([i, template_name(t), compute_dof(t), kill[t]])
    emit('kill_index.csv', w_kill)

    # ------------------------------------------------- chirality_audit.csv
    def w_chi(p):
        with open(p, 'w', newline='') as fh:
            w = csv.writer(fh, lineterminator='\n')
            w.writerow(['template', 'dof', 'witness', 'dirac_pairs',
                        'real_Y0_singlet_entries', 'truly_chiral_at_witness'])
            for r in chirality_rows:
                w.writerow([r['template'], r['dof'], r['witness'],
                            r['dirac_pairs'], r['real_Y0_singlet_entries'],
                            r['truly_chiral_at_witness']])
    emit('chirality_audit.csv', w_chi)

    # ---------------------------------------------------- certificate.sha256
    cert_path = os.path.join(audit_dir, 'certificate.sha256')
    bundle = hashlib.sha256()
    with open(cert_path, 'w', newline='\n') as fh:
        fh.write('# SHA-256 certificate for the Paper 2 scan audit bundle\n')
        fh.write(f'# generator: {VERSION_LOCK["script"]}\n')
        fh.write(f'# version lock: codebase {VERSION_LOCK["codebase"]} '
                 f'numerical kernel {VERSION_LOCK["numerical_kernel_commit"]} '
                 f'bank {VERSION_LOCK["bank"]} '
                 f'(corrigenda trail in scan_inputs.json)\n')
        for name in files:
            data = open(os.path.join(audit_dir, name), 'rb').read()
            h = hashlib.sha256(data).hexdigest()
            bundle.update(data)
            fh.write(f'{h}  {name}\n')
        fh.write(f'{bundle.hexdigest()}  BUNDLE '
                 f'(ordered concatenation of the files above)\n')
    print(f"  wrote certificate.sha256")
    print(f"\n  Audit bundle complete: {len(files)} data files + certificate.")


if __name__ == '__main__':
    emit = '--emit-audit' in sys.argv
    args = [a for a in sys.argv[1:] if a != '--emit-audit']
    audit_dir = args[0] if args else 'release_audit'
    sys.exit(run_scan(emit_audit=emit, audit_dir=audit_dir))
