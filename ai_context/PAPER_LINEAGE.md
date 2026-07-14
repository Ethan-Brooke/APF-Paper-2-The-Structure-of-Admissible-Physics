# PAPER_LINEAGE.md — Version History for Paper 2

This file tracks the version history of Paper 2 (The Structure of Admissible
Physics) and the relationship between the versions in this release, the
Zenodo deposits, and the canonical codebase.

---

## Current release

- **Main paper:** v7.2 — `Paper_2_Structure_of_Admissible_Physics_v7.2.tex` + `.pdf` (60 pp)
- **Technical Supplement I — The Classification Core:** v5.3 —
  `Paper_2_Structure_of_Admissible_Physics_Supplement_v5.3.tex` + `.pdf` (62 pp)
- **Technical Supplement II — The Foundational Gauge Program:** v1.0 —
  `Paper_2_Foundational_Gauge_Program_Supplement_v1.0.tex` + `.pdf`
- **Release date:** 2026-07-14
- **Codebase version at build:** v24.3.423 (numerical kernel 5bc6193;
  bank 3912, native verify_all --bank-audit 3912/3912 gap 0;
  count-neutral corrigenda trail in the release manifest)
- **Canonical scan executable:** `fermion_scan_standalone.py` v4.2
  (RT1–RT6; VERSION_LOCK split into numerical-kernel commit + corrigenda
  trail; emits `release_audit/`)

## Zenodo records

- **Main paper concept DOI:** 10.5281/zenodo.18439274
- **Supplement I concept DOI:** 10.5281/zenodo.19714959
- **Companion-repo concept DOI:** 10.5281/zenodo.18604839
- Concept DOIs resolve to the latest version; version DOIs pin specific
  deposits. The v2 standalone scan is archived at 10.5281/zenodo.19154197.

## Version history (newest first)

- **v7.2 main + Supp I v5.3** (2026-07-15): the review 5.2.01 pass (MINOR
  REVISION — acceptance named). P3 gains the color-dimension case split
  (dim 6/8 doublets bust the SU(2) budget outright); the one-U(1)
  uniqueness claim moved to the physical quotient T_phys = T_rel/ker(ρ_M)
  (kernel countermodel owned); the B−L edge case rewritten to the licensed
  EC/CM model-selection form (Y and B−L independent, all six anomaly
  conditions vanish — computed); lem:min_abelian restated conditionally;
  C5 anomaly count corrected (five perturbative + Witten); "chiral
  template" → "Weyl-fermion template"; twistor and 11/3 glosses fixed
  (Hughes 1980 / Nielsen 1981 sourced); VERSION_LOCK split into
  numerical-kernel commit + corrigenda trail; engine P3 battery case-split.

- **v7.1 main + Supp I v5.2** (2026-07-14): the review 5.1.01 pass (second
  consecutive non-reject; the reviewer independently reproduced the
  canonical waterfall). Feasibility/minimality corrected (five feasible
  classes, unique minimum); "electromagnetic completeness" retired as F6's
  name (the predicate is nonzero quark-doublet hypercharge); chirality
  decoupled from F6; the one-U(1) closure conditionalized on I-typing's
  relative-torus matter action (H3); generation universality promoted to a
  named premise with the L_mu−L_tau direction owned exactly; the
  Lie-carrier and N_c claims scoped to their tested lists; P3 reproved a
  priori (F2+F5 joint budget); script descriptions synchronized (v4.1,
  RT1–RT6); engine metadata re-scoped (Declared-Ansatz Classification).

- **v7.0 main + Supp I v5.1 + Supp II v1.0** (2026-07-14): the v5.1
  acceptance pass after review 5.0.01 (MAJOR REVISION — first non-reject of
  the cycle). Completeness proposition restated at its licensed relative
  form; P4 tightness withdrawn (class dominance, minimum 54); F3 renamed to
  its honest content-predicate role; beta primer rewritten on the Weyl form;
  Theorem 4.7 split into carrier ranking + a-posteriori one-U(1) closure;
  C(G) = dim G premise pair named; "all 17" phrasing scoped; hypercharge
  claims at the licensed ratios+convention form; kinetic-mixing subsection
  removed (false lemma); neutrino/cosmology residue exited to the Papers 8/41
  landing fragment; computational notes corrected (canonical 10/5 waterfall
  attributed to check_L_F6_not_from_EC).
- **Supp I v5.0 + Supp II v1.0 + main v6.9** (2026-07-14): the
  dual-supplement split — the classification core (conditional theorem,
  C1–C10 ledger, canonical F6 = full-system 10/5) separated from the
  foundational gauge program (chain at banked grades, open-lane register).
- **v4.x** (2026-07-13): the core split + repairs arc across reviews
  4.0.01 and 4.1.01; the EC lane banked at v24.3.423
  (check_L_F6_not_from_EC, check_L_EC_inventory_reading).
- **v5.3-PLEC** (2026-04-19): the pre-review-cycle release (single
  supplement v2; codebase v6.9-era). Preserved in `archive/`.

## What supersedes what

**Main v7.2 + Supp I v5.3 + Supp II v1.0 supersede all earlier versions.**
For strict reproducibility of earlier work, cite the version DOI of the
specific deposit used.

## Relationship to the canonical codebase

All `\coderef{check_X}{module.py}` anchors in the current papers are valid
against canonical codebase v24.3.423 (numerical kernel commit 5bc6193;
count-neutral corrigenda thereafter). The bundled `apf/` package is
vendored at the corrigenda-trail head; `python verify_all.py` runs the
20-check subset, and `python fermion_scan_standalone.py --emit-audit`
regenerates the audit bundle byte-identically (see
`release_audit/certificate.sha256`).

## Policy on retractions

If a [P] theorem in this paper is demoted or retracted in a future framework
version, the retraction is logged in the canonical planning surface, the
codebase changelog, and the successor version's PAPER_LINEAGE.md. Retractions
are not silent: the specific theorem, the failing condition, and the
downstream papers affected are named. (Worked examples in this very cycle:
P4's tightness claim and the kinetic-mixing lemma, both withdrawn at v5.1
with the counterexamples on record.)
