# Claims Ledger — Paper 2 (main v7.1 · Supplement I v5.2 · Supplement II v1.0)

Row-by-row attack surface. Every load-bearing claim maps to its proof
location, its code check in THIS repo, its status, and the failure mode a
skeptical reviewer would attack. "Supp I" = The Classification Core (v5.2);
"Supp II" = The Foundational Gauge Program (v1.0).

| # | Claim | Status | Proof location | Code check (this repo) | Failure mode |
|---|---|---|---|---|---|
| 1 | Theorem R: carrier requirements R1–R2 derived; R3 under the admissibility-completeness reading | R1–R2 [P]; R3 reading-typed | Supp II §3 | `check_Theorem_R` | exhibit an admissible carrier violating R1/R2; adjudicate the R3 reading |
| 2 | Nonabelian carrier ranking: SU(3)×SU(2) unique at minimum capacity cost; R3 requires ≥1 abelian grading | [P] on the tested classification (17 representatives; families closed by monotonicity) | Supp I §gauge consolidation (thm split, clause i) | `check_L_gauge_template_uniqueness` | a compact structure outside the tested set passing R1–R2 at lower cost |
| 3 | One-U(1) closure: exactly one U(1) closes the template — proved A-POSTERIORI for the selected matter content, not forward | [P] a-posteriori; NOT a forward derivation | Supp I §one-U(1) closure (clause ii of the split theorem) | `check_L_gauge_template_uniqueness` (pointer); closure theorems in Supp I | a second admissible abelian factor on the selected content |
| 4 | C(G) = dim(G)·ε — under operational encoding + disjoint-anchor realizability (premises named in the statement) | [P | named premises] | Supp I §capacity; canonical core.py | `check_L_cost_gauge` | break either named premise; exhibit sub-dim(G) encoding |
| 5 | The conditional classification theorem: relative to the declared representation list, caps, and filter inputs (C1–C10), the 1,680-template scan has the unique minimum-capacity survivor = SM at 45 Weyl DOF | conditional [P]; caps-completeness OPEN by declaration | Supp I §fermion scan | `check_T_field`, `check_L_F6_not_from_EC`, the canonical executable `fermion_scan_standalone.py` | an admissible sub-45-DOF template outside the declared caps; any waterfall count failing reproduction |
| 6 | Canonical F6 = full-system non-degeneracy (10/5); the F6 non-degeneracy assumption (nonzero quark-doublet hypercharge, Y_Q ≠ 0 — the name "electromagnetic completeness" is retired) is an INDEPENDENT phenomenological assumption doing the work of removing the 42-DOF near-miss | declared input, point-of-use | Supp I §seven filters (F6) | `check_L_F6_not_from_EC`; `release_audit/near_misses.csv` | reject the assumption → the stripped generation survives below the SM |
| 7 | P4: two-colored-doublet class dominance — class minimum 54 > 45 (conjugate-pair witness; mini-enumeration) | [P]; TIGHTNESS WITHDRAWN | Supp I §exclusion proofs (Prop P4) | `check_T_field` (54-witness battery); RT4 of the canonical executable | a two-doublet template below 54 passing F1–F5 |
| 8 | EC-label-injectivity and F6 are logically independent (all four quadrants inhabited) | [P] computed | Supp I §F6 declaration; Supp II | `check_L_F6_not_from_EC` | any quadrant witness failing exact re-verification |
| 9 | EC inventory reading (R-EC-inv): kinematic type-inventory completeness, A1-motivated NOT A1-derived | [P_structural_reading] | Supp II | `check_L_EC_inventory_reading` | promoting the reading to a derivation (the in-check counter-construction kills it) |
| 10 | L_count: C_total = 61 = 45 + 4 + 12 | arithmetic on forced inputs | Supp I §capacity count | `check_L_count` | upstream count shifts |
| 11 | I2 at the L_count seam: K = 61 = denominator of the cosmological fractions | seam statement; full bridge is Paper 8 Thm 1.1 | Supp I §I2 exit note; Papers 8/41 | `check_I2_gauge_cosmological` (engine, not bundled) | same as Paper 8 I2 failure mode |
| 12 | Non-closure: no single representation valid across all regimes | [P] | Supp II §non-closure; main §2 | `check_L_nc`, `check_T3` | exhibit single-rep closure |

## Attack surface priority

Claims 5, 6, 7 (the classification core and its declared inputs), then 2–3
(the ranking/closure split), then 1 (Theorem R's R3 reading). The
dual-supplement split exists precisely so the conditional theorem (Supp I)
and the foundational program (Supp II) are attacked at their own registers.

---

*20 bank-registered checks verify Paper 2 in this repo, vendored at
canonical codebase v24.3.423 (commit 5bc6193, bank 3912).*
