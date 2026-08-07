# IRB Protocol: Grammar-to-Coherence EEG Study

**Title:** Grammar Eigenvalues and Brain Oscillations: A Test of Coherence Theory

**Principal Investigator:** [Name]  
**Institution:** [University]  
**IRB Protocol #:** [To be assigned]  
**Funding Source:** NSF Cognitive Neuroscience  
**Protocol Version:** 1.0  
**Date:** July 16, 2026

---

## A. STUDY OVERVIEW

### 1. Objectives and Rationale

**Objective:** To investigate whether mathematical properties of grammar (eigenvalues of dependency structures) predict dominant brain oscillations during sentence comprehension.

**Rationale:**
- Grammar is typically studied in linguistics without reference to brain function
- Brain oscillations (EEG) are typically studied without computational linguistic models
- We propose a formal bridge: parse trees → adjacency matrices → eigenvalues → EEG spectral peaks
- This could explain: (1) why coherent writing is easier to understand, (2) how brains process complex sentences, (3) why ambiguous sentences feel confusing

**Hypothesis:** The dominant eigenvalue of a sentence's dependency parse tree (λ₁) predicts the dominant frequency of EEG activity (8–12 Hz alpha band) during that sentence's silent reading.

**Primary endpoint:** Pearson correlation between log(λ₁) and dominant EEG frequency (target: r > 0.65, p < 0.01)

---

## B. STUDY POPULATION

### 1. Inclusion Criteria

- Age: 18–35 years
- Native English speaker (minimum 12+ years of continuous English exposure)
- Right-handed (Edinburgh Handedness Inventory > +40)
- No neurological disorder (self-reported)
- No psychiatric medication
- Normal or corrected-to-normal vision
- Willing to wear EEG cap for 2 hours

### 2. Exclusion Criteria

- History of seizures, traumatic brain injury, stroke
- Diagnosed language disorder (dyslexia, aphasia, etc.)
- Current psychiatric medication
- Claustrophobia or discomfort with cap placement
- Pregnancy (MRI safety precaution, if any imaging planned later)
- Tattoos/piercings on scalp (affect electrode placement)

### 3. Recruitment and Enrollment

**Target N:** 40–60 subjects  
**Recruitment source:** 
- University subject pool (psychology dept; ~30% of subjects)
- Community postings (flyers, social media; ~40%)
- Word-of-mouth referral (existing subjects; ~30%)

**Enrollment procedure:**
1. Phone/email screening (5 min) → inclusion/exclusion criteria
2. Confirm availability (2-hour session)
3. Explain payment: $150 for complete session
4. Schedule session
5. Send detailed instructions (what to expect, contraindications)

---

## C. DETAILED STUDY PROCEDURES

### 1. Pre-Study Visit (Scheduling Call)

**Duration:** 5–10 minutes (phone/video)

**Content:**
- Brief explanation of study
- Confirm inclusion/exclusion criteria
- Answer questions
- Confirm comfort with EEG (no personal/medical concerns)
- Schedule session (book 2-hour slot)

### 2. Day-of-Study Visit (Lab Session)

**Total duration:** 2.5 hours (2 hours active, 30 min setup/cleanup)

#### Pre-Session (15 min)
1. Greet subject, confirm informed consent (in person)
2. Re-screen for inclusion/exclusion (checklist)
3. Measure head size (10–20 system for electrode placement)
4. Explain electrode placement and safety
5. Q&A
6. Have subject sign informed consent (two copies: one for subject, one for file)

#### EEG Setup (15 min)
1. Guide subject to EEG prep area
2. Explain cap (64 electrodes, Ag/AgCl, saline electrolyte)
3. Apply electrode paste/saline to scalp and electrodes
4. Place cap on head, adjust for comfort
5. Check impedance (all channels < 5 kΩ)
6. Place subject in comfortable chair facing monitor (distance: 60 cm)

#### Task Instructions (5 min)
1. Explain task: "You'll see sentences, one at a time. Read them silently. We're recording your brain activity."
2. Practice with 3 sentences
3. Confirm subject understands
4. Clarify: "Keep your head still during each sentence"

#### Main Task (90 min)
**Stimulus presentation:**
- 240 sentences, presented via MATLAB Psychtoolbox (white text on black background)
- Sentence presentation: 500 ms, then 1000 ms viewing window (subject reads silently)
- Brief blank (200 ms), then comprehension question appears (yes/no, 50% targets)
- Subject presses button (button box with <100 ms lag)
- Intertrial interval: 1.5–2.0 s (random)

**Sentences (240 total):**
- Controlled for word count (4–10 words)
- Controlled for frequency (common words)
- No semantic ambiguity (unambiguous sentences only in this experiment)
- Diverse topics (weather, objects, animals, activities)
- Examples:
  - "The cat sat on the mat." (Simple, 6 words)
  - "The young dog ran very quickly through the park." (Complex, 9 words)

**Procedure:**
- 240 sentences presented in 4 blocks (60 sentences each)
- 2-minute rest between blocks (subject can relax)
- Option to take additional break if needed

#### Post-Task (10 min)
1. Remove cap carefully (rinse electrodes from scalp)
2. Rinse subject's hair/scalp if needed
3. Debrief: "Thank you for participating. Your brain data will help us understand how grammar works."
4. Payment: Give $150 cash or check (receipt signed)
5. Confirm contact info for future studies

### 3. Compensation

**Amount:** $150 (cash or check)  
**Payment method:** At end of session  
**Timing:** All subjects paid, regardless of data quality  
**Documentation:** Signature on receipt, with subject ID

---

## D. EEG RECORDING AND ANALYSIS

### 1. EEG Acquisition

**Equipment:**
- EEG cap: 64-channel (BioSemi ActiveTwo or Neurodyne)
- Sampling rate: 500 Hz
- Reference: Cz (central electrode)
- Electrode type: Ag/AgCl with saline
- Impedance: < 5 kΩ per channel (checked pre-study)

**Data storage:**
- Raw .fif file (MNE Python format)
- Metadata: subject ID, age, sex, date, time
- Backup: Copied to secure server within 24 hours

### 2. Preprocessing

1. **High-pass filter:** 0.5 Hz (remove drift)
2. **Low-pass filter:** 100 Hz (remove aliasing)
3. **Notch filter:** 60 Hz (line noise)
4. **Independent Component Analysis (ICA):** Remove eye blinks, muscle artifacts
5. **Artifact rejection:** Channels with > 5 μV peak-to-peak during 500-ms epoch → marked but not excluded
6. **Resampling:** 250 Hz (reduce file size)

### 3. Analysis

**Grammar analysis:**
1. Sentences parsed with spaCy en_core_web_sm
2. Dependency trees converted to adjacency matrices A (n_words × n_words)
3. A is symmetric (undirected graph)
4. Eigenvalue decomposition via numpy.linalg.eigvalsh()
5. Extract λ₁ (largest eigenvalue)
6. Log-transform: log(λ₁ + 1)

**EEG analysis:**
1. Extract 0–1000 ms epoch per sentence (relative to sentence onset)
2. Welch's method (256-point FFT, 50% overlap, Hann window) → power spectral density (PSD)
3. Frequency range: 1–30 Hz
4. Find dominant frequency as peak in PSD
5. Per-subject z-score normalization

**Correlation:**
1. Pearson correlation: log(λ₁) vs dominant frequency
2. P-value via t-test (n = 240 sentences)
3. Permutation test (10,000 shuffles) for robustness
4. Effect size: r, R² = r²

---

## E. RISKS AND SAFEGUARDS

### 1. Potential Risks

**Physical risks (minimal):**
- Discomfort from cap (slight pressure on head for 90 min)
- Mild skin irritation from electrode paste (rare, resolves in hours)
- Claustrophobia (for ~2% of population; mitigated by pre-screening)

**Psychological risks (minimal):**
- Boredom during task (reading 240 sentences)
- Anxiety from electrode placement (mitigated by clear explanation)
- Concern about "brain being read" (mitigated by education on EEG limitations)

**Data privacy risks:**
- EEG data could be re-identified from head shape + electrode positions (very rare)
- Genetic information leaked via genomics databases (not applicable here)
- Behavioral data (reaction times, button presses) could reveal task comprehension

### 2. Safeguards

**Physical safety:**
- Cap is CE-certified for human use
- Electrode paste is hypoallergenic, medical-grade
- Lab monitored by trained technician during session
- Emergency exit clearly marked; subject can stop at any time
- Researcher checks in verbally every 15 minutes during task

**Psychological safety:**
- Detailed informed consent (written, verbal)
- Opportunity for practice trial (3 sentences before main task)
- Clear permission to pause or withdraw at any time
- Debriefing after session explaining study aims
- Contact info for questions/concerns

**Data privacy:**
- De-identified storage: Subject ID only (no name, date of birth, address)
- Encrypted AWS S3 storage (AES-256)
- Access restricted to PI + 1 research assistant (background checked)
- Secure deletion after 3 years (unless subject consents to longer retention)
- Anonymization before sharing (remove head shape, age, identifying metadata)

---

## F. BENEFITS AND RISK-BENEFIT ANALYSIS

### 1. Direct Benefits to Subjects

- Minimal: Subjects learn about their own brain activity (general interest)
- Payment ($150) appropriate compensation for time/effort

### 2. Societal Benefits

- Advances understanding of grammar-brain interface
- Could inform interventions for language disorders (dyslexia, aphasia, dementia)
- Bridges linguistics and neuroscience (educational value)
- Open-source toolkit released for community use

### 3. Risk-Benefit Analysis

**Risks:** Minimal (mild discomfort, privacy concern is very low)  
**Benefits:** Significant (scientific advancement, potential clinical applications)  
**Justification:** Benefits far outweigh risks. This is standard neuroscience research, well-established and low-risk.

---

## G. INFORMED CONSENT

### Key Consent Elements

1. **Study purpose:** Test whether grammar structure predicts brain activity
2. **Procedures:** Wear EEG cap, read 240 sentences for 90 minutes
3. **Duration:** 2.5 hours total
4. **Risks:** Mild discomfort, rare skin irritation
5. **Benefits:** $150 payment, possible knowledge of cognitive processes
6. **Alternatives:** Subjects free to decline or withdraw
7. **Confidentiality:** Data de-identified, stored securely
8. **Voluntary nature:** No penalty for withdrawal
9. **Contact info:** PI name, phone, email for questions
10. **IRB contact:** IRB office contact for concerns about subject rights

**Format:** Written consent document (grade 8 reading level), signed before study

---

## H. DATA MANAGEMENT AND CONFIDENTIALITY

### 1. Data Storage

- **Raw EEG:** Encrypted AWS S3 (server-side encryption, AES-256)
- **Backup:** University secure server (redundant, daily backup)
- **Access:** PI + 1 research assistant only (password-protected)
- **Retention:** 3 years (per NSF/NIH guidelines), then secure deletion

### 2. De-identification

Before sharing data publicly:
- Remove subject name, date of birth, email
- Replace with subject ID (e.g., "S001", "S002")
- Remove session date/time (use relative timing only)
- Remove any identifying metadata from EEG file headers

### 3. Data Sharing

- **Primary dataset:** Available on OpenNeuro after embargo (6 months post-publication)
- **Format:** BIDS standard (BioSemi or Neurodyne BIDS conversion)
- **Restrictions:** Use-restricted (researchers only; sign data use agreement)

---

## I. STATISTICAL ANALYSIS PLAN

### Primary Analysis

**Hypothesis test:** H₀: ρ = 0 (no correlation between log(λ₁) and dominant frequency)

**Method:** Pearson correlation (n = 240 sentences)
- Coefficient: r
- 95% CI: via Fisher's z-transformation
- P-value: two-tailed t-test
- Significance threshold: p < 0.05

**Secondary analysis (robustness):**
- Spearman rank correlation (non-parametric alternative)
- Permutation test (10,000 shuffles) to confirm p-value
- Per-subject correlations (individual variation)
- Split-half reliability (first 120 vs. last 120 sentences)

### Stopping Rule

- Continue enrollment until n = 50 (target N = 40–60)
- No interim analysis

---

## J. QUALIFICATIONS OF RESEARCH TEAM

- **PI:** [PhD in Neuroscience or Psychology, 5+ years EEG experience]
- **EEG Technician:** [Certified clinical neurophysiologist, 3+ years]
- **Data Analyst:** [MS in Statistics, 2+ years EEG analysis]
- **IRB training:** All staff completed CITI certification (human subjects research)

---

## K. APPENDICES

**Appendix A:** Informed Consent Form (1 page)  
**Appendix B:** Screening Checklist (inclusion/exclusion)  
**Appendix C:** Edinburgh Handedness Inventory  
**Appendix D:** Sample Stimuli (10 example sentences)  
**Appendix E:** EEG Cap Diagram (64-electrode positions)  
**Appendix F:** Safety Checklist (technician pre-session)

---

**Approval date:** [To be completed by IRB]  
**Expiration date:** [To be completed by IRB, typically 1 year]  
**Signature of PI:** _________________________ Date: _______

---

*This protocol follows APA Ethical Guidelines, NSF guidelines, and institutional policy for human subjects research.*
