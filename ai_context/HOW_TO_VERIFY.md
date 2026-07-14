# HOW_TO_VERIFY.md — Verification Recipes

This file is the quick-reference for verifying any claim in this paper. Tested recipes, ordered from friction-free to detailed.

---

## Zero-install — Colab

Click the Colab badge at the top of `README.md` or open directly: [`APF_Reviewer_Walkthrough.ipynb`](../APF_Reviewer_Walkthrough.ipynb) on Colab. Every theorem has its own cell with the check invocation, expected result, and structural commentary. `Runtime → Run all` verifies everything.

This is the recommended entry for any reviewer, physicist, or AI assistant that doesn't want to install Python.

## Zero-install — browser

Open the interactive DAG at `https://ethan-brooke.github.io/APF-Paper-2-The-Structure-of-Admissible-Physics/` (requires GitHub Pages enabled on this repo's `/docs` folder). Hover any node for its claim, epistemic tag, and shortest derivation chain. Click **Run Checks** to watch all theorems verify in topological order.

## Local — one command

From a terminal at the repo root:

```bash
python verify_all.py
```

Expected output: one line per check, then `20 passed, 0 failed, 20 total`. Elapsed time is under a second; no install is needed (standard library only). `python verify_all.py --paper2-core` runs just the 6 classification-core checks; `python run_checks.py` is a kept alias.

## Local — regenerate the scan audit bundle

```bash
python fermion_scan_standalone.py --emit-audit
```

This is the canonical executable: it reruns the full 1,680-template scan in exact arithmetic (canonical F6 = full-system non-degeneracy, 10/5; robustness variants 8/4 and 4/2), verifies the five exclusion proofs (P4 at class dominance, minimum 54), runs red-team challenges RT1–RT6 (RT6 = filter-order invariance across all 5,040 orderings), and rewrites `release_audit/` byte-identically — compare `release_audit/certificate.sha256` before and after.

## Local — inspect a specific check

Pick the check name from `ai_context/THEOREMS.md` (use `grep` to filter by module, or by epistemic tag, or by keyword). Then:

```bash
python -c "from apf import core; r = core.check_L_nc(); print(r)"
```

The returned dict has fields:

- `name` — the check's display name
- `tier` — tier in the project (1 = foundational, up to 5 = applied)
- `epistemic` — the tag ([P], [P]+[I], [P_structural], [Pred])
- `summary` — human prose
- `key_result` — one-line bottom line
- `dependencies` — list of upstream theorems / axioms
- `cross_refs` — related theorems
- `artifacts` — computed values, witnesses, parameters

## Local — read the proof

Open `apf/core.py` and find the function by name (editor jump-to-definition works). Each `check_*` function is structured:

1. **Docstring.** States the claim, the mechanism, the proof steps, the status tag, and the dependencies. Read this first.
2. **Witness setup.** Concrete objects (matrices, distinctions, fractions) on which the witness operates.
3. **Assertions via `check(...)`.** Each `check(condition, message)` is a required invariant; if it fails, `CheckFailure` is raised.
4. **Return via `_result(...)`.** Packages name, tier, epistemic, summary, key_result, dependencies, cross_refs, artifacts.

A check that passes means the witness survived every invariant. The witness is typically a minimal case chosen to be rigorous, not maximally general — the derivation argument (in the docstring, and in the paper / supplement) makes the generality claim.

## Cross-check against the manuscript

Every `\coderef{check_X}{module.py}` in the paper source (`Paper_2_Structure_of_Admissible_Physics_v7.1.tex`) points to a specific check function. To verify the paper's claim at a particular point:

```bash
# find all coderefs in the paper
grep -o '\\coderef{[^}]*}{[^}]*}' Paper_2_Structure_of_Admissible_Physics_v7.1.tex

# for each coderef, run it:
python -c "from apf import core; print(core.check_T7B().get('key_result'))"
```

(Replace `core` with the actual module name from the second brace of the coderef.)

## Cross-check against the Technical Supplement (if present)

The supplement contains the canonical proofs. Each theorem in the supplement has a `\coderef` pointing to its executable witness. The supplement is the source of truth for formal content; the main paper compresses proofs into sketches with "See Technical Supplement, Theorem X."

## Cross-check against the DAG

The interactive DAG (`docs/index.html`, or browse it directly as a web page) shows the full dependency graph. Every edge corresponds to a `dependencies` entry in a `_result(...)` call. To verify a claim: find the node, inspect its dependencies, verify each recursively.

For scriptable access, use `ai_context/derivation_graph.json`.

## Verify a specific paper claim step by step

1. Identify the claim in the paper (a theorem, equation, or statement).
2. Find the `\coderef{}{}` anchor. If absent, this is a potential coderef drift — flag it.
3. Run the check: `python -c "from apf import <module>; print(<module>.<check_name>())"`.
4. Read the check's docstring to confirm the witness matches the paper's claim.
5. Walk dependencies (from the returned `dependencies` list or `derivation_graph.json`) until you hit an axiom or an already-verified claim.

## Verify against external data (predictions)

For checks tagged [Pred] or [P] with a numerical prediction:

1. Run the check and note the `artifacts` fields (predicted values).
2. Compare against the observational source cited in the docstring.
3. Compute the tension: $(observed - predicted)/\sigma$.
4. A tension exceeding the paper's claimed confidence level is a falsification candidate. Don't patch it — flag it.

Example (from this release's context): APF's $H_0 = 67.76$ km/s/Mpc vs. H0DN 2026 $73.50 \pm 0.81$ gives $7.09\sigma$ tension. This is a known falsification candidate (see `ai_context/OPEN_PROBLEMS.md` for the full treatment and the five escape-route verdicts).

## What to do if a check fails

Don't patch. Don't skip. Report:

1. The check name.
2. The `CheckFailure` message (or the exception traceback).
3. The function's docstring claim.
4. Whether the paper prose makes a claim that the check's failure would contradict.

A failing check is either a bug in the witness, a bug in the paper prose, a bug in a dependency, or a genuine falsification of a framework claim. The discipline is to identify which — not to silence the check.

---

*Generated by `create-repo`. To edit the recipe set, modify `templates/HOW_TO_VERIFY.md.template` in the skill folder.*
