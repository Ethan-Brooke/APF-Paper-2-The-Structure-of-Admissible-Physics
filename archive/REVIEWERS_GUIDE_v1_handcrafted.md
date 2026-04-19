# Reviewers' Guide

### A physics-first walkthrough of the codebase for *The Structure of Admissible Physics*

This document is written for the peer reviewers of Paper 2.  Its purpose is to map the logical architecture of the executable codebase to the claims in the manuscript, to make the structural assumptions maximally transparent, and to pre-empt the objections a skeptical reader should raise.

Every assertion in this guide can be verified without reading Python.  The Colab notebook provides an executable path; the code provides a machine-verified one.  This guide provides the third: a prose walkthrough of the mathematical logic.

Paper 1 established the quantum skeleton (Hilbert space, Born rule, gauge symmetry skeleton, entropy) from A1 alone.  Paper 2 uses those results to derive specific structure.  The codebase here imports from `apf/core.py` (Paper 1 results) and extends them in `apf/gauge.py` (Paper 2 results).

---

## Quick navigation

| | |
|---|---|
| **[Derivation DAG ↗](https://ethan-brooke.github.io/APF-Paper-2-The-Structure-of-Admissible-Physics/)** | Interactive 33-node theorem graph — click any node to trace the chain back to A1, count derivation paths, inspect dependencies |
| **[Visual Storyboard ↗](https://ethan-brooke.github.io/APF-Paper-2-The-Structure-of-Admissible-Physics/storyboard.html)** | 12-panel illustrated walkthrough — hydrogen atom → non-closure → gauge group → Ω_Λ = 42/61 |
| **[Paper (Zenodo) ↗](https://doi.org/10.5281/zenodo.18867119)** | Archival PDF with full proofs |
| **[Colab Notebook ↗](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics/blob/main/APF_Reviewer_Walkthrough_Paper2.ipynb)** | Zero-install executable walkthrough |

---

## 1. The derivation in fourteen steps

**Step 1 — Two kinds of non-closure** (§3, `check_L_nc_budget`, `check_L_nc_interf`)

Non-closure means: two individually admissible enforcement demands can be jointly inadmissible.  But non-closure comes in two varieties that must be distinguished.

*Budget non-closure* (L_nc^budget): classical pigeonhole.  Two demands each below the budget can sum to exceed it.  The surplus Δ₁₂ = Δ₂₁ — it is symmetric in the order of operations.  This is classical resource contention.  It does not produce non-commutativity.

*Interference non-closure* (L_nc^interf): the quantum case.  The surplus is order-asymmetric: Δ₁₂ ≠ Δ₂₁.  Committing to enforcement of d₁ before d₂ costs a different total than the reverse order, because the first commitment rearranges the channel landscape in a way that depends on which commitment came first.  This asymmetry is the operational content of non-commutativity.

The paper proves both types exist.  The distinction matters: a classical resource-constrained system can have budget non-closure without order asymmetry.  Only interference non-closure drives the non-abelian gauge structure.

**Step 2 — Irreducibility from A1** (§4, `check_L_irred`)

*Depends on:* A1, T2 (Paper 1).

A1 requires that the enforcement algebra distinguishes all physically distinct admissible states: no two distinct states receive the same enforcement record.  This is precisely the irreducibility condition on the algebra's action on the Hilbert space H (from T2, Paper 1): if a proper closed invariant subspace V ⊊ H existed, then any state in V and any state outside V that agreed on all operators within V would receive identical enforcement records — violating A1.  Therefore no such subspace exists.

The proof is by contradiction, using only A1 and the Hilbert space established in Paper 1.  No additional structure is assumed.

**Step 3 — Non-commutativity from Schur's lemma** (§4, `check_L_delta_nc`)

*Depends on:* L_irred, T2.

Schur's lemma: any operator commuting with every element of an irreducible algebra on a complex Hilbert space must be a scalar multiple of the identity.  A1 requires enforcement operators to be non-trivial (they distinguish states, so they are not proportional to the identity).  Therefore no non-trivial enforcement operator commutes with the entire algebra.  Non-commuting pairs AB ≠ BA exist.

The order-asymmetric surplus Δ₁₂ ≠ Δ₂₁ then follows: AB|ψ⟩ and BA|ψ⟩ are distinct states encoding different enforcement records, and the surplus terms measure the additional cost encoded in those distinct records.

*Why this differs from Paper 1's T1:* T1 established order-dependence from the superadditivity of the capacity functional (scalar argument, no Hilbert space).  L_Δ→nc establishes the same result from a different angle: irreducibility of the algebra on H.  The two arguments are consistent and mutually reinforcing.  A classical contention system produces Δ > 0 with Δ₁₂ = Δ₂₁ (no Hilbert space structure); the present argument has no classical analogue.

**Step 4 — Cost function uniqueness** (§5, `check_L_Cauchy_uniqueness`)

*Depends on:* A1, L_nc.

The enforcement cost function F must be: (i) additive over independent channels, (ii) monotone increasing, (iii) normalised so that the minimum distinct cost is F(1) = 1.  Cauchy's functional equation (1821) then forces F(d) = d as the unique solution.  This eliminates a potential free parameter in the Weinberg angle derivation (completed in Paper 4A).

The proof restricts to ℕ first (where the argument is watertight), then extends to ℚ by density.  The generalisation to ℝ requires continuity, which is provided by monotonicity.

**Step 5 — Three carrier requirements** (§6, `check_Theorem_R`)

*Depends on:* L_nc^interf, T_M (Paper 1).

Non-closure generates three independent enforcement problems.  Each requires a distinct carrier type.  The three problems are genuinely independent: solving one does not solve the others.

*R1 (Confinement carrier):* Stable composites must be distinguishable from their anti-composites: B ≠ B̄.  This requires a trilinear invariant ε_ijk v^i w^j x^k — one that cannot be decomposed into pairwise contractions.  Bilinear carriers produce only B = B̄ (proved in Paper 7, Lemma B1′; Paper 2 states the consequence).  The minimal carrier with a trilinear invariant is complex, 3-dimensional, and faithful (R1).

*R2 (Chiral carrier):* The gauge sector must contain intrinsically irreversible processes in isolation — not merely inherit entropy from the environment or from decoherence.  A vector-like gauge theory is CPT-symmetric at the gauge level, with no intrinsic time-reversal breaking: every process has an exact inverse, sphalerons are absent, all CP phases are rotatable away, bare masses are gauge-invariant.  Such a theory provides zero intrinsically irreversible channels under T_M (enforcement independence).  The only escape is chirality: left and right treated asymmetrically.  The minimal orientation-asymmetric carrier is pseudoreal and 2-dimensional (R2).

*R3 (Abelian grading):* SU(3) × SU(2) representations do not separate all physically distinct states: for example, up-type and down-type antiquarks both transform as (3̄, 1) under colour and weak isospin.  Enforcement completeness (A1: all distinct states must receive distinguishable enforcement records) requires a third carrier to break ties.  The minimal option is one U(1) with distinct charge assignments.  Note: SU(3) × SU(2) is already anomaly-free without U(1) — all cubic and global anomalies cancel.  R3 is therefore not forced by anomaly cancellation but by enforcement completeness and minimality.

**Step 6 — Gauge template uniqueness** (§6, `check_L_gauge_template_uniqueness`)

*Depends on:* Theorem R.

All 17 compact simple Lie algebras are classified against R1.  The result is a two-stage argument:

*Stage 1 (family):* R1 requires a complex faithful fundamental representation with a totally antisymmetric invariant of rank k ≥ 3.  Of the 17 algebras, only the A_n = SU(n+1) family (n ≥ 2) passes.  All others are excluded: B_n and D_n are real (no complex carrier), C_n and E_7 are pseudoreal (composites self-conjugate), G₂/F₄/E₈ are real, E₆ passes the complex test but has minimal faithful dimension 27 — violating A1 capacity minimality.

*Stage 2 (minimality):* The antisymmetric invariant of SU(N_c) has rank k = N_c.  The minimum k = 3 forces N_c = 3.

R2 uniquely selects SU(2): the only compact simple Lie algebra with a 2-dimensional irreducible representation.  R3 selects U(1).  The product structure SU(3) × SU(2) × U(1) is unique.

**Step 7 — Fermion content** (§7, `check_T_field`)

*Depends on:* Gauge template, asymptotic freedom, anomaly cancellation.

A chiral fermion template is formally defined as a finite multiset T = {(r_i, n_i)} where each r_i is an irreducible representation of SU(3) × SU(2) and n_i ≥ 1 is its multiplicity, subject to: (i) left-handed Weyl fields, (ii) SU(3) factor in {3, 3̄, 6, 6̄, 8} (AF bound), (iii) SU(2) factor in {1, 2} (AF bound), (iv) |T| ≤ 5 field types (minimality).

Five closed-form exclusion proofs bound the search space to exactly 4,680 templates.  Seven sequential filters are then applied: SU(3) asymptotic freedom, SU(2) asymptotic freedom, chirality, [SU(3)]³ anomaly cancellation, Witten anomaly freedom, [U(1)]³ anomaly cancellation, CPT quotient.  Minimality selects among survivors.

4,679 templates fail.  One survives: the Standard Model at 45 Weyl degrees of freedom.

**Step 8 — Hypercharge uniqueness** (§7, `check_L_hypercharge`)

*Depends on:* T_field, anomaly cancellation.

The surviving template has 5 multiplet types: Q(3,2), L(1,2), u^c(3̄,1), d^c(3̄,1), e^c(1,1).  Five hypercharge unknowns (Y_Q, Y_L, Y_u, Y_d, Y_e), four independent anomaly conditions, one overall normalisation convention.  The system is uniquely solved.

**Step 9 — Structural channel count C_total = 61** (§8, `check_L_count`, `check_L_species`)

*Depends on:* T_field, gauge template.

L_species: each irreducible representation contributes exactly one structural enforcement channel.  Kinematic properties (helicity, polarization) are not additional channels — they are free given the structural commitment.  Once the interface has committed to enforcing that a left-handed electron is present (one capacity unit ε*), its helicity is determined by the Lorentz representation (Paper 5); no additional enforcement is required.

Under L_species: 45 fermion type-identities + 12 gauge generators (8 gluons + 3 weak + 1 hypercharge) + 4 Higgs real components = 61.  Each costs exactly ε* at Bekenstein saturation.

**Step 10 — Vacuum sector assignment: 42** (§8, `check_L_vac`)

*Depends on:* L_count, T_M.

Three-case exhaustion assigns channels to the vacuum sector (Q1 = 0: not gauge-addressable by external probe):

*Case 1:* 12 gauge generators → vacuum.  They are the enforcement infrastructure itself, not consumers of it.  No external probe addresses a gauge generator directly.

*Case 2:* 27 of 30 fermion internal-structure channels → vacuum.  The 30 fermion internal channels decompose as 3 colour charges (baryonic) + 27 encoding internal SU(N_c) × SU(2) representation structure.  By T_M (Monogamy), each channel has one role.  The role of the 27 is to index the representation-theoretic decomposition of multiplets whose type-identity is already counted in the 15 dark-sector labels.  Assigning an independent Q1=1 label to any of the 27 would require either a second role for the same channel (T_M violation) or a new gauge pathway (T_gauge completeness violation).

*Case 3:* 3 of 4 Higgs components → vacuum.  The 3 Goldstone modes absorbed by W±, Z become longitudinal polarizations after SSB.  They mediate enforcement of the electroweak vacuum structure itself; external probes do not address them independently.  The remaining 1 physical Higgs → dark sector.

Total vacuum: 12 + 27 + 3 = 42.

**Step 11 — Dark sector: rank-1 Gram matrix** (§9, `check_L_singlet_Gram`)

*Depends on:* L_vac, T_M.

The 16 dark-sector channels (15 matter type-identities + 1 physical Higgs) satisfy Q1=1 (gauge-addressable) and Q2=0 (no conserved SU(3) color charge).  Q2=0 zeroes the SU(3) components of every dark-sector demand vector.  The remaining SU(2)×U(1) structure makes all 16 demand vectors project onto the same one-dimensional subspace of gauge-channel space (the direction orthogonal to all SU(3) generators).  The Gram matrix G_ij = v_i · v_j is a rank-1 outer product.  Self-interaction requires at least two linearly independent channels to mediate exchange; rank-1 gives none: σ/m = 0 at leading order.  Single-fluid behavior follows.

Note: the 16 dark types are *not* gauge singlets — they are matter multiplets (Q, L, u^c, d^c, e^c) with non-trivial SU(2)×U(1) quantum numbers.  What collapses to rank-1 is their demand vectors in gauge-channel space, not their gauge charges.

**Step 12 — Horizon equipartition** (§10, `check_L_equip`)

*Depends on:* L_count, L_irr (Paper 1).

At the causal horizon, L_irr (Paper 1, §4.5) forces entropy to its maximum and no further information arrives.  The framework assigns no preferred ordering among the 61 capacity types: they are distinguished only by their discrete Q1/Q2 labels, not by any dynamical weighting.  A system with N equally-unlabelled discrete types has a unique maximum-entropy macrostate: all types equally likely.  Applied to 61 types: each carries an equal share of total enforcement capacity.  The energy density fraction of any sector equals its type-count fraction.

**Step 13 — Saturation independence** (§10, `check_L_sat_partition`)

*Depends on:* L_equip, L_count.

The MECE partition 42+3+16=61 holds independently of the saturation level.  The predicates Q1 and Q2 are structural (they follow from the definitions of gauge-addressability and SU(3) color charge) and do not depend on how close the system is to Bekenstein saturation.  The cosmological fractions are therefore not a near-horizon approximation — they are structural ratios.

**Step 14 — Cosmological fractions** (§10)

Ω_Λ = 42/61 = 0.6885.  Ω_m = 19/61 = 0.3115 (matter = baryonic 3 + dark 16 = 19).  Baryonic fraction f_b = 3/19 ≈ 16%.  No empirical inputs; no free parameters.

---

## 2. The precise non-abelian criterion

A referee may ask: why is Δ > 0 (mere superadditivity) not sufficient to force non-abelian structure?

The answer is that classical resource-contention systems can have Δ > 0 with Δ₁₂ = Δ₂₁ — symmetric surplus.  Network congestion, shared-memory contention, and bandwidth allocation all exhibit budget non-closure with a symmetric cost.  Such systems satisfy L_nc^budget but not L_nc^interf.

The non-abelian criterion is **order-asymmetric superadditivity**: Δ₁₂ ≠ Δ₂₁.  This asymmetry is what L_Δ→nc proves via Schur's lemma on the irreducible Hilbert space of T2.  It is also what makes AB ≠ BA in the enforcement algebra — the records encoded in AB|ψ⟩ and BA|ψ⟩ are distinct because the surplus terms are distinct.  Classical contention produces symmetric surplus (no Hilbert space structure); the Schur argument has no classical analogue.

---

## 3. Structural assumptions and their status

| Assumption | Where used | Status |
|---|---|---|
| A1 (finite enforcement capacity) | All results | Axiom — everything else flows from it |
| T2 (Hilbert space from Paper 1) | L_irred, L_Δ→nc | Proved in Paper 1 codebase |
| T_M (Monogamy from Paper 1) | L_vac, L_singlet_Gram | Proved in Paper 1 codebase |
| L_irr (Irreversibility from Paper 1) | L_equip | Proved in Paper 1 codebase |
| Lemma B1′ (bilinear carriers → B=B̄) | R1 proof boundary | Proved in Paper 7; Paper 2 cites consequence only |
| L_species (rep = channel) | L_count | Derived in this paper; the kinematic/structural distinction is a framework definition grounded in what A1 constrains |

---

## 4. What is not proved in Paper 2

- Quantitative mass predictions — Paper 4B
- Mixing angles (CKM, PMNS) — Paper 4B  
- CP violation — Paper 4B
- Weinberg angle derivation (uses γ₂/γ₁ from T27d) — Paper 4A
- Beta-function coefficients from capacity (L_beta_capacity) — Paper 4A
- Spacetime dimension d=4 — Paper 5
- Lorentzian signature — Paper 5
- Individual vacuum geometric channels (Lorentz frame, spatial metric) — Paper 5
- Inflation and gravitational dynamics — Paper 6
- The absolute EW scale and VEV — Paper 6

The hydrogen atom example in §8 names the 7 channels active at the electron locus and the 24 at the proton locus, but defers the naming of vacuum geometric channels to Paper 5.

---

## 5. How to falsify: six attack surfaces

| # | Attack surface | What to try in the code |
|---|---|---|
| 1 | L_nc^interf vs L_nc^budget | In `check_L_nc_interf()`: verify that setting Δ₁₂ = Δ₂₁ (forcing symmetry) eliminates non-commutativity from the argument while L_nc^budget still holds |
| 2 | L_irred from A1 | In `check_L_irred()`: construct a system with a proper invariant subspace; verify it violates A1's distinguishability requirement |
| 3 | Schur's lemma requirement | In `check_L_delta_nc()`: verify that a commutative algebra on H satisfies Schur only if all operators are scalar — inconsistent with A1 non-triviality |
| 4 | R3 (abelian grading) | In `check_Theorem_R()` R3 step: verify that SU(3)×SU(2) is anomaly-free without U(1). Then verify that without U(1), up-type and down-type antiquarks receive identical enforcement records — A1 violation |
| 5 | L_species (kinematic vs structural) | In `check_L_species()`: add helicities as additional channels (count 73 not 61) and verify this gives wrong Ω_Λ prediction — a direct falsification |
| 6 | L_vac Case 2 (27 fermion internal → vacuum) | In `check_L_vac()`: attempt to assign Q1=1 to any of the 27 internal channels; verify it requires either a T_M violation or a new gauge pathway beyond SU(3)×SU(2)×U(1) |

---

## 6. Reading the code

**`apf/core.py`** — Foundational lemmas carried over from Paper 1, plus Paper 2 additions: `check_L_nc_budget`, `check_L_nc_interf`, `check_L_irred`, `check_L_delta_nc`, `check_L_equip`.

**`apf/gauge.py`** — Paper 2's main physics module: gauge template classification (`check_Theorem_R`, `check_L_gauge_template_uniqueness`), fermion content (`check_T_field`), hypercharges (`check_L_hypercharge`), capacity counting (`check_L_species`, `check_L_count`, `check_L_vac`, `check_L_singlet_Gram`), cosmological partition (`check_L_sat_partition`).

**`apf/L_Cauchy_uniqueness.py`** — Standalone cost function uniqueness proof (`check_L_Cauchy_uniqueness`).

**`apf/bank.py`** — Theorem registry connecting names to check functions.  Provides `run_all()`, `get_check()`, `list_theorems()`.

Every check function begins with a six-field docstring: manuscript section, logical dependencies, mathematical statement, verification method, physical meaning, and code reference.

---

## 7. The scalar-to-matrix boundary

Paper 2 inherits the stratification from Paper 1.  The non-closure argument (Steps 1–3 above) operates at the level of the capacity functional and Hilbert space representation — the Schur's lemma argument uses the operator algebra structure established by T2 (Paper 1), not any matrix representation introduced for computational convenience.

The gauge classification (Step 6) uses Lie algebra theory and representation theory, which Paper 2 applies as established mathematics without re-deriving.  The fermion scan (Step 7) uses the asymptotic freedom and anomaly cancellation conditions of the derived gauge group.

There is no circular use of non-commutativity: non-commutativity is proved from A1 via L_irred and Schur (Steps 2–3), and only then used to establish that the gauge group must be non-abelian.

---

## 8. Connection to Paper 1

The logical relationship between the two papers is explicit:

| Paper 1 result | Paper 2 use |
|---|---|
| T2 (Hilbert space) | L_irred (irreducibility from A1) |
| T3 (gauge bundle skeleton) | Theorem R (carrier requirements) |
| T_M (Monogamy) | L_vac (vacuum assignment), L_singlet_Gram |
| L_irr (Irreversibility) | L_equip (horizon equipartition) |
| L_nc (Non-Closure) | L_nc^budget, L_nc^interf (two types) |
| L_cost (cost uniqueness skeleton) | L_Cauchy (full uniqueness proof) |

Paper 2 does not re-prove Paper 1's results.  It imports them via `from apf.core import ...` and builds on them.  A referee who accepts Paper 1 accepts Paper 2's starting point.

---

*This guide accompanies the manuscript "The Structure of Admissible Physics" submitted to Foundations of Physics, March 2026. DOI: [https://doi.org/10.5281/zenodo.18867119](https://doi.org/10.5281/zenodo.18867119)*
