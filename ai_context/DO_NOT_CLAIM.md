# Do Not Claim — Paper 2 (main v7.0 · Supp I v5.1 · Supp II v1.0)

Anti-hallucination guards, harvested from four external review rounds
(2026-07-13/14) and the internal audits. Consult before writing any summary,
email, or reviewer response.

1. **Do not claim the scan is universally complete.** The classification
   theorem is CONDITIONAL: complete relative to the declared representation
   list and multiplicity caps. That no admissible sub-45-DOF template exists
   outside the caps is an open proof obligation, stated as such.

2. **Do not claim P4 tightness.** The two-colored-doublet class minimum is
   54 (conjugate-pair witness), not 63 and not 81 — both earlier figures are
   withdrawn (the 63 witness is Witten-odd; the 81 was a same-chirality
   corner). The licensed statement is class DOMINANCE: 54 > 45.

3. **Do not claim F6 follows from EC, or from anomaly cancellation.**
   Electromagnetic completeness (Y_Q != 0) is an independent declared
   assumption of the scan, declared at its point of use. EC-injectivity and
   F6 are computed to be logically independent (check_L_F6_not_from_EC).

4. **Do not claim "EC is derived from A1 alone."** The EC derivation is dead
   as a derivation; what stands is the named reading R-EC-inv (A1-motivated,
   not A1-derived) plus the named input I-typing
   (check_L_EC_inventory_reading).

5. **Do not claim the full gauge group is forward-derived.** The forward
   statement is the nonabelian carrier ranking SU(3)xSU(2) plus R3's
   at-least-one abelian grading; that exactly one U(1) closes the template is
   proved a-posteriori for the selected matter content. "No additional
   abelian factor is needed" is not a forward claim.

6. **Do not cite the kinetic-mixing lemma.** The positive-definiteness
   inequality it rested on is false (counterexample verified); the subsection
   was removed at v5.1. Only the no-second-U(1) point survives, at the
   closure theorems.

7. **Do not claim F3 is a chirality test.** It is a doublet-singlet CONTENT
   predicate; the conjugate-pair two-doublet template passes it while being
   exactly vector-like. True chirality is charge-dependent and reported in
   the release audit layer (chirality_audit.csv), never consumed as a
   filter.

8. **Do not quote a single post-F6 survivor count without naming the
   predicate.** Canonical (full-system non-degeneracy): 10 pre-CPT / 5
   post-CPT. Spectator reduction: 8/4. Uniform dimension: 4/2. The winner
   (SM at 45) is invariant; intermediate counts are not.

9. **Do not claim "all 17 compact simple Lie algebras" as exhaustive
   coverage.** The tested set is the 4 classical families + 5 exceptionals
   via 17 representatives, with the families closed by the monotonicity
   arguments; state it that way.

10. **Do not claim the scan predicts neutrino physics.** The in-core
    supported sentence is: the minimum template in the declared scan contains
    no light sterile singlet. Majorana/0vbb language and the >5-sigma nu_R
    argument live in the Papers 8/41 bridge analysis, not here.

11. **Do not claim Paper 2 derives Omega_Lambda, fermion masses, or the Born
    rule.** I2 at the L_count seam carries the shared integer K = 61 only
    (Paper 8 Thm 1.1 has the bridge); masses are Paper 4's arc; quantum
    structure is Paper 5.

12. **Do not claim 61 is fitted.** It is arithmetic on forced counts:
    45 + 4 + 12.

13. **Do not present imported mathematics as framework results.** The Lie
    classification (Killing-Cartan), the Witten anomaly theorem, the anomaly
    equations, and N_gen = 3 enter as named imports/inputs where stated.

14. **Do not treat the bundled 20-check subset as the whole engine.** The
    canonical bank is 3,912 entries at v24.3.423; this repo carries the
    Paper 2 subset, version-locked at commit 5bc6193.
