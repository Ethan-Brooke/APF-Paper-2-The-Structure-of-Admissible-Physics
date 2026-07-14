# PAPER_LINEAGE.md — Version History for Paper 2

This file tracks the version history of Paper 2 (The Structure of Admissible
Physics) and the relationship between the versions in this release, the
Zenodo deposits, and the canonical codebase.

---

## Current release

- **Main paper:** v7.0 — `Paper_2_Structure_of_Admissible_Physics_v7.0.tex` + `.pdf` (59 pp)
- **Technical Supplement I — The Classification Core:** v5.1 —
  `Paper_2_Structure_of_Admissible_Physics_Supplement_v5.1.tex` + `.pdf` (60 pp)
- **Technical Supplement II — The Foundational Gauge Program:** v1.0 —
  `Paper_2_Foundational_Gauge_Program_Supplement_v1.0.tex` + `.pdf`
- **Release date:** 2026-07-14
- **Codebase version at build:** v24.3.423 (commit 5bc6193; bank 3912,
  native verify_all --bank-audit 3912/3912 gap 0)
- **Canonical scan executable:** `fermion_scan_standalone.py` v4.0
  (emits `release_audit/`)

## Zenodo records

- **Main paper concept DOI:** 10.5281/zenodo.18439274
- **Supplement I concept DOI:** 10.5281/zenodo.19714959
- **Companion-repo concept DOI:** 10.5281/zenodo.18604839
- Concept DOIs resolve to the latest version; version DOIs pin specific
  deposits. The v2 standalone scan is archived at 10.5281/zenodo.19154197.

## Version history (newest first)

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

**Main v7.0 + Supp I v5.1 + Supp II v1.0 supersede all earlier versions.**
For strict reproducibility of earlier work, cite the version DOI of the
specific deposit used.

## Relationship to the canonical codebase

All `\coderef{check_X}{module.py}` anchors in the current papers are valid
against canonical codebase v24.3.423 (commit 5bc6193). The bundled `apf/`
package is vendored from that commit; `python verify_all.py` runs the
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
