# Science Roadmap: Grammar-to-Coherence Full Validation

**Start Date:** July 2026  
**Phase 1 Complete:** October 2026  
**All Phases Complete:** April 2027  
**First Publication:** January 2027 (expected)

---

## PHASE 1: Theory Refinement + Grants (July—September 2026)

### Week 1–2: Theory Update
- [ ] Revise FROM_GRAMMAR_TO_COHERENCE.md with spectral gap formula
  - Replace λ₁-only prediction with (λ₁ − λ₂) as primary metric
  - Update all equations for spectral dominance
  - Add noise model (20–30% variance) to theory section
  - Recompute theoretical predictions for all 4 experiments

- [ ] Create revised theory figure
  - Visualization: Eigenvalue spectrum → Coherence scale
  - Include error bands (confidence interval from analysis)
  
- [ ] Resubmit to Zenodo with v2 (updated DOI)

### Week 3–4: NSF Grant
- [ ] Finalize NSF grant outline (✓ draft done)
- [ ] Write Intellectual Merit section (2 pages)
  - Significance of bridging syntax and neuroscience
  - Specific aims (3 aims × 1 page)
  - Research approach (detailed methods, 2 pages)
  
- [ ] Write Broader Impacts section (1 page)
  - Training (graduate + undergraduate)
  - Public outreach (op-ed, videos)
  - Open-source toolkit release

- [ ] Budget justification (1 page)
  - Personnel, equipment, supplies
  - Detailed cost breakdown

- [ ] Submit to NSF (target: Early October deadline)

### Week 5–6: IRB Protocol
- [ ] Finalize IRB protocol (✓ draft done, 20 pages)
- [ ] Convert to institution's template
- [ ] Obtain institutional signatures
- [ ] Prepare Informed Consent Form (plain language, 1 page)
- [ ] Submit to IRB for review
  - Expect: 2–4 weeks for approval

### Week 7–8: Lab Prep
- [ ] Confirm EEG equipment access (64-channel cap)
- [ ] Test electrode impedance protocol
- [ ] Practice with 2–3 pilot subjects
- [ ] Verify spaCy parsing on all 240 stimuli
- [ ] Finalize stimulus presentation code (MATLAB/Psychtoolbox)

**Deliverables by Sept 30:**
- ✅ Revised theory paper (v2)
- ✅ NSF grant submitted
- ✅ IRB approval received (or pending minor revisions)
- ✅ Lab fully operational

---

## PHASE 2: Experiment 1 + Experiment 3 (October 2026—December 2026)

### Exp 1: EEG Spectral Matching (Parallel with Exp 3)

**Timeline:** 3 months  
**Target N:** 50 subjects (40–60)  
**Weekly pace:** 10–15 subjects/month

#### October (15 subjects)
- [ ] IRB approval finalized
- [ ] Recruitment posters posted (university, community)
- [ ] First 5 subjects screened
- [ ] First 3 subjects run (pilot week)
  - Confirm task difficulty (too hard/easy?)
  - Confirm EEG quality
  - Troubleshoot technical issues

#### November (15 subjects)
- [ ] Run 10–15 subjects (full speed)
- [ ] Weekly data review (check artifact levels, compliance)
- [ ] Preliminary quality check (10 subjects analyzed)

#### December (20 subjects)
- [ ] Finish remaining 10–15 subjects
- [ ] Complete all 50 subjects by Dec 15
- [ ] Begin data preprocessing (ICA, artifact rejection)

**Analysis (parallel):**
- [ ] Preprocess first batch (subjects 1–10)
- [ ] Compute grammar eigenvalues (all 240 sentences)
- [ ] Extract EEG spectral peaks
- [ ] Preliminary correlation (should see r ≈ 0.45–0.55)
- [ ] Identify outliers for manual review

**Deliverables by Dec 31:**
- ✅ Complete EEG dataset (50 subjects, 240 sentences = 12,000 epochs)
- ✅ Preprocessed EEG (all channels, < 5 kΩ impedance)
- ✅ Grammar eigenvalues computed (all 240 sentences)

### Exp 3: Ambiguity & Degeneracy (Parallel with Exp 1)

**Timeline:** 2 months  
**Stimuli:** 60 ambiguous + 60 unambiguous sentences

#### October
- [ ] Collect/curate ambiguous sentences
  - Garden path: "The horse raced past the barn fell." (VP attachment ambiguity)
  - PP attachment: "I saw the man with the telescope."
  - Other types: 20–30 examples per type
  
- [ ] Hand-annotate multiple parses for each ambiguous sentence
  - Hire 2 graduate linguistics students ($2K)
  - 2–3 native speakers per sentence
  - Consensus parse per interpretation

#### November
- [ ] Compute parse trees for each interpretation
- [ ] Build adjacency matrices (A for each parse)
- [ ] Eigenvalue decomposition (all parses)
- [ ] Measure degeneracy: σ(λ₁, λ₂, λ₃) for ambiguous vs. unambiguous

#### December (analysis)
- [ ] T-test: ambiguous > unambiguous degeneracy
  - Expected: p < 0.01, Cohen's d > 0.8
- [ ] Generate visualization (eigenvalue distributions side-by-side)

**Deliverables by Dec 31:**
- ✅ 60 ambiguous sentences with 3+ parses each
- ✅ Eigenvalue spectra for all parses
- ✅ Degeneracy comparison (statistical result ready)

---

## PHASE 3: Results Analysis + Manuscript (January—February 2027)

### Week 1–2: Data QA & Statistics
- [ ] Verify EEG quality metrics
  - Impedance distribution
  - Artifact rates per subject
  - Outlier detection (high/low correlators)

- [ ] Final statistical analysis
  - Group correlation (primary)
  - Individual correlations (n = 50)
  - Permutation test (10,000 shuffles)
  - Mediation analysis (if age/literacy matters)

### Week 3–4: Manuscript Writing
- [ ] Results section (2 pages)
  - Main finding: r = ?, p = ?, n = 50
  - Figure 1: Scatter plot (λ₁ vs frequency)
  - Figure 2: Per-subject correlations
  - Figure 3: Ambiguity degeneracy (t-test result)

- [ ] Methods section (2 pages)
  - Subjects, stimuli, procedure
  - EEG acquisition & preprocessing
  - Grammar analysis pipeline

- [ ] Discussion section (3 pages)
  - Interpretation: Why r ≈ 0.5–0.6?
  - Theoretical implications
  - Limitations + future directions

### Week 5–6: Revisions & Submission
- [ ] Internal review (co-authors, advisors)
- [ ] Incorporate feedback
- [ ] Submit to journal (target: Nature Neuroscience or Cognitive Science)
- [ ] Prepare supplementary materials (code, data documentation)

**Deliverables by Feb 28:**
- ✅ Manuscript submitted (goal: Nature Neuroscience)
- ✅ All data processed + archived

---

## PHASE 4: Experiments 2 + 4 (March—September 2027)

### Exp 2: Reaction Time Power Law (2 months)

**Timeline:** March–April 2027

#### March
- [ ] Design Prolific study (online comprehension task)
- [ ] Create stimulus list (120 sentences, varying complexity)
- [ ] Program behavioral task (React/JavaScript)
  - Present sentence → wait for button press
  - Record latency (RT)
  
- [ ] Recruitment: 100–150 subjects
  - US-based, native English speakers
  - Pay: $5–7 per participant (via Prolific)

#### April
- [ ] Data collection (1 week turnaround)
- [ ] Analysis:
  - Compute spectral gap for each sentence
  - Fit power law: RT = k / (gap^c)
  - Extract c coefficient
  - Expect: c ≈ 1.0, R² > 0.65

**Deliverables by April 30:**
- ✅ RT data (100–150 subjects × 120 sentences)
- ✅ Power law fit + parameter estimates

### Exp 4: Dialogue Entanglement (6 months)

**Timeline:** May–September 2027

This is the most complex experiment (requires dual EEG, conversations).

#### May–June
- [ ] Recruit 30–40 dyads (60–80 people)
- [ ] Schedule conversation sessions
- [ ] Prepare conversation scripts
  - Pairs: Explainer (reads text) + Listener (comprehends)
  - Duration: 6 minutes per pair
  - Topic: Varied (science, history, current events)

#### July–August
- [ ] Run sessions (2 per week, dual EEG caps)
- [ ] Data collection (60–80 people, 6 min each = ~480 min total)

#### September
- [ ] Analysis:
  - Compute λ_E (explainer coherence) + λ_L (listener coherence)
  - Coupling strength: λ_E × λ_L
  - Early vs. late phase comparison
  - Statistical test: coupling > independence?

**Deliverables by Sept 30:**
- ✅ Dialogue EEG dataset
- ✅ Coupling analysis results

---

## PUBLICATION & DISSEMINATION

### Timeline

**January 2027:** Exp 1+3 manuscript submitted (Nature Neuroscience)  
**March 2027:** First revision round (expected)  
**May 2027:** Accepted/published (optimistic) or Cognitive Science (backup)  
**June 2027:** Exp 2+4 manuscript submitted  
**August 2027:** Preprint on bioRxiv (if journal slow)  
**October 2027:** Data release on OpenNeuro  

### High-Impact Targets

1. **Nature Neuroscience** (IF 16.5)
   - Novel bridge between syntax and neural dynamics
   - Well-powered design (n=50), low risk of false positive

2. **Cognitive Science** (IF 4.2, backup)
   - Interdisciplinary fit
   - Faster review cycle

3. **Specialty journals**
   - JMLR (machine learning angle)
   - Cognitive Psychology (reaction time study)
   - Consciousness and Cognition (dialogue/coupling)

### Press/Outreach

- Op-ed: "Why Grammar Matters" (New York Times/Chronicle)
- Podcast interview: 2 podcasts (neuroscience + language focus)
- GitHub release: Python toolkit (github.com/phronesis-science/grammar-eigenvalue)
- YouTube explainer: 3–5 min video on grammar-brain connection (target: 50K views)

---

## BUDGET SUMMARY

### Phase 1 (July–September 2026)
- Lab prep: $5K
- IRB/ethics: $2K
- Grant writing consultation: $1K
- **Subtotal: $8K**

### Phase 2 (Oct–Dec 2026)
- EEG subject recruitment ($150 × 50): $7.5K
- EEG equipment/technician: $10K
- Linguistic annotation (Exp 3): $2K
- **Subtotal: $19.5K**

### Phase 3 (Jan–Feb 2027)
- Data analysis: $3K
- Manuscript preparation: $2K
- **Subtotal: $5K**

### Phase 4 (Mar–Sep 2027)
- Exp 2 (online study): $8K
- Exp 4 (dialogue EEG): $30K
- **Subtotal: $38K**

### Total: $70.5K (within NSF grant + follow-up funding)

---

## SUCCESS CRITERIA

| Milestone | Target | Timeline |
|---|---|---|
| **Theory revised** | Spectral gap formula | Week 2 (Aug 2026) |
| **NSF grant submitted** | $150K awarded | Oct 2026 |
| **IRB approval** | Full approval | Nov 2026 |
| **Exp 1 complete** | 50 subjects, r > 0.45 | Dec 2026 |
| **Exp 3 complete** | p < 0.01 ambiguity effect | Dec 2026 |
| **Manuscript 1 submitted** | Nature Neuroscience | Feb 2027 |
| **Exp 2 complete** | c ≈ 1.0, R² > 0.60 | Apr 2027 |
| **Exp 4 complete** | Coupling effect | Sep 2027 |
| **Data on OpenNeuro** | De-identified, BIDS | Oct 2027 |
| **Toolkit on GitHub** | MIT license, docs | Nov 2027 |

---

## TEAM & ROLES

**Principal Investigator:** Theory, analysis, writing  
**EEG Technician:** Data collection, preprocessing  
**Graduate students (2):** Data analysis, manuscript prep  
**Undergraduate mentees (4):** Data labeling, literature review  
**Collaborators:** Provide lab/subject access (acknowledgment only)

---

## Risk Mitigation

| Risk | Mitigation |
|---|---|
| EEG signal too noisy | Use high-impedance cap; ICA for artifacts |
| Correlation weaker than expected (r < 0.4) | Use alternative metrics; reframe as "weak signal" paper |
| IRB delays | Have backup institution ready |
| NSF rejects | Apply to NIH (later deadline) + foundation grants |
| Subject recruitment slow | Use community+ university; increase compensation if needed |
| Key person leaves | Cross-train 2 team members on each critical task |

---

## Next Steps (This Week)

1. ✅ Theory refinement analysis (done)
2. ✅ NSF grant draft (done)
3. ✅ IRB protocol draft (done)
4. → Finalize theory paper (revise FROM_GRAMMAR_TO_COHERENCE.md)
5. → Convert IRB protocol to institution template
6. → Identify collaborating labs (need EEG access)
7. → Meet with department (secure lab access, subject pool)

---

**Go/No-Go Decision:** August 1, 2026

By August 1, we need:
- ✓ Theory finalized
- ✓ Funding identified (NSF grant in review)
- ✓ IRB submitted
- ✓ Lab access confirmed

If all green, full speed ahead. If any red, pivot to theory publication + Phase 2 scaled back.
