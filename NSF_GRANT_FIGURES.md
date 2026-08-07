# NSF Grant Supporting Materials
## Figures, Biosketches, Current/Pending Support

---

## FIGURE 1: From Grammar to Coherence (Conceptual)

**Figure Title:** "Spectral Grammar Theory: From Parse Trees to Brain Oscillations"

**Description:** Multi-panel figure showing the complete pipeline

```
Panel A: Parse Tree Example
─────────────────────────────
Input: "The cat sat on the mat."

Dependency tree visualization:
        sat
       /  \
     cat  on
    /      |
  The      mat
           |
          The

Panel B: Adjacency Matrix
─────────────────────────
     [cat] [sat] [on] [mat] [The]
[cat]  0    1     0    0    1
[sat]  1    0     1    0    0
[on]   0    1     0    1    0
[mat]  0    0     1    0    1
[The]  1    0     0    1    0

(Symmetric, undirected)

Panel C: Eigenvalue Spectrum
────────────────────────────
Graph showing eigenvalues (λ) in descending order:

      λ₁ (dominant) ──┐  } Spectral Gap
      λ₂              ┘
      λ₃
      λ₄
      λ₅

Δλ = λ₁ - λ₂ = "Coherence Dominance"

Panel D: EEG Correlate
──────────────────────
Brain oscillation at dominant frequency matching λ₁:

Δλ = 1.8  →  Dominant frequency = 12 Hz (alpha)
Δλ = 0.4  →  Dominant frequency = 8 Hz (theta, diffuse)

Prediction: log(Δλ) correlates with observed frequency
```

**Figure Notes:**
- Create using GraphViz (tree), Python (matrix/spectrum), or Adobe Illustrator
- Color scheme: Tree (green), matrix (blue heatmap), spectrum (red → yellow decay), EEG (purple oscillation)
- Panel sizes: 2.5" × 2.5" each (6" × 6" overall)

---

## FIGURE 2: Four-Experiment Validation Strategy

**Figure Title:** "Four Experiments Testing Spectral Grammar Theory"

```
TOP ROW: Experimental Design

┌─────────────────────────────────────────────────────────────────────┐
│                    EXPERIMENT 1: EEG SPECTRAL MATCHING               │
├─────────────────────────────────────────────────────────────────────┤
│ INPUT: 240 sentences with computed spectral gaps (Δλ)               │
│                          ↓                                           │
│ SUBJECT: Wears 64-channel EEG cap, reads sentences silently          │
│                          ↓                                           │
│ OUTPUT: Correlate dominant EEG frequency with log(Δλ)                │
│ PREDICTION: r > 0.65, p < 0.01                                      │
│ TIMELINE: 3 months | SUBJECTS: 50 | COST: $7.5K                    │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                  EXPERIMENT 2: REACTION TIME POWER LAW               │
├─────────────────────────────────────────────────────────────────────┤
│ INPUT: 120 sentences with known spectral gaps (Δλ ∈ [0.2, 2.2])    │
│                          ↓                                           │
│ SUBJECT: Online (Prolific), reads & presses button when understood  │
│                          ↓                                           │
│ OUTPUT: Fit power law model: RT = k / (Δλ^c)                       │
│ PREDICTION: c ≈ 1.0, R² > 0.65                                     │
│ TIMELINE: 2 months | SUBJECTS: 100–150 | COST: $900               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│             EXPERIMENT 3: AMBIGUITY & EIGENVALUE DEGENERACY         │
├─────────────────────────────────────────────────────────────────────┤
│ INPUT: 60 ambiguous + 60 unambiguous sentences (hand-parsed)       │
│                          ↓                                           │
│ ANALYSIS: For each ambiguous sentence, compute Δλ for all parses   │
│ Degeneracy metric: σ(Δλ) across valid interpretations               │
│                          ↓                                           │
│ PREDICTION: Ambiguous > Unambiguous degeneracy, d > 0.8, p < 0.001 │
│ TIMELINE: 2 months | SUBJECTS: 0 (computational) | COST: $3K      │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│               EXPERIMENT 4: DIALOGUE ENTANGLEMENT                    │
├─────────────────────────────────────────────────────────────────────┤
│ INPUT: Two speakers (Explainer + Listener) discuss complex topic   │
│                          ↓                                           │
│ METHOD: Dual-cap EEG (64 ch each), transcript dialogue into 2-min   │
│ windows. Compute Δλ for each speaker per window.                    │
│                          ↓                                           │
│ OUTPUT: Track spectral gap convergence over time (early vs. late)   │
│ PREDICTION: Late coupling > early by >0.5, p < 0.001               │
│ TIMELINE: 6 months | SUBJECTS: 30–40 dyads (60–80 people)         │
│ COST: $30K                                                          │
└─────────────────────────────────────────────────────────────────────┘

BOTTOM ROW: Expected Results (if theory validated)

[Simple bar chart showing predicted vs. null results for each experiment]

Exp 1: r > 0.65 ✓
Exp 2: c ≈ 1.0 ✓
Exp 3: d > 0.8 ✓
Exp 4: coupling late > early ✓

All four predictions confirmed → Theory VALIDATED
At least 3/4 confirmed → Publishable, theory refined
Fewer than 3/4 → Alternative metrics needed
```

**Notes:**
- Create using PowerPoint, Illustrator, or Canva
- Use consistent color scheme (EEG = purple, grammar = green, behavior = blue, dialogue = orange)
- Include small icons for each experiment (brain, hourglass, question mark, two people)

---

## FIGURE 3: Timeline & Milestones

**Figure Title:** "Project Timeline: Grammar-to-Coherence Validation (24 Months)"

```
YEAR 1                          YEAR 2
┌─────────────────────┬─────────────────────────────┐
│  Months 1–6         │  Months 7–12  │  Months 13–24
├─────────────────────┼───────────────┼──────────────┤

IRB & Setup:
└─ Approval           └─ Exp 1 recruitment (ongoing)

Exp 1 (EEG):
├─ Months 1–3: Data collection (50 subjects)
├─ Months 3–6: Preprocessing & preliminary analysis
└─ Months 6–9: Final statistics, manuscript draft
  
Exp 2 (RT):
├─ Months 3–4: Design & setup (online study)
├─ Months 4–5: Data collection (100–150 subjects)
└─ Months 5–8: Analysis & power law fitting

Exp 3 (Ambiguity):
├─ Months 2–3: Linguistic annotation (120 sentences)
├─ Months 3–6: Computational analysis (degeneracy)
└─ Months 6–8: Subject ratings & correlations

Exp 4 (Dialogue):
├─ Months 5–8: Recruitment & setup
├─ Months 8–12: Data collection (30–40 dyads)
└─ Months 13–15: Analysis & visualization

Publications:
├─ Month 9: Manuscript 1 (Exp 1+3) submitted
├─ Month 12: MS1 revision/acceptance (if expedited)
├─ Month 15: Manuscript 2 (Exp 2+4) drafted
└─ Month 18+: Data release (OpenNeuro), GitHub toolkit

Major Milestones:
☐ M2: IRB approval received
☐ M4: Exp 1+3 in progress
☐ M6: First results (Exp 1 preliminary)
☐ M9: MS1 submitted
☐ M12: Exp 4 complete
☐ M15: All data analyzed
☐ M18: Toolkit released
☐ M24: Project conclusion
```

---

## BIOGRAPHICAL SKETCH — PI (NSF Format, 2 pages)

```
A. PROFESSIONAL PREPARATION

Undergraduate Degree:
  Institution: [Your University]
  Degree: B.S. or B.A.
  Major: [Psychology/Neuroscience/Computer Science]
  Year: [Year]

Graduate Degree (PhD):
  Institution: [Your University or other]
  Degree: PhD
  Field: [Psychology / Cognitive Neuroscience / Neuroscience]
  Year: [Year]

Postdoctoral Training (if applicable):
  Institution: [Institution]
  Field: EEG Analysis / Computational Linguistics
  Years: [Start–End]

B. APPOINTMENTS AND POSITIONS

[Current Year]–Present:
  Assistant Professor [or Postdoc/Research Scientist]
  Department of [Psychology/Neuroscience/Cognitive Science]
  [Your University]
  Duties: Teaching, research, mentoring

[Previous Year]–[Previous Year]:
  [Previous title and institution]

C. SELECTED PUBLICATIONS (5 most relevant to this proposal)

*PubMed ID or DOI required for all*

1. [You], [Collaborator]. ([Year]). "Title of paper on EEG/neuroscience topic."
   *Journal of Neuroscience*, Vol(Issue), pp-pp. PMID: [or DOI]

2. [You], [Collaborator]. ([Year]). "Title on computational linguistics/grammar."
   *Natural Language Processing Journal*, Vol(Issue), pp-pp. DOI: [or PMID]

3. [You], [Collaborator]. ([Year]). "Title on symbolic AI or reasoning."
   *Cognitive Science*, Vol(Issue), pp-pp. DOI: [or PMID]

[... continue with 2 more relevant papers ...]

D. RESEARCH AND PROFESSIONAL EXPERIENCE SUMMARY

Dr. [Your Name] has [3–7] years of research experience in cognitive neuroscience,
with specific expertise in:

- **EEG Signal Processing:** Led data collection and analysis for [N subjects]
  in studies of [relevant domain]. Proficient in MNE-Python, MATLAB, and spectral
  analysis (Welch's method, wavelet decomposition).

- **Computational Linguistics:** Developed [parsing algorithm / annotation framework]
  for [language]. Experienced with spaCy, NLTK, and dependency grammar formalism.

- **Human Subjects Research:** Completed CITI certification in human subjects protection
  and has prior experience designing, recruiting for, and conducting [prior EEG/behavioral study].

**Relevant Prior Projects:**

1. "The Neural Correlates of Grammatical Complexity" ([Year–Year])
   - Role: Lead researcher
   - Subjects: 30 participants, 64-channel EEG during sentence comprehension
   - Finding: EEG alpha band (8–12 Hz) correlates with grammatical complexity metrics
   - Publications: [2 papers, in prep or published]

2. "Automated Parse Tree Analysis in Large Corpora" ([Year–Year])
   - Role: Developer
   - Developed Python pipeline for dependency parsing 1M+ sentences
   - Applied to [domain], revealing [finding]
   - Publications: [1 paper]

3. [One more relevant project]

**Mentoring:** Have mentored [2–3] undergraduate research assistants and [1] Master's student.

E. RESEARCH INTERESTS

Dr. [Your Name]'s research lies at the intersection of cognitive neuroscience, 
linguistics, and AI. Primary interests:
- How brain dynamics reflect linguistic structure
- Formal bridges between symbolic logic and neural computation
- EEG as a tool for understanding coherence and mental clarity

F. COLLABORATORS AND CO-EDITORS (Last 48 months)

**Collaborators:**
- [Senior researcher at Your University] — EEG methodologist
- [Collaborator at other institution] — Computational linguist
- [Collaborator] — Statistician/methodologist

**Co-editors:** None in last 48 months.

---

CERTIFICATION

I hereby certify that the above information is true and complete.

Signature (electronic): ________________________

Name (typed): _________________________

Date: _________________________

Position/Title: _________________________
```

---

## CURRENT AND PENDING SUPPORT (1 page)

```
A. CURRENT SUPPORT

[If you have other grants, list them here. If none, write "None."]

Example:
─────────────────────────────────────────
Grant Title: "Neural Mechanisms of Language Learning"
Funding Agency: NSF (BCS-1234567)
Amount: $75,000
Duration: 7/2023–6/2025
Effort: 20%
Role: Co-Investigator
Status: Active

Overlap with proposed research: 
  None. Current grant focuses on learning; proposed grant focuses on 
  grammar-to-brain mapping in adults during comprehension.
─────────────────────────────────────────

B. PENDING SUPPORT

[List any grants you've submitted but haven't heard back on]

Example:
─────────────────────────────────────────
Grant Title: "Grammar-to-Coherence: Validating the Spectral Decomposition 
Theory of Reasoning"
Funding Agency: NSF (Cognitive Neuroscience Program)
Amount: $150,000
Duration: 24 months
Expected Start Date: 2027-01-15
Status: Under review (submitted Oct 2026)
Effort: 50% (if awarded)

Overlap with current proposal:
  N/A — This IS the current proposal.
─────────────────────────────────────────

C. SUMMARY OF OVERLAP

No significant overlap with current support. Proposed grant will fund 
new experiments (EEG validation, reaction time study, dialogue coupling) 
not covered by existing awards.
```

---

## CONFLICT OF INTEREST CERTIFICATION

```
NSF Conflict of Interest Form

Researcher Name: [Your Name]
Institution: [Your University]
Proposal Title: Grammar-to-Coherence: Validating the Spectral Decomposition 
                Theory of Reasoning

☐ I have a financial interest in the outcome of this research
  (Stock, consulting fees, patents, royalties, etc.)

☐ I have a personal or family relationship with a study participant

☐ I have developed the theory or method being tested, which might bias me

☐ Other conflict (describe): ___________________________________________

If you checked any boxes above, you must disclose the conflict to your 
institution's Conflict of Interest office BEFORE submitting this grant.

For most researchers in basic science: Check NONE of the above.

☑ I declare no conflicts of interest.

Signature: _________________________ Date: _________________
```

---

## LETTERS OF SUPPORT (Sample, if needed)

**Sample Letter from EEG Lab Director**

```
[Letterhead of EEG Lab / Your Institution]

[Date]

To: NSF Program Officer, Cognitive Neuroscience Program
From: [Director Name], [Title], [Institution]
Re: Letter of Support for NSF Grant Proposal

Dear Program Officer,

I write to express strong support for Dr. [Your Name]'s proposal titled 
"Grammar-to-Coherence: Validating the Spectral Decomposition Theory of Reasoning."

I am the Director of the [Name] EEG Laboratory at [Your University]. Dr. [Your Name]
has been a member of our lab for [X years], and I can attest to her/his 
exceptional skill in EEG data collection, preprocessing, and analysis.

SPECIFIC SUPPORT THIS PROJECT WILL RECEIVE:

1. Equipment access: Our lab has a 64-channel BioSemi EEG system available 
   for this project at no cost. The system is fully operational and calibrated.

2. Space: Dedicated testing room (15' × 12' with Faraday cage) will be available 
   Oct 2026–Dec 2026 and Jan–Jun 2027.

3. Personnel: Our lab technician, [Name], will assist with electrode preparation 
   and troubleshooting at no cost to the project.

4. Subject pool: Our institution's subject pool (Psychology dept) has ~300 active 
   participants who regularly sign up for neuroscience studies. We anticipate no 
   difficulty recruiting 50 subjects for Experiment 1.

CONFIDENCE IN SUCCESS:

Dr. [Your Name]'s preliminary data from 10 pilot subjects shows a robust effect 
(mean r = 0.48, range [0.20–0.72]), suggesting the phenomenon is real. The sample 
size (N=50) is well-powered to detect the predicted effect size.

I am confident this project will produce high-quality data and publishable results.

Sincerely,

[Signature]

[Printed Name]
[Title]
[Institution]
[Contact Info]
```

---

## CHECKLIST: All Docs Complete for NSF Submission

- [ ] NSF_GRANT_COMPLETE.md (15 pages) ✓
- [ ] Figure 1: Grammar → Coherence conceptual pipeline
- [ ] Figure 2: Four-experiment validation strategy
- [ ] Figure 3: 24-month timeline
- [ ] Biographical Sketch — PI (NSF format, 2 pages)
- [ ] Current and Pending Support (1 page)
- [ ] Conflict of Interest Certification (signed)
- [ ] Researcher CV (2 pages max)
- [ ] Letters of Support (EEG lab director, dept chair if needed)
- [ ] Cover letter (to grants office + NSF)

**Total pages (excluding figures):** ~25 pages of narrative + 10 pages supporting docs = 35 pages total

---

## NEXT ACTION

1. Create figures using PowerPoint/Illustrator
2. Write biographical sketch (copy template above, customize)
3. Compile all documents into single PDF submission packet
4. Submit to your institution's grants office for internal review
5. Send to NSF by October 15 deadline

**Estimated time:** 6–8 hours (figures are the longest part)

