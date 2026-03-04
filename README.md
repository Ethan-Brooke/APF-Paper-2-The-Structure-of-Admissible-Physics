# APF Paper 2 — The Structure of Admissible Physics

**Non-Closure, Gauge Origin, Capacity Counting, and the 61-Type Partition**

*E. S. Brooke — Admissibility Physics Framework, Paper 2*

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen.svg)]()

---

## Overview

Paper 1 established the quantum skeleton: Hilbert space, the Born rule, gauge symmetry, tensor products, and entropy — all from a single axiom (A1: enforcement capacity is finite and positive). Paper 2 deploys those results to derive the specific architecture of admissible physics.

The central engine is the **Non-Closure Theorem** ($L_\mathrm{nc}$): individually admissible enforcement demands, when composed at shared interfaces, generically exceed local budgets. This excess — the interference surplus $\Delta > 0$ — forces non-abelian gauge structure, drives the selection of SU(3) × SU(2) × U(1), and determines the full matter content.

**What this paper derives, from A1 alone:**

| Result | Theorem | Value |
|--------|---------|-------|
| Gauge group forced | $T_\mathrm{gauge}$ | SU(3) × SU(2) × U(1) |
| Fermion content | $T_\mathrm{field}$ | 45 Weyl fermions (1 of 4,680 survives) |
| Cost function uniqueness | $L_\mathrm{Cauchy}$ | F(d) = d, no alternatives |
| Capacity total | $L_\mathrm{count}$ | C_total = 45 + 4 + 12 = **61** |
| Vacuum/matter partition | $P_\mathrm{exhaust}$ | 42 + 3 + 16 = 61 (MECE) |
| Cosmological fractions | $L_\mathrm{equip}$ | Ω_Λ = 42/61 = 0.6885, Ω_m = 19/61 = 0.3115 |

**Free parameters introduced: 0. Physics imported: 0.**

---

## The Derivation Chain

```
A1  (enforcement capacity is finite and positive)
 │
 ├─→ L_nc  (non-closure: ΔC > 0 at shared interfaces)
 │    ├─→ L_irred  (irreducible representations forced)
 │    ├─→ L_Δ→nc  (interference surplus ↔ non-commutativity)
 │    └─→ T_confinement  (IR saturation → singlets only)
 │
 ├─→ L_irr  (irreversibility: some commitments cannot be undone)
 │    └─→ chiral carrier requirement
 │
 ├─→ L_loc  (locality: enforcement is interface-local)
 │    └─→ L_Cauchy  (cost function uniqueness: F(d) = d)
 │
 └─→ [L_nc + L_irr + T_M + T_conf + B₁'] ──→  Theorem R
          │                                    (R1: ternary carrier)
          │                                    (R2: chiral carrier)
          │                                    (R3: abelian grading)
          │
          └─→ L_gauge,unique  (17 Lie algebras → 1 structure)
               └─→ T_gauge  (N_c = 3 by cost minimality)
                    ├─→ T_field  (4,680 templates → 45 Weyl fermions)
                    │    ├─→ L_hypercharge  (unique Y assignments)
                    │    └─→ T_Higgs  (1 complex SU(2) doublet)
                    │
                    └─→ L_count  (C_total = 61)
                         └─→ P_exhaust  (42 vacuum + 3 baryonic + 16 dark)
                              ├─→ L_equip  (Ω_Λ = 42/61, Ω_m = 19/61)
                              └─→ L_sat,part  (partition is topological)
```

**Interactive version:** [View the live DAG visualization →](https://ethan-brooke.github.io/APF-Paper-2-The-Structure-of-Admissible-Physics/)

---

## Repository Contents

```
APF-Paper-2-The-Structure-of-Admissible-Physics/
│
├── core.py                    # Axiom A1, L_nc, L_irr, L_loc, L_ε* — foundational lemmas
├── gauge.py                   # Gauge derivation: Theorem R, T_gauge, T_field, L_count
├── L_Cauchy_uniqueness.py     # Cost function uniqueness (Cauchy 1821)
├── bank.py                    # Theorem registry — run_all() executes all checks
├── apf_utils.py               # Shared utilities (linalg, DAG cache, constants)
│
├── docs/
│   └── index.html             # Interactive DAG visualization (GitHub Pages)
│
├── CITATION.cff               # Citation metadata
└── README.md
```

---

## Quick Start

**Requirements:** Python 3.8+, zero external dependencies (stdlib only).

```bash
git clone https://github.com/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics.git
cd APF-Paper-2-The-Structure-of-Admissible-Physics
```

**Run the full theorem bank:**
```python
from bank import run_all
results = run_all()
```

**Run individual Paper 2 checks:**
```python
from core import check_L_nc, check_L_irred
from gauge import (check_Theorem_R, check_T_gauge, check_T_field,
                   check_L_gauge_template_uniqueness, check_L_count)
from core import check_P_exhaust
from L_Cauchy_uniqueness import check_L_Cauchy_uniqueness

# Non-closure: the engine of structure
r = check_L_nc()
print(r['summary'])
# → L_nc PASS: interference surplus Δ = 0.250 > 0. Admissible sets not closed.

# Gauge template uniqueness (17 Lie algebras → 1 structure)
r = check_L_gauge_template_uniqueness()
print(r['summary'])
# → L_gauge_template_uniqueness PASS: SU(N_c)×SU(2)×U(1) unique (17 algebras scanned)

# Fermion content (4,680 chiral templates → 1 survivor)
r = check_T_field()
print(r['summary'])
# → T_field PASS: 45 Weyl fermions, 3 generations. 4679 templates excluded.

# Capacity counting
r = check_L_count()
print(r['summary'])
# → L_count PASS: C_total = 61 (45 fermions + 4 Higgs + 12 gauge)

# MECE partition
r = check_P_exhaust()
print(r['summary'])
# → P_exhaust PASS: 42 vacuum + 3 baryonic + 16 dark = 61
```

**Run cosmological predictions:**
```python
from cosmology import check_L_equip, check_L_saturation_partition

r = check_L_equip()
print(r['summary'])
# → L_equip PASS: Ω_Λ = 42/61 = 0.6885 (obs 0.6889, err 0.05%)
```

---

## Theorem Index

All theorems in this paper, with their check functions and dependency sources:

| Name | Full title | Code | Module |
|------|-----------|------|--------|
| $L_\mathrm{nc}^\mathrm{budget}$ | Budget Non-Closure | `check_L_nc` | `core.py` |
| $L_\mathrm{nc}^\mathrm{interf}$ | Interference Non-Closure | `check_L_nc`, `check_T1` | `core.py` |
| $L_\mathrm{irred}$ | Irreducibility from A1 | `check_L_irred` | `core.py` |
| $L_{\Delta\to\mathrm{nc}}$ | Interference Non-Closure → Non-Commutativity | `check_T0`, `check_L_nc` | `core.py` |
| $T_\mathrm{confinement}$ | Confinement Mechanism | `check_T_confinement` | `gauge.py` |
| Theorem R | Representation Requirements (R1–R3) | `check_Theorem_R` | `gauge.py` |
| $L_\mathrm{Cauchy}$ | Cost Function Uniqueness | `check_L_Cauchy_uniqueness` | `L_Cauchy_uniqueness.py` |
| $L_\mathrm{gauge,uniq}$ | Gauge Template Uniqueness | `check_L_gauge_template_uniqueness` | `gauge.py` |
| $T_\mathrm{gauge}$ | Gauge Group Selection (N_c = 3) | `check_T_gauge` | `gauge.py` |
| $T_\mathrm{field}$ | SM Fermion Content | `check_T_field` | `gauge.py` |
| $L_\mathrm{hypercharge}$ | Unique Hypercharge Assignment | `check_L_anomaly_free` | `gauge.py` |
| $T_\mathrm{Higgs}$ | Scalar Sector | `check_T_Higgs` | `gauge.py` |
| $L_\mathrm{species}$ | Species as Enforcement Channels | `check_L_species` | `gauge.py` |
| $L_\mathrm{count}$ | Capacity Counting (C = 61) | `check_L_count` | `gauge.py` |
| $P_\mathrm{exhaust}$ | MECE Partition (42 + 3 + 16) | `check_P_exhaust` | `core.py` |
| $L_\mathrm{vac}$ | Vacuum Sector Assignment | `check_P_exhaust` | `core.py` |
| $L_\mathrm{singlet,Gram}$ | Rank-1 Dark Sector | `check_L_singlet_Gram` | `cosmology.py` |
| $L_\mathrm{equip}$ | Horizon Equipartition | `check_L_equip` | `cosmology.py` |
| $L_\mathrm{sat,part}$ | Saturation-Independent Partition | `check_L_saturation_partition` | `cosmology.py` |
| $L_\mathrm{self\text{-}excl}$ | Effective Dimension (d_eff = 102) | `check_L_self_exclusion` | `gravity.py` |

---

## The 61-Type Partition

The capacity budget partitions by two mechanism predicates (confines? / has mass via SSB?), yielding a MECE decomposition:

```
C_total = 61
         ├── Vacuum sector  (42):  gauge bosons + Higgs — no SSB mass, confines or abelian
         └── Matter sector  (19):
              ├── Baryonic  ( 3):  quarks — confines, carries baryon number
              └── Dark       (16):  right-handed neutrinos + dark matter — neither confines nor SSB
```

This partition is **topological**: the fractions Ω_Λ = 42/61 and Ω_m = 19/61 are invariants of the matching structure, independent of the saturation level. They cannot evolve, cannot be tuned, and cannot depend on continuous parameters.

**Observational status:**

| Prediction | APF value | Observed | Error |
|-----------|-----------|----------|-------|
| Ω_Λ = 42/61 | 0.68852 | 0.6889 ± 0.0056 | 0.05% |
| Ω_m = 19/61 | 0.31148 | 0.3111 ± 0.0056 | 0.12% |
| Ω_b/Ω_m = 3/19 | 0.15789 | 0.1571 ± 0.0030 | 0.5% |

---

## Falsification Targets

The structural claims of this paper are sharp enough to falsify. Constructive counter-models are explicitly invited:

- **(F1)** An A1-compatible interaction theory that does not require R1–R3 (ternary carrier, chiral carrier, abelian grading).
- **(F2)** A compact gauge group with dim(G) < 12 hosting all three carrier requirements.
- **(F3)** A cost functional compatible with A1 (additive, monotone, positively normalized) other than F(d) = d.
- **(F4)** A chiral fermion set with fewer than 45 Weyl degrees of freedom satisfying all seven filters.
- **(F5)** A demonstration that kinematic degrees of freedom (polarizations, helicities) are structurally enforceable at Bekenstein saturation, changing C_total from 61.

Experimentally:
- **(F6)** A fourth fermion generation participating coherently without saturation-like behavior.
- **(F7)** Dirac neutrinos with standard electroweak couplings.
- **(F8)** Dark matter as a fundamental particle species outside the Standard Model field content.

---

## Series Context

This is Paper 2 of the **Admissibility Physics Framework** (APF), a seven-paper series deriving Standard Model structure from a single axiom.

| Paper | Title | Core result |
|-------|-------|-------------|
| **Paper 1** | [The Enforceability of Distinction](https://github.com/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction) | Quantum skeleton from A1 |
| **Paper 2** | *This repository* | Gauge group, matter content, C_total = 61 |
| Paper 3 | The Ledgers | Thermodynamic structure, entropy arrow |
| Paper 4A | Constraints I | Gauge uniqueness, field content |
| Paper 4B | Constraints II | Masses, mixing, CP violation |
| Paper 5 | Quantum Geometry | Spacetime from capacity geometry |
| Paper 6 | Dynamics | Cosmological trajectory through S_adm |
| Paper 7 | The Action | Structural closure, BSM exclusion |

---

## Citation

```bibtex
@article{Brooke2026APFPaper2,
  author  = {Brooke, E. S.},
  title   = {{Paper 2: The Structure of Admissible Physics}},
  subtitle = {Non-Closure, Gauge Origin, Capacity Counting, and the 61-Type Partition},
  year    = {2026},
  doi     = {10.5281/zenodo.XXXXXXX},
  url     = {https://github.com/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics},
  note    = {Admissibility Physics Framework, Paper 2}
}
```

---

## License

This repository is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The codebase may be freely used, adapted, and redistributed with attribution.

---

*ORCID: [0009-0001-2261-4682](https://orcid.org/0009-0001-2261-4682) · Contact: ebrooke@cleanwater1.com*
