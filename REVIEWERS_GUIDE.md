# Reviewers' Guide — APF Paper 2: The Structure of Admissible Physics: Non-Closure, Gauge Origin, Capacity Counting, and the 61-Type Partition

This guide is the physics-first walkthrough for peer reviewers of The Structure of Admissible Physics: Non-Closure, Gauge Origin, Capacity Counting, and the 61-Type Partition. It addresses the structural assumptions, anticipated objections, and falsification surfaces of the paper's argument. The intended audience is a peer reviewer with a background in physics or mathematics.

The guide complements three other verification routes:
- The [executable codebase](apf/) (run `python run_checks.py` for the full 14-theorem verification);
- The [Colab notebook](APF_Reviewer_Walkthrough.ipynb) (zero-install, theorem-by-theorem cells with prose + code);
- The [interactive derivation DAG](https://ethan-brooke.github.io/The-Structure-of-Admissible-Physics/) (hover-for-details, click-for-dependencies, animated verification).

---

## The derivation in 14 steps

The full chain from the foundational commitments to this paper's results:

**Step 1 — L_nc** (`check_L_nc`)

  L_nc: Non-Closure from Admissibility Physics + Locality.


**Step 2 — L_irr** (`check_L_irr`)

  L_irr: Irreversibility from Admissibility Physics.


**Step 3 — T3** (`check_T3`)

  T3: Locality -> Gauge Structure.


**Step 4 — Theorem_R** (`check_Theorem_R`)

  Theorem_R: Representation Requirements from Admissibility.


**Step 5 — L_Cauchy_uniqueness** (`check_L_Cauchy_uniqueness`)

  


**Step 6 — L_gauge_template_uniqueness** (`check_L_gauge_template_uniqueness`)

  L_gauge_template_uniqueness: SU(N_c)×SU(2)×U(1) is the Unique Gauge Template.


**Step 7 — L_anomaly_free** (`check_L_anomaly_free`)

  L_anomaly_free: Gauge Anomaly Cancellation Cross-Check [P].


**Step 8 — L_count** (`check_L_count`)

  L_count: Capacity Counting ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â 1 structural enforcement channel = 1 unit.


**Step 9 — P_exhaust** (`check_P_exhaust`)

  P_exhaust: Predicate Exhaustion (MECE Partition of Capacity).


**Step 10 — L_singlet_Gram** (`check_L_singlet_Gram`)

  L_singlet_Gram: Singlet Gram Matrix is Rank-1 [P].


**Step 11 — L_equip** (`check_L_equip`)

  L_equip: Horizon Equipartition ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â capacity fractions = energy density fractions.


**Step 12 — L_saturation_partition** (`check_L_saturation_partition`)

  L_saturation_partition: Type-Count Partition is Saturation-Independent [P].


**Step 13 — L_self_exclusion** (`check_L_self_exclusion`)

  L_self_exclusion: Self-Correlation Excluded from Microstate Counting [P].


**Step 14 — T_vacuum_stability** (`check_T_vacuum_stability`)

  T_vacuum_stability: Vacuum is Absolutely Stable [P].



Each step is a single theorem. The dependencies form a directed acyclic graph (DAG) with no cycles; the [interactive DAG](https://ethan-brooke.github.io/The-Structure-of-Admissible-Physics/) shows multiple derivation paths to the same result, which is structural redundancy: many results are over-determined and would survive even if individual derivation steps were weakened.

---

## Pre-empting the operational-witness objection

A common objection to executable mathematical appendices is that the test-case witnesses (specific small examples used to verify the theorem) "smuggle in" the very structure being derived. Each test-case witness in this paper is the smallest concrete instance of a structure already proved in the abstract argument. Witnesses are constructed *after* the abstract claim is established, never before. The reviewer can re-derive each witness from the abstract derivation chain, not the other way around. If a witness appears to smuggle structure in, the corresponding `check_*` function will fail when the witness is replaced with an explicit countermodel.

---

## The structural assumptions

Beyond Axiom A1, this paper relies on the four PLEC components and a small set of structural regularity conditions:

- **A1 (Finite Enforcement Capacity)** — at any interface, the total enforcement cost across maintained distinctions is bounded.
- **MD (Minimum Distinction)** — every physical distinction has strictly positive enforcement cost (positive floor μ\* > 0).
- **A2 (Argmin selection)** — the realized configuration is the argmin of cost over the admissible set.
- **BW (Boundary Weight / Non-degeneracy)** — the cost spectrum is rich enough that the argmin is generically informative.

The four are pairwise logically independent (proved in Paper 1's Technical Supplement §1 with explicit countermodels). Together they define the variational structure named the **Principle of Least Enforcement Cost (PLEC)**: *reality is the minimum-cost expression of distinction compatible with finite capacity.*

**Paper 2 additionally relies on:**

- **Sharing-admissibility (S):** the admissibility structure allows configurations in which distinct subsystems share resource commitments (the condition under which tensor products exist).
- **Generation-channel hypothesis (GCH):** the framework admits a generation-channel bridge connecting distinct copies of a representational structure to yield observed generational multiplicity (underwrites the $N_{\rm gen} = 3$ argument).

---

## The identifications

Several mappings between enforcement concepts and standard mathematical structures are used in the paper. They are **motivated, not deduced**, and reviewers should pay particular attention to their justification:

1. **Distinction ↔ binary partition of admissible configurations.** Spencer-Brown's distinction primitive (drawing the line between *this* and *not-this*) is identified with a binary measurement / partition at an enforcement interface. Motivated, not deduced.

2. **Cost ↔ resource expenditure.** The framework's $\varepsilon(d)$ functional is identified with the operational resource (energy / mass / barrier height) that maintains a distinction in any specific laboratory instance. This is a multi-resource correspondence; specific identifications appear in domain-specific papers (Paper 7 for action / Lagrangian, Paper 6 for spacetime metric, etc.).

3. **Capacity bound ↔ physical scarcity.** $C(\Gamma) < \infty$ at every interface is identified with the universally observed pattern that any specific physical system supports finitely many distinguishable states (Bekenstein--Hawking, Landauer, Ashby). Motivated by these traditions; not derived from them.

4. **Argmin ↔ realization.** The realized configuration at an interface is identified with the $\arg\min$ of total enforcement cost over the admissible set. This is a *locator*, not a process: nothing is doing the optimization; the argmin is what realization *means* under the framework.

5. **Hilbert space ↔ minimal representation of the noncommutative enforcement algebra.** Per the Paper 1 GNS argument, complex Hilbert space appears as the *unique* representational target for the algebraic structure that finite enforcement forces. Not assumed; selected via Frobenius.

These identifications are conventional rather than discovered: they are the choice that makes the framework's vocabulary and standard mathematics align. None is internally derivable.

---

## What is *not* proved in this paper

To prevent scope inflation, the following are flagged explicitly as *outside* the scope of Structure of Admissible Physics:

- **Specific gauge-group derivations** belong to Paper 2; this paper assumes them as imports if cited.
- **Specific particle content / generation count** belongs to Papers 2 and 4; not derived here.
- **Quantitative cosmological observables** beyond what is explicitly cited belong to Papers 3 (entropy / horizon) and 6 (geometry / DESI).
- **Quantum-gravity backreaction** is out of scope for any single paper in the v6.8 series; it is a future direction.
- **Numerical mass values** (absolute scales for $m_t$, $m_b$, $m_\nu$) are open problems noted in Paper 4 and the Engine paper; not within this paper's scope.
- **Spacetime dimension** (D = 4) is structurally derived in Paper 6 from Lovelock uniqueness; this paper assumes it where used.

If a reviewer concludes that the paper claims any of the above without supplying a proof for it, the reviewer is correct that the paper does not deliver that claim — those claims belong to other papers in the series and are explicitly flagged as such.

---

## How to falsify: attack surfaces

Each falsifier below targets a specific theorem or structural assumption. The corresponding code change in `apf/core.py` is also identified; reviewers can modify the codebase and re-run `python run_checks.py` to test each surface directly.

| # | Surface | Code-level test |
|---|---------|------------------|
| 1 | **Numerical disagreement.** A predicted observable disagrees with experiment beyond the framework's stated tolerance. | Modify the corresponding `check_*` to use the published experimental value; observe failure. |
| 2 | **Structural redundancy collapse.** Removing one PLEC component (A1, MD, A2, BW) leaves the derivation chain intact. | Comment out the test for the removed component in `apf/core.py`; observe other downstream checks failing. |
| 3 | **Reconstruction-program parity.** A standard quantum reconstruction (Hardy / CDP / Masanes--Müller) reaches the same conclusion with a strictly weaker assumption set. | Extract the GPT axioms used by the comparator; supply them as inputs to the relevant `apf/core.py` functions. |
| 4 | **Composition / locality break.** A multi-interface test with one interface deliberately violating $L_{\rm loc}$ does not produce the expected falsification mode. | Modify `check_L_loc` countermodel; rerun and observe expected vs. actual behavior. |
| 5 | **Cost-functional uniqueness fails.** An alternative cost functional satisfies all framework axioms equally well. | Replace the cost functional in `apf_utils.py`; observe whether downstream checks still pass. |
| 6 | **Scope-creep test.** A claim attributed to this paper is shown to actually require an unstated assumption. | Trace the claim's `\coderef`s through the bank dependency chain; identify any check that exits the paper's named scope. |

This is a structured threat model. If any of the surfaces fails empirically, the paper falsifies on that specific point.

---

## Reading the code

The codebase has three files in `apf/`:

- **`apf/core.py`** — the 14 theorem check functions for this paper. Each function constructs a mathematical witness, verifies the theorem's claim, and returns a structured result with name, dependencies, status, and key result.
- **`apf/apf_utils.py`** — exact arithmetic utilities (mostly `Fraction`-based; numpy/scipy where required by specific numerical lemmas).
- **`apf/bank.py`** — registry of all check functions in this repo, plus the `run_all()` runner.

Execution model: `run_checks.py` calls `bank.run_all()`, which iterates over every registered check and aggregates pass/fail/error counts. Individual checks can be invoked via `apf.bank.get_check('T_Born')()`.

---

## Scalar-to-matrix boundary

A characteristic feature of the APF program is that the early derivations use only finite sets and exact rational arithmetic (no matrices, no complex numbers, no linear algebra). Matrices first appear at the GNS construction (T2 in Paper 1), as the *minimal representation* of structure that the earlier scalar-only theorems prove must exist. This paper inherits the scalar-to-matrix transition from Paper 1's $T_2$. No new derivations of matrix structure occur in this paper; matrices appear where Paper 1 already established them.

This stratification is a deliberate methodological commitment: matrices are derived as representations of an already-proved abstract structure, not assumed as the substrate of the framework.

---

## The complex-field justification

The complex numbers as the unique admissible amplitude field is not a postulate but a derived selection (Paper 1 T2c, with proved exclusions $P_{\rm tom}$ and $P_{\rm cls}$ ruling out $\mathbb{R}$ and $\mathbb{H}$ respectively). This paper does not re-derive the complex-field selection; it inherits from Paper 1 ($T_{2c}$, with proved exclusions $P_{\rm tom}$ and $P_{\rm cls}$). For the original derivation, see Paper 1's [REVIEWERS_GUIDE.md](https://github.com/Ethan-Brooke/The-Enforceability-of-Distinction/blob/main/REVIEWERS_GUIDE.md).

---

## Citation and Zenodo

This repository is the executable mathematical appendix to APF Paper 2. The canonical archival deposit is at [https://doi.org/10.5281/zenodo.18604839](https://doi.org/10.5281/zenodo.18604839) (DOI: 10.5281/zenodo.18604839).

---

*Generated by the APF `create-repo` skill. Codebase snapshot: v6.8 (frozen 2026-04-18; 348 verify_all checks, 335 bank-registered theorems, 48 quantitative predictions).*
