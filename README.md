# The Structure of Admissible Physics: Non-Closure, Gauge Origin, Capacity Counting, and the 61-Type Partition

### Interactive Mathematical Appendix to Paper 2 of the Admissibility Physics Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18604839.svg)](https://doi.org/10.5281/zenodo.18604839) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics/blob/main/APF_Reviewer_Walkthrough.ipynb)

[Interactive Derivation DAG](https://ethan-brooke.github.io/APF-Paper-2-The-Structure-of-Admissible-Physics/) · [Theorem Map](#theorem-mapping-table) · [Reviewers' Guide](REVIEWERS_GUIDE.md) · [The full APF corpus](#the-full-apf-corpus) · [Citation](#citation)

> **AI agents:** start with [`START_HERE.md`](START_HERE.md) — operational checklist that loads the framework context in 5–10 minutes. The corpus inventory and full file map are in [`ai_context/repo_map.json`](ai_context/repo_map.json).

---

## Why this codebase exists

Non-closure theorem: the admissibility algebra admits no single representation valid across all admissibility regimes. Gauge template uniqueness (SU(3)*SU(2)*U(1) with N_c=3); 1-of-4680 surviving fermion template (45 Standard Model fermions); capacity partition C_total = 61 = 42 + 19 yielding cosmological fractions Omega_Lambda = 42/61 and Omega_m = 19/61, weak mixing angle sin^2(theta_W) = 3/13.

This repository is the executable proof.

The codebase is a faithful subset of the canonical APF codebase v6.9 (frozen 2026-04-18; 355 verify_all checks, 342 bank-registered theorems across 19 modules + `apf/standalone/`). Each theorem in the manuscript traces to a named `check_*` function in `apf/core.py`, which can be called independently and returns a structured result.

The codebase requires Python 3.8+ and NumPy / SciPy (some numerical lemmas use them; see `pyproject.toml`).

## How to verify

Three paths, in order of increasing friction:

**1. Colab notebook — zero install.** [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics/blob/main/APF_Reviewer_Walkthrough.ipynb) Every key theorem is derived inline, with annotated cells you can inspect and modify. Run all cells — the full verification takes under a minute.

**2. Browser — zero install.** Open the [Interactive Derivation DAG](https://ethan-brooke.github.io/APF-Paper-2-The-Structure-of-Admissible-Physics/). Explore the dependency graph. Hover any node for its mathematical statement, key result, and shortest derivation chain to A1. Click **Run Checks** to watch all theorems verify in topological order.

**3. Local execution.**

```bash
git clone https://github.com/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics.git
cd APF-Paper-2-The-Structure-of-Admissible-Physics
pip install -e .
python run_checks.py
```

Expected output:

```
      Paper 2 (The Structure of Admissible Physics): 14 passed, 0 failed, 14 total — verified in <minutes>
```

**4. Individual inspection.**

```python
from apf.bank import get_check
r = get_check('check_L_nc')()
print(r['key_result'])
```

For reviewers, a [dedicated guide](REVIEWERS_GUIDE.md) walks through the logical architecture, the structural assumptions, and the anticipated objections.

---

## Theorem mapping table

This table maps every result in the manuscript to its executable verification.

| Check | Type | Summary |
|-------|------|---------|
| `check_L_nc` | Lemma | L_nc: Non-Closure from Admissibility Physics + Locality. |
| `check_L_irr` | Lemma | L_irr: Irreversibility from Admissibility Physics. |
| `check_T3` | Theorem | T3: Locality -> Gauge Structure. |
| `check_Theorem_R` | Theorem | Theorem_R: Representation Requirements from Admissibility. |
| `check_L_Cauchy_uniqueness` | Lemma |  |
| `check_L_gauge_template_uniqueness` | Lemma | L_gauge_template_uniqueness: SU(N_c)×SU(2)×U(1) is the Unique Gauge Template. |
| `check_L_anomaly_free` | Lemma | L_anomaly_free: Gauge Anomaly Cancellation Cross-Check [P]. |
| `check_L_count` | Lemma | L_count: Capacity Counting ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â 1 structural enforcement channel = 1 unit. |
| `check_P_exhaust` | Other | P_exhaust: Predicate Exhaustion (MECE Partition of Capacity). |
| `check_L_singlet_Gram` | Lemma | L_singlet_Gram: Singlet Gram Matrix is Rank-1 [P]. |
| `check_L_equip` | Lemma | L_equip: Horizon Equipartition ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â capacity fractions = energy density fractions. |
| `check_L_saturation_partition` | Lemma | L_saturation_partition: Type-Count Partition is Saturation-Independent [P]. |
| `check_L_self_exclusion` | Lemma | L_self_exclusion: Self-Correlation Excluded from Microstate Counting [P]. |
| `check_T_vacuum_stability` | Theorem | T_vacuum_stability: Vacuum is Absolutely Stable [P]. |

All check functions reside in `apf/core.py`. Every function listed above can be called independently and returns a structured result including its logical dependencies and the mathematical content it verifies.

---

## The derivation chain

```
  Level 0: L_nc · L_irr · T3 · Theorem_R · L_Cauchy_uniqueness · L_gauge_template_uniqueness · L_anomaly_free · L_count · P_exhaust · L_singlet_Gram · L_equip · L_saturation_partition · L_self_exclusion · T_vacuum_stability
```

The [interactive DAG](https://ethan-brooke.github.io/APF-Paper-2-The-Structure-of-Admissible-Physics/) shows the full graph with hover details and animated verification.

---

## Repository structure

```
├── README.md                              ← you are here
├── START_HERE.md                          ← AI operational checklist; read-first for AI agents
├── REVIEWERS_GUIDE.md                     ← physics-first walkthrough for peer reviewers
├── ai_context/                            ← AI onboarding pack (corpus map, theorems, glossary, etc.)
│   ├── AGENTS.md                          ← authoritative entry point for AI agents
│   ├── FRAMEWORK_OVERVIEW.md              ← APF in 5 minutes
│   ├── GLOSSARY.md                        ← axioms, PLEC primitives, epistemic tags
│   ├── AUDIT_DISCIPLINE.md                ← engagement posture for critique/proposal
│   ├── OPEN_PROBLEMS.md                   ← catalog of open problems + verdicts
│   ├── repo_map.json                      ← machine-readable map of this repo
│   ├── theorems.json                      ← machine-readable theorem catalog
│   ├── derivation_graph.json              ← theorem DAG as JSON
│   └── wiki/                              ← bundled APF wiki (concepts, papers, codebase)
├── apf/
│   ├── core.py                            ← 14 theorem check functions
│   ├── apf_utils.py                       ← exact arithmetic + helpers
│   └── bank.py                            ← registry and runner
├── docs/
│   └── index.html                         ← interactive derivation DAG (GitHub Pages)
├── APF_Reviewer_Walkthrough.ipynb         ← Colab notebook
├── run_checks.py                          ← convenience entry point
├── pyproject.toml                         ← package metadata
├── zenodo.json                            ← archival metadata
├── Paper_2_Structure_of_Admissible_Physics_v5.3-PLEC.tex                ← the paper
├── Paper_2_Structure_of_Admissible_Physics_Supplement_v2.tex                ← Technical Supplement

└── LICENSE                                ← MIT
```

---

## What this paper derives and what it does not

**Derived:** (see Theorem mapping table above)

**Not derived here:** Specific results outside this paper's scope live in companion papers — see the corpus table below for the full 9-paper series.

---

## Citation

```bibtex
@software{apf-paper2,
  title   = {The Structure of Admissible Physics: Non-Closure, Gauge Origin, Capacity Counting, and the 61-Type Partition},
  author  = {Brooke, Ethan},
  year    = {2026},
  doi     = {10.5281/zenodo.18604839},
  url     = {https://github.com/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics}
}
```

For the full citation lineage (concept-DOI vs version-DOI, related identifiers, bibtex for all corpus papers), see [`ai_context/CITING.md`](ai_context/CITING.md).

---

## The full APF corpus

This repository is **one paper-companion** in a 9-paper series. Each paper has its own companion repo following this same layout. The full corpus, with canonical references:

| # | Title | Zenodo DOI | GitHub repo | Status |
|---|---|---|---|---|
| 0 | What Physics Permits | [10.5281/zenodo.18605692](https://doi.org/10.5281/zenodo.18605692) | [`APF-Paper-0-What-Physics-Permits`](https://github.com/Ethan-Brooke/APF-Paper-0-What-Physics-Permits) | public |
| 1 | The Enforceability of Distinction | [10.5281/zenodo.18604678](https://doi.org/10.5281/zenodo.18604678) | [`APF-Paper-1-The-Enforceability-of-Distinction`](https://github.com/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction) | public |
| 2 | The Structure of Admissible Physics **(this repo)** | [10.5281/zenodo.18604839](https://doi.org/10.5281/zenodo.18604839) | [`APF-Paper-2-The-Structure-of-Admissible-Physics`](https://github.com/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics) | public |
| 3 | Ledgers | [10.5281/zenodo.18604844](https://doi.org/10.5281/zenodo.18604844) | [`APF-Paper-3-Ledgers-Entropy-Time-Cost`](https://github.com/Ethan-Brooke/APF-Paper-3-Ledgers-Entropy-Time-Cost) | public |
| 4 | Admissibility Constraints and Structural Saturation | [10.5281/zenodo.18604845](https://doi.org/10.5281/zenodo.18604845) | [`APF-Paper-4-Admissibility-Constraints-Field-Content`](https://github.com/Ethan-Brooke/APF-Paper-4-Admissibility-Constraints-Field-Content) | public |
| 5 | Quantum Structure from Finite Enforceability | [10.5281/zenodo.18604861](https://doi.org/10.5281/zenodo.18604861) | [`APF-Paper-5-Quantum-Structure-Hilbert-Born`](https://github.com/Ethan-Brooke/APF-Paper-5-Quantum-Structure-Hilbert-Born) | public |
| 6 | Dynamics and Geometry as Optimal Admissible Reallocation | [10.5281/zenodo.18604874](https://doi.org/10.5281/zenodo.18604874) | [`APF-Paper-6-Dynamics-Geometry-Spacetime-Gravity`](https://github.com/Ethan-Brooke/APF-Paper-6-Dynamics-Geometry-Spacetime-Gravity) | public |
| 7 | Action, Internalization, and the Lagrangian | [10.5281/zenodo.18604875](https://doi.org/10.5281/zenodo.18604875) | [`APF-Paper-7-Action-Internalization-Lagrangian`](https://github.com/Ethan-Brooke/APF-Paper-7-Action-Internalization-Lagrangian) | public |
| 13 | The Minimal Admissibility Core | [10.5281/zenodo.18614663](https://doi.org/10.5281/zenodo.18614663) | [`APF-Paper-13-The-Minimal-Admissibility-Core`](https://github.com/Ethan-Brooke/APF-Paper-13-The-Minimal-Admissibility-Core) | public |
| — | Canonical codebase (v6.9) | [10.5281/zenodo.18604548](https://doi.org/10.5281/zenodo.18604548) | [`APF-Codebase`](https://github.com/Ethan-Brooke/APF-Codebase) | pending |

The canonical computational engine — the full bank of 342 theorems across 19 modules — is the **APF Codebase** ([Zenodo](https://doi.org/10.5281/zenodo.18604548)). Every per-paper repo is a faithful subset of that engine.

---

## License

MIT. See [LICENSE](LICENSE).

---

*Generated by the APF `create-repo` skill on 2026-04-18. Codebase snapshot: v6.9 (frozen 2026-04-18; 355 verify_all checks, 342 bank-registered theorems, 48 quantitative predictions).*
