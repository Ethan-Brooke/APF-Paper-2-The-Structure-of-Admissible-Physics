# The Structure of Admissible Physics

### Interactive Mathematical Appendix to Paper 2 of the Admissibility Physics Framework

<p align="center">
  <a href="https://doi.org/10.5281/zenodo.18867119"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.18867119.svg" alt="DOI"></a>
  <a href="https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics/blob/main/APF_Reviewer_Walkthrough_Paper2.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a>
</p>

<p align="center">
  <a href="#theorem-mapping-table">Theorem Map</a> ·
  <a href="REVIEWERS_GUIDE.md">Reviewers' Guide</a> ·
  <a href="#citation">Citation</a> ·
  <a href="https://doi.org/10.5281/zenodo.18439200">Paper 1</a>
</p>

---

## Interactive resources

Two browser-based visualisations are hosted on GitHub Pages and require no installation:

| Resource | Description |
|----------|-------------|
| **[Derivation DAG ↗](https://ethan-brooke.github.io/APF-Paper-2-The-Structure-of-Admissible-Physics/)** | 33-node interactive theorem graph — click any node for dependencies, path count, and shortest chain to A1; animate full topological verification |
| **[Visual Storyboard ↗](https://ethan-brooke.github.io/APF-Paper-2-The-Structure-of-Admissible-Physics/storyboard.html)** | 12-panel illustrated walkthrough from the hydrogen atom to Ω_Λ = 42/61 — arrow-key navigation, panel quotes, colour-coded derivation flow |

Both are standalone HTML files in `docs/` — no framework, no build step.

---

## Why this codebase exists

Paper 1 derived the quantum skeleton from a single axiom — finite enforcement capacity (A1) — producing Hilbert spaces, the Born rule, gauge symmetry, and entropy.  Paper 2 deploys those results.

The central result is the **Non-Closure Theorem**: individually admissible enforcement demands, when composed at shared interfaces, generically exceed local budgets.  Non-closure is the engine behind all competition, selection, and structure in the framework.  The paper then shows that non-closure *requires* non-abelian gauge structure, identifies that structure uniquely as SU(3) × SU(2) × U(1), derives the Standard Model fermion content by exhaustive elimination, counts 61 structural enforcement channels, and partitions them — without free parameters or empirical inputs — into the cosmological density fractions Ω_Λ = 42/61 and Ω_m = 19/61.

This repository is the executable proof of those claims.

All check functions use the same design principle as Paper 1: every result traces to a named function that constructs a mathematical witness and returns a structured result with its dependencies, epistemic status, and a summary of what was proved.  The codebase requires **Python 3.9+ and the standard library only** — no NumPy, no SciPy, no external dependencies.

## How to verify

**1. Colab notebook — zero install.** [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics/blob/main/APF_Reviewer_Walkthrough_Paper2.ipynb) Annotated cells walking through the full derivation chain from L_nc to Ω_Λ = 42/61.

**2. Local — no pip install.**
```bash
git clone https://github.com/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics.git
cd APF-Paper-2-The-Structure-of-Admissible-Physics
python run_checks.py
```
Expected output:
```
  Paper 2 (STRUCTURE): all checks passed — gauge template, fermion content, capacity partition
```

**3. Individual inspection.**
```python
from apf.gauge import check_L_gauge_template_uniqueness
r = check_L_gauge_template_uniqueness()
print(r['key_result'])
# → "SU(3) × SU(2) × U(1) is the unique admissible gauge template"

from apf.gauge import check_T_field
r = check_T_field()
print(r['key_result'])
# → "Standard Model fermion content: 45 Weyl DOF, unique survivor of 4680-template scan"
```

For referees, a [dedicated guide](REVIEWERS_GUIDE.md) walks through the logical architecture, the key proof steps, and six falsification surfaces.

---

## Theorem mapping table

| Theorem | Manuscript | Code | What is mathematically verified |
|---------|-----------|------|-------------------------------|
| **L_nc^budget** (Budget Non-Closure) | §3 | `check_L_nc_budget()` in `core.py` | Classical pigeonhole: two individually admissible demands exceed shared capacity; symmetric surplus Δ₁₂ = Δ₂₁ |
| **L_nc^interf** (Interference Non-Closure) | §3 | `check_L_nc_interf()` in `core.py` | Quantum case: order-asymmetric surplus Δ₁₂ ≠ Δ₂₁; superadditivity of joint enforcement cost |
| **L_irred** (Irreducibility from A1) | §4 | `check_L_irred()` in `core.py` | A1 distinguishability requirement forces irreducible action on H: no proper invariant subspace |
| **L_Δ→nc** (Non-Commutativity) | §4 | `check_L_delta_nc()` in `core.py` | Schur's lemma on irreducible H: no non-trivial operator commutes with full algebra → AB ≠ BA |
| **L_Cauchy** (Cost Function Uniqueness) | §5 | `check_L_Cauchy_uniqueness()` in `L_Cauchy_uniqueness.py` | Cauchy (1821): unique monotone additive F with F(1)=1 is F(d)=d; no free parameter |
| **T_R1** (Ternary Carrier) | §6 | `check_Theorem_R()` in `gauge.py` | Confinement forces complex ternary carrier: orientation requires ε_ijk trilinear invariant; dim=3 minimal |
| **T_R2** (Chiral Carrier) | §6 | `check_Theorem_R()` in `gauge.py` | Intrinsic gauge irreversibility (not environmental) forces pseudoreal 2-dim carrier |
| **T_R3** (Abelian Grading) | §6 | `check_Theorem_R()` in `gauge.py` | Enforcement completeness (A1) + minimality forces exactly one U(1); SU(3)×SU(2) anomaly-free without it |
| **L_gauge_template_uniqueness** (Gauge Group) | §6 | `check_L_gauge_template_uniqueness()` in `gauge.py` | All 17 compact simple Lie algebras classified; SU(N_c) family unique passer; N_c=3 by minimality |
| **T_field** (Fermion Content) | §7 | `check_T_field()` in `gauge.py` | 4,680 chiral templates scanned; 7 sequential filters applied; unique survivor: SM at 45 Weyl DOF |
| **L_hypercharge** (Hypercharge Uniqueness) | §7 | `check_L_hypercharge()` in `gauge.py` | Anomaly cancellation + minimality uniquely fixes all 5 hypercharges; no free parameter |
| **L_count** (C_total = 61) | §8 | `check_L_count()` in `gauge.py` | Structural channel count: 45 fermion + 12 gauge + 4 Higgs = 61; each rep = one channel (L_species) |
| **L_species** (Channel Counting Principle) | §8 | `check_L_species()` in `gauge.py` | Each irreducible representation = one structural enforcement channel; kinematic DOF are free |
| **L_vac** (Vacuum Assignment) | §8 | `check_L_vac()` in `gauge.py` | Three-case exhaustion assigns 12 gauge + 27 fermion-internal + 3 Higgs-Goldstone to vacuum sector |
| **L_singlet_Gram** (Rank-1 Dark Sector) | §9 | `check_L_singlet_Gram()` in `gauge.py` | Q2=0 zeroes SU(3) components of 16 dark-sector demand vectors; Gram matrix rank=1; σ/m=0 at leading order |
| **L_equip** (Horizon Equipartition) | §10 | `check_L_equip()` in `gauge.py` | Microcanonical argument at Bekenstein horizon: each of 61 types carries equal share → Ω = \|sector\|/61 |
| **L_sat_part** (Saturation Independence) | §10 | `check_L_sat_partition()` in `gauge.py` | MECE partition 42+3+16=61 holds at all saturation levels; Ω_Λ = 42/61, Ω_m = 19/61 |

All check functions reside in `apf/core.py`, `apf/gauge.py`, and `apf/L_Cauchy_uniqueness.py`.

---

## The derivation chain

```
                              A1
                    (finite enforcement capacity)
                              │
                    ┌─────────┴──────────┐
                    │                    │
            L_nc^budget           L_nc^interf
          (classical surplus)   (order-asymmetric Δ)
                                         │
                                    L_irred
                               (irreducibility from A1)
                                         │
                                    L_Δ→nc
                               (Schur: AB ≠ BA)
                                         │
                    ┌────────────────────┼────────────────────┐
                    │                    │                    │
               L_Cauchy            Theorem R            L_species
           (F(d) = d unique)   (R1, R2, R3 carriers)  (rep = channel)
                                         │
                          L_gauge_template_uniqueness
                            SU(3) × SU(2) × U(1)
                                         │
                        ┌────────────────┼──────────────┐
                        │                │              │
                   T_field          L_count          L_vac
               (45 Weyl DOF)       (61 types)    (42 vacuum)
                                         │
                              L_singlet_Gram + L_equip
                              Ω_Λ = 42/61, Ω_m = 19/61
```

---

## Repository structure

```
├── README.md                          ← you are here
├── REVIEWERS_GUIDE.md                 ← dedicated guide for peer reviewers
├── apf/
│   ├── core.py                        ← foundational lemmas (L_nc, L_irred, L_Δ→nc, L_equip)
│   ├── gauge.py                       ← gauge template, fermion scan, capacity partition
│   ├── L_Cauchy_uniqueness.py         ← cost function uniqueness
│   ├── apf_utils.py                   ← exact arithmetic utilities
│   └── bank.py                        ← theorem registry and runner
├── APF_Reviewer_Walkthrough_Paper2.ipynb  ← Colab notebook for referees
├── run_checks.py                      ← convenience entry point
├── pyproject.toml                     ← metadata (zero dependencies)
├── .zenodo.json                       ← archival metadata
└── LICENSE                            ← MIT
```

---

## What this paper derives and what it does not

**Derived:**
Non-closure (two types), non-commutativity from A1 (L_irred + Schur), cost function uniqueness (Cauchy), gauge template SU(3)×SU(2)×U(1) (17-algebra classification), fermion content at 45 Weyl DOF (4,680-template scan), hypercharge assignments, C_total = 61, MECE partition 42+3+16, cosmological fractions Ω_Λ = 42/61 and Ω_m = 19/61.

**Not derived here (later papers):**
Quantitative mass predictions (Paper 4B), mixing angles and CP violation (Paper 4B), absolute EW scale and VEV (Paper 4A/6), spacetime dimension d=4 (Paper 5), Lorentzian signature (Paper 5), inflation (Paper 6), gravitational dynamics (Paper 6), the 47 zero-parameter quantitative predictions (Papers 4–7 combined).

---

## Citation

```bibtex
@software{apf-paper2,
  title   = {The Structure of Admissible Physics: Non-Closure, Gauge Origin,
             Capacity Counting, and the 61-Type Partition},
  author  = {Ethan Brooke},
  year    = {2026},
  doi     = {10.5281/zenodo.18867119},
  url     = {https://github.com/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics}
}
```

## License

MIT. See [LICENSE](LICENSE).
