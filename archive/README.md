# archive/ — Historical Paper 2 artifacts

This folder preserves the first public release of Paper 2 alongside the current
canonical version. Top-level files are what reviewers and AI agents should use;
everything here is preserved for continuity.

## What's here

- **`Paper_2_STRUCTURE_v7.tex/.pdf`** — the v7 manuscript (older internal
  versioning). The current canonical manuscript is
  `../Paper_2_Structure_of_Admissible_Physics_v5.3-PLEC.{tex,pdf}` which uses
  the post-PLEC restructuring. (The v5.3-PLEC numbering reset when PLEC was
  introduced; v7 → v5.3-PLEC is a continuation of the same work, not a rollback.)

- **`APF_Paper2_Colab.ipynb`** — original second Colab notebook (educational
  variant focused on the 61-channels visualization workflow).

- **`APF_Reviewer_Walkthrough_v1_handcrafted.ipynb`** — original hand-crafted
  reviewer walkthrough. The current canonical notebook is
  `../APF_Reviewer_Walkthrough.ipynb` (38 cells, tier-grouped, `show()` helper).

- **`REVIEWERS_GUIDE_v1_handcrafted.md`** — hand-curated reviewers' guide.
  Current canonical guide is `../REVIEWERS_GUIDE.md`.

- **`zenodo_paper2_v1.json`** — v1 Zenodo metadata (paper-suffixed name).
  Current canonical is `../zenodo.json`.

- **`apf_v1_handcrafted/`** — original hand-curated `apf/` package layout
  (root-level `core.py`, `gauge.py`, `bank.py`, `apf_utils.py`). The current
  layout vendors a paper-specific subset into `../apf/` and is auto-regenerated
  on each rebuild.

## What's at the repo root and why

- **`storyboard.html`** + **`apf_storyboard.jsx`** — interactive React-based
  visual walkthrough (preserved from v1, promoted from `docs/` to root for
  discoverability).
- **`61_channels_v5.html`** — the 61-channels visualization specific to Paper 2.
- **`L_Cauchy_uniqueness.py`** + **`fermion_scan_standalone.py`** — standalone
  computational experiments referenced by the paper.
- **`CITATION.cff`** — GitHub's standard citation file (renders the "Cite this
  repository" widget on the GitHub repo page).
- **`repo_map.json`**, **`theorems.json`**, **`derivation_graph.json`**,
  **`interactive_dag.html`** — machine-readable artifacts promoted from
  `ai_context/` and `docs/` to root for visibility.

See `../START_HERE.md` for the AI operational checklist.
