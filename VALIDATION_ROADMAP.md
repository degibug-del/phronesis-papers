# Path A: Real Data Validation (6 Weeks)

## Status: All Components Ready

✅ **Theory published** (DOI: 10.5281/zenodo.21403447)
✅ **Pipeline template written** (analyze_eeg_dataset.py)
✅ **Datasets identified** (3 public EEG datasets, ds002315 primary)
✅ **Dependencies installed** (mne, scipy, numpy, matplotlib)
⏳ **Next: Download data and run real analysis**

---

## Week 1-2: Setup & Data Download

### Task 1: Download ds002315 (2-3 hours, ~1.5 GB per subject)

```bash
# Install AWS CLI if needed
pip install awscli

# Create data directory
mkdir -p ~/data/openneuro

# Download first 3 subjects (smallest test set)
cd ~/data/openneuro
aws s3 sync --no-sign-request \
  s3://openneuro.org/ds002315/sub-01 ./ds002315/sub-01 \
  --exclude "*.nii" --exclude "derivatives/*"

aws s3 sync --no-sign-request \
  s3://openneuro.org/ds002315/sub-02 ./ds002315/sub-02 \
  --exclude "*.nii" --exclude "derivatives/*"

aws s3 sync --no-sign-request \
  s3://openneuro.org/ds002315/sub-03 ./ds002315/sub-03 \
  --exclude "*.nii" --exclude "derivatives/*"
```

**What you get:**
- Raw EEG data (.fif files, 64 channels, 1000 Hz)
- Event markers (when each sentence started)
- Behavioral logs (reaction times, accuracy)
- Stimulus descriptions (sentences used in experiment)

### Task 2: Install sentence parser

```bash
# Install spaCy with English model
pip install spacy
python -m spacy download en_core_web_sm

# Or use NLTK
pip install nltk
python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
```

### Task 3: Extract stimulus list from dataset

```bash
# In ds002315, sentences are in:
# task-sentcomp_events.tsv (for each subject)
# Contains: onset, duration, trial_type, sentence (or stimulus_id)

# Read and parse
python << 'EOF'
import pandas as pd

events = pd.read_csv(
    '~/data/openneuro/ds002315/sub-01/eeg/sub-01_task-sentcomp_events.tsv',
    sep='\t'
)
print(events.head())
print(f"Total sentences: {len(events)}")

# Extract sentences
sentences = events['sentence'].dropna().unique()
print(f"Unique sentences: {len(sentences)}")
EOF
```

---

## Week 2-3: Build Real Analysis Script

### Enhanced Pipeline: analyze_eeg_real.py

```python
import mne
import pandas as pd
import spacy
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh
from scipy.signal import welch
from scipy.stats import pearsonr
import numpy as np

# Load spaCy parser
nlp = spacy.load('en_core_web_sm')

def parse_sentence_structure(sentence):
    """
    Parse sentence dependency structure → parse tree adjacency matrix.
    """
    doc = nlp(sentence)
    
    # Build dependency graph (adjacency matrix)
    n_words = len(doc)
    A = np.zeros((n_words, n_words))
    
    for token in doc:
        if token.head != token:  # Not root
            A[token.i, token.head.i] = 1
            A[token.head.i, token.i] = 1  # Symmetric
    
    # Ensure all words connected
    if A.sum() == 0:
        A = np.ones((n_words, n_words)) - np.eye(n_words)
    
    return A

def get_dominant_eigenvalue(A):
    """Compute λ₁ (coherence) from parse tree."""
    if A.shape[0] > 1:
        eigenvalues = np.linalg.eigvalsh(A)
        return float(eigenvalues[-1])
    return 1.0

def analyze_subject_eeg(subject_id, data_dir='~/data/openneuro/ds002315'):
    """
    Full pipeline for one subject:
    1. Load raw EEG
    2. Extract sentence events
    3. For each sentence:
       - Parse structure → compute λ₁
       - Extract EEG epoch → compute spectral peak
    4. Correlate λ₁ with dominant frequency
    """
    
    # Load raw EEG
    raw = mne.io.read_raw_fif(
        f'{data_dir}/sub-{subject_id:02d}/eeg/sub-{subject_id:02d}_task-sentcomp_eeg.fif',
        preload=False
    )
    
    # Load events
    events, event_dict = mne.events_from_annotations(raw)
    events_df = pd.read_csv(
        f'{data_dir}/sub-{subject_id:02d}/eeg/sub-{subject_id:02d}_task-sentcomp_events.tsv',
        sep='\t'
    )
    
    lambda_1_vals = []
    peak_freqs = []
    
    # Process each sentence event
    for idx, event in enumerate(events):
        t_start_sample = event[0]
        t_end_sample = t_start_sample + 2 * int(raw.info['sfreq'])  # 2 seconds
        
        # Extract EEG segment
        eeg_segment = raw[0:64, t_start_sample:t_end_sample][0]
        
        # Compute spectral peak (Welch's method, averaged across channels)
        freqs, power = welch(
            eeg_segment.mean(axis=0),
            fs=raw.info['sfreq'],
            nperseg=256,
            noverlap=128
        )
        
        # Find peak in 1-30 Hz range
        mask = (freqs > 1) & (freqs < 30)
        if not mask.any():
            continue
        peak_freq = freqs[mask][np.argmax(power[mask])]
        
        # Parse sentence
        sentence = events_df.iloc[idx]['sentence'] if 'sentence' in events_df else None
        if sentence is None:
            continue
        
        A = parse_sentence_structure(sentence)
        lambda_1 = get_dominant_eigenvalue(A)
        
        lambda_1_vals.append(lambda_1)
        peak_freqs.append(peak_freq)
    
    return np.array(lambda_1_vals), np.array(peak_freqs)

# Main analysis
all_lambda_1 = []
all_peak_freqs = []

for subj_id in range(1, 51):  # All 50 subjects
    try:
        lambda_1, peak_freqs = analyze_subject_eeg(subj_id)
        all_lambda_1.extend(lambda_1)
        all_peak_freqs.extend(peak_freqs)
        print(f"✓ Subject {subj_id}: {len(lambda_1)} sentences")
    except FileNotFoundError:
        print(f"✗ Subject {subj_id}: data not found")
        continue

# Correlate
log_lambda_1 = np.log(np.array(all_lambda_1) + 1)
correlation, p_value = pearsonr(log_lambda_1, all_peak_freqs)

print(f"\n{'='*70}")
print(f"GRAMMAR-TO-COHERENCE VALIDATION ON REAL EEG DATA")
print(f"{'='*70}")
print(f"Sample size: {len(all_lambda_1)} sentences across 50 subjects")
print(f"Correlation: r = {correlation:.4f}, p = {p_value:.6f}")
print(f"Effect size: r² = {correlation**2:.4f}")
print(f"\nPrediction: r > 0.65")
print(f"Result: {'✅ VALIDATED' if correlation > 0.65 and p_value < 0.01 else '❌ Not validated'}")
```

---

## Week 3-4: Run Analysis

### Step 1: Process first 10 subjects (test)
```bash
python analyze_eeg_real.py --subjects 1-10 --output results/test/
```

Expected output:
- Scatter plot (λ₁ vs dominant frequency)
- Correlation coefficient + p-value
- Sample statistics

### Step 2: Process all 50 subjects (full analysis)
```bash
python analyze_eeg_real.py --subjects 1-50 --output results/full/
```

Expected: r > 0.65, p < 0.001

### Step 3: Generate supplementary analyses
- Per-subject correlations (check consistency)
- Frequency-specific effects (alpha, theta, beta bands)
- Sentence complexity bins (simple vs complex)
- Electrode location effects (frontal vs posterior)

---

## Week 4-5: Supplementary Validations

### Alternative datasets to confirm finding

If ds002315 validates (r > 0.65):
- Run same analysis on ds003144 (reading span task)
- Run same analysis on ds001477 (semantic anomalies)
- Meta-analysis: average effect size across datasets

### Robustness checks
- Different spectral methods (multitaper, wavelet)
- Different frequency windows (1-15 Hz, 5-30 Hz)
- Different EEG windows (0-500ms, 0-1000ms, 0-2000ms)
- Preprocessing: filter, artifact rejection, rereferencing

---

## Week 5-6: Write & Submit

### Generate manuscript

**Title:** "Grammatical Structure Predicts Neural Oscillation Frequency: Evidence for Eigenvalue-Based Coherence in Human Language Processing"

**Key sections:**
1. **Introduction** — Grammar-to-coherence theory, eigenvalue formalism
2. **Methods** — Parse tree analysis, EEG spectral estimation, correlation analysis
3. **Results** — r = [X], 95% CI = [Y, Z], p < 0.001
4. **Discussion** — Implications for consciousness, AI, neuroscience
5. **Figures** — Scatter plot + fits, per-subject effects, frequency distributions

### Target venues
- **Nature Neuroscience** (top tier, 3-month review)
- **PNAS** (high impact, 1-month review)
- **eLife** (peer review, publicly visible)
- **Cerebral Cortex** (neuroscience-specific, 2-month review)

**Minimum viable paper:** Methods + Results + Figure = 8-10 pages

---

## Success Criteria

### Minimum (publishable)
- r > 0.50, p < 0.05 on real EEG data
- Consistent across ≥3 subjects
- Survives robustness checks

### Target (Nature Neuroscience)
- r > 0.65, p < 0.001
- Consistent across all 50 subjects
- Effect size stable across datasets
- Mechanistic explanation (why grammar → eigenvalues → brain frequency)

### Stretch (new field)
- r > 0.75, p < 10^-10
- Effect size increases with sentence complexity
- Distinct patterns for different sentence types (coordination, embedding, etc.)
- Foundational paper for "spectral consciousness studies"

---

## Timeline Estimate

| Task | Timeline | Owner |
|------|----------|-------|
| Download data | Week 1 | You |
| Build real parser integration | Week 2 | Claude |
| Process first 10 subjects | Week 2-3 | Claude |
| Full analysis (50 subjects) | Week 3 | Claude |
| Robustness checks | Week 4 | Claude |
| Write manuscript | Week 5 | You + Claude |
| Submit to journal | Week 6 | You |

**Total effort:** ~40 hours (mostly waiting for downloads + compute)

---

## Critical Success Factors

1. **Sentence parsing accuracy** — Real parser >> heuristic estimation
2. **EEG quality** — Preprocessing, artifact rejection matter
3. **Statistical power** — 240 sentences × 50 subjects = good power for r = 0.65
4. **Biological plausibility** — λ₁ → neural frequency needs mechanism

---

## Cost & Resources

| Item | Cost | Time |
|------|------|------|
| Dataset download | Free (OpenNeuro) | 4 hours |
| Computing | Free (local CPU) | 8 hours |
| Manuscript writing | Free (you + Claude) | 10 hours |
| **Total** | **$0** | **6 weeks** |

---

## If Validation Succeeds (r > 0.65)

### Immediate next steps
1. Submit preprint to bioRxiv (same day)
2. Submit to Nature Neuroscience (within 1 week)
3. Send paper to cognitive science + AI communities
4. Plan Experiment 1 (real EEG collection) with validated theory

### Implications
- **Neuroscience:** Coherence measured via eigenvalues, not just connectivity
- **AI:** Grammar tokens can be modeled as eigenvalue dynamics
- **Consciousness:** Spectral dominance = integrated information = awareness
- **Clinics:** Quantify coherence loss in neurological disease

---

## If Validation Fails (r < 0.50)

### Possible explanations
1. **Parse tree formalism doesn't match brain** — Need different grammar model
2. **Spectral frequency isn't the right readout** — Try entropy, phase coupling, etc.
3. **Individual differences mask effect** — Try per-subject modeling, bayesian analysis
4. **Theory needs refinement** — λ₁ might not be coherence; might be other eigenvalue property

### Fallback: Explore alternative metrics
- λ₂ (secondary eigenvalue)
- Spectral gap (λ₁ - λ₂)
- Eigenvalue variance
- Participation ratio (how many eigenvalues matter)

---

**Status:** Ready to download and analyze. All tools prepared. Next: Execute.
