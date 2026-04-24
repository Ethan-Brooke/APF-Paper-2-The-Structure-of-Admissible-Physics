# Claims Ledger — Paper 2

| # | Claim | Status | Proof location | Code check | Failure mode |
|---|---|---|---|---|---|
| 1 | Theorem R: no single-rep closure | nontrivial (load-bearing) | Supp §2 | `check_Theorem_R` | exhibit single-rep admissibility |
| 2 | $T_M$ (interface monogamy) | nontrivial | Supp §3 | `check_T_M` | counterexample with non-monogamous interface |
| 3 | Gauge template uniqueness (imported) | imported | Paper 1 Supp §5 | `check_L_gauge_template_uniqueness` | same as Paper 1 claim 6 |
| 4 | $T_{\rm gauge}$: $N_c = 3$ by optimisation | structural | Supp §4 | `check_T_gauge` | alternative $N_c$ with equal cost |
| 5 | $L_{\rm count}$: $C_{\rm total} = 61$ | arithmetic | Supp §5 | `check_L_count` | upstream count shifts |
| 6 | I2 at $L_{\rm count}$ seam: $K = 61$ = denom of $\pi_C$ | nontrivial (deferred to Paper 8 Theorem 1.1) | Supp v2.1 §I2 | `check_T_ACC_unification` (Paper 8) | same as Paper 8 I2 failure mode |
| 7 | 45 fermions = 3 × 15 | arithmetic | Supp §6 | `check_L_count` | fermion irrep content wrong |
| 8 | 12 gauge slots = 8 + 3 + 1 | arithmetic (on forced gauge group) | Supp §6 | `check_L_count` | gauge group wrong upstream |

## Attack surface priority

Claims 1, 2, 4, 6. Theorem R is the spine of Paper 2.

---

*14 bank-registered checks verify Paper 2 in this repo.*
