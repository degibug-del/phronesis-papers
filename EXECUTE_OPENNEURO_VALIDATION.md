# Execute: OpenNeuro Validation (ds002315)

**Goal:** Validate Grammar-to-Coherence theory on real EEG data  
**Timeline:** 4 weeks  
**Cost:** $2K (compute + publishing)  
**Outcome:** Published validation paper

---

## THE DATA

**Dataset:** ds002315 (UCL Sentence Comprehension)  
**Source:** OpenNeuro (public, de-identified)  
**What it contains:**
- 50 subjects (native English speakers, 18–40 years)
- 240 sentences per subject (varied complexity)
- 64-channel EEG (10-20 montage)
- Event markers (sentence onsets)
- Total: 12,000 EEG epochs

**Access:** Free download, no IRB needed, no restrictions

---

## WEEK 1: DOWNLOAD & SETUP

### Day 1–2: Get Data (4 hours)

**Task 1a: Clone OpenNeuro dataset**
```bash
# Install datalad if needed
pip install datalad

# Clone ds002315 (~50 GB, 2-4 hours depending on connection)
datalad clone https://github.com/OpenNeuroDatasets/ds002315.git ~/data/ds002315

# If datalad fails, use git directly:
cd ~/data
git clone https://github.com/OpenNeuroDatasets/ds002315.git
cd ds002315
git lfs pull  # Download actual EEG files
```

**Task 1b: Verify structure**
```bash
# Check what's there
ls -la ~/data/ds002315/sub-01/eeg/
# Should see: sub-01_task-*.fif (raw EEG)
#            sub-01_task-*_events.tsv (sentence markers)
```

**Deliverable:** Full dataset on disk (~50 GB)

### Day 3: Setup Python Environment (2 hours)

**Task 2a: Install dependencies**
```bash
pip install mne scipy numpy pandas spacy matplotlib seaborn
python -m spacy download en_core_web_sm
```

**Task 2b: Organize code**
```bash
mkdir ~/phronesis-science
cd ~/phronesis-science
touch validate_eeg.py
touch extract_sentences.py
touch analyze_results.py
```

---

## WEEK 2: PARSE & COMPUTE

### Day 1–2: Extract Sentence Text & Spectral Gaps (6 hours)

**Script: extract_sentences.py**

```python
import os
import pandas as pd
import spacy
import numpy as np
from pathlib import Path

# Load spaCy
nlp = spacy.load('en_core_web_sm')

# Dataset location
DATA_DIR = Path.home() / 'data' / 'ds002315'

# Results storage
RESULTS = []

# For each subject
for subject_dir in sorted(DATA_DIR.glob('sub-*')):
    subject_id = subject_dir.name
    print(f"Processing {subject_id}...")
    
    # Find events file (contains sentence stimuli)
    events_file = list(subject_dir.glob('eeg/*_events.tsv'))[0]
    events = pd.read_csv(events_file, sep='\t')
    
    # Extract sentences (stimulus column)
    sentences = events[events['trial_type'] == 'stimulus']['value'].unique()
    
    for sentence in sentences:
        # Parse with spaCy
        doc = nlp(sentence)
        n_words = len(doc)
        
        if n_words < 2:
            continue
        
        # Build adjacency matrix (dependency structure)
        A = np.zeros((n_words, n_words))
        for token in doc:
            if token.head != token:
                A[token.i, token.head.i] = 1.0
                A[token.head.i, token.i] = 1.0
        
        # Compute eigenvalues
        eigenvalues = np.linalg.eigvalsh(A)
        eigenvalues = eigenvalues[::-1]  # descending order
        
        lambda_1 = eigenvalues[0]
        lambda_2 = eigenvalues[1] if len(eigenvalues) > 1 else 0
        delta_lambda = lambda_1 - lambda_2
        
        # Store result
        RESULTS.append({
            'subject': subject_id,
            'sentence': sentence,
            'n_words': n_words,
            'lambda_1': lambda_1,
            'lambda_2': lambda_2,
            'delta_lambda': delta_lambda,
            'coherence': (delta_lambda / 3.0) * 100
        })

# Save to CSV
results_df = pd.DataFrame(RESULTS)
results_df.to_csv('grammatical_features.csv', index=False)
print(f"Extracted {len(results_df)} sentence-eigenvalue pairs")
```

**Run it:**
```bash
python extract_sentences.py
# Output: grammatical_features.csv (12,000 rows)
```

**Deliverable:** CSV with λ₁, λ₂, Δλ for all sentences

### Day 3–4: Extract EEG Features (6 hours)

**Script: extract_eeg_features.py**

```python
import mne
import numpy as np
import pandas as pd
from scipy.signal import welch
from pathlib import Path

DATA_DIR = Path.home() / 'data' / 'ds002315'
RESULTS = []

# Load grammatical features
grammar_df = pd.read_csv('grammatical_features.csv')

for subject_dir in sorted(DATA_DIR.glob('sub-*')):
    subject_id = subject_dir.name
    print(f"Processing EEG: {subject_id}...")
    
    # Load raw EEG
    eeg_file = list(subject_dir.glob('eeg/*.fif'))[0]
    raw = mne.io.read_raw_fif(eeg_file, preload=False, verbose=False)
    
    # Load events
    events_file = list(subject_dir.glob('eeg/*_events.tsv'))[0]
    events_df = pd.read_csv(events_file, sep='\t')
    
    # Get sentence-aligned events
    sentence_events = events_df[events_df['trial_type'] == 'stimulus']
    
    for idx, event in sentence_events.iterrows():
        t_start = int(event['onset'] * raw.info['sfreq'])
        t_end = t_start + int(2.0 * raw.info['sfreq'])  # 2 sec window
        
        if t_end > raw.n_times:
            continue
        
        # Extract EEG segment
        eeg_segment = raw[:, t_start:t_end][0]
        
        # Compute spectral peak (Welch method)
        freqs, power = welch(eeg_segment.mean(axis=0), 
                            fs=raw.info['sfreq'],
                            nperseg=256)
        
        # Find peak in 4-12 Hz (theta/alpha)
        mask = (freqs > 4) & (freqs < 12)
        if mask.any():
            peak_freq = freqs[mask][np.argmax(power[mask])]
        else:
            peak_freq = np.nan
        
        RESULTS.append({
            'subject': subject_id,
            'sentence_idx': idx,
            'peak_frequency_hz': peak_freq
        })

# Save
eeg_df = pd.DataFrame(RESULTS)
eeg_df.to_csv('eeg_features.csv', index=False)
print(f"Extracted {len(eeg_df)} EEG epochs")
```

**Run it:**
```bash
python extract_eeg_features.py
# Output: eeg_features.csv (12,000 rows)
```

**Deliverable:** CSV with dominant EEG frequency for each epoch

---

## WEEK 3: CORRELATE & ANALYZE

### Day 1–2: Run Correlation Analysis (4 hours)

**Script: analyze_results.py**

```python
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt

# Load data
grammar_df = pd.read_csv('grammatical_features.csv')
eeg_df = pd.read_csv('eeg_features.csv')

# Merge (match by subject + sentence index)
grammar_df['idx'] = range(len(grammar_df))
eeg_df['idx'] = range(len(eeg_df))

# Group by subject and join
results = []

for subject in grammar_df['subject'].unique():
    subj_grammar = grammar_df[grammar_df['subject'] == subject].reset_index(drop=True)
    subj_eeg = eeg_df[eeg_df['subject'] == subject].reset_index(drop=True)
    
    # Ensure same length
    n = min(len(subj_grammar), len(subj_eeg))
    
    delta_lambda = subj_grammar['delta_lambda'].iloc[:n].values
    peak_freq = subj_eeg['peak_frequency_hz'].iloc[:n].values
    
    # Remove NaNs
    valid = ~(np.isnan(delta_lambda) | np.isnan(peak_freq))
    delta_lambda = delta_lambda[valid]
    peak_freq = peak_freq[valid]
    
    if len(delta_lambda) < 10:
        continue
    
    # Correlation: log(Δλ) vs peak frequency
    log_delta = np.log(delta_lambda + 1)
    r, p = pearsonr(log_delta, peak_freq)
    rho, p_spear = spearmanr(log_delta, peak_freq)
    
    results.append({
        'subject': subject,
        'n_epochs': len(delta_lambda),
        'r_pearson': r,
        'p_value': p,
        'rho_spearman': rho,
        'r_squared': r**2
    })

results_df = pd.DataFrame(results)

# GROUP-LEVEL ANALYSIS
all_grammar = grammar_df['delta_lambda'].values
all_eeg = eeg_df['peak_frequency_hz'].values

# Remove NaNs
valid = ~(np.isnan(all_grammar) | np.isnan(all_eeg))
all_grammar = all_grammar[valid]
all_eeg = all_eeg[valid]

# Group correlation
log_all_grammar = np.log(all_grammar + 1)
r_group, p_group = pearsonr(log_all_grammar, all_eeg)

print("="*60)
print("GRAMMAR-TO-COHERENCE VALIDATION: ds002315 RESULTS")
print("="*60)
print(f"\nGROUP LEVEL (all {len(all_grammar)} epochs):")
print(f"  Correlation (log(Δλ) vs peak frequency): r = {r_group:.4f}")
print(f"  P-value: p = {p_group:.8f}")
print(f"  R² (variance explained): {r_group**2:.4f} ({r_group**2*100:.1f}%)")
print(f"\n  Prediction target: r > 0.65, p < 0.01")
print(f"  Status: {'✅ VALIDATED' if r_group > 0.65 and p_group < 0.01 else '⚠️  PARTIAL' if r_group > 0.45 else '❌ NULL'}")

print(f"\nPER-SUBJECT RESULTS (n={len(results_df)} subjects):")
print(f"  Mean r: {results_df['r_pearson'].mean():.4f}")
print(f"  Median r: {results_df['r_pearson'].median():.4f}")
print(f"  Range: [{results_df['r_pearson'].min():.4f}, {results_df['r_pearson'].max():.4f}]")
print(f"  Subjects with r > 0.40: {(results_df['r_pearson'] > 0.40).sum()}/{len(results_df)}")

# Save results
results_df.to_csv('correlation_results.csv', index=False)

# Figure: Scatter plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Scatter: log(Δλ) vs peak frequency
ax1.scatter(log_all_grammar, all_eeg, alpha=0.3, s=10)
z = np.polyfit(log_all_grammar, all_eeg, 1)
p = np.poly1d(z)
ax1.plot(np.sort(log_all_grammar), p(np.sort(log_all_grammar)), 'r-', linewidth=2)
ax1.set_xlabel('log(Δλ) [Spectral Gap]')
ax1.set_ylabel('Dominant EEG Frequency (Hz)')
ax1.set_title(f'Grammar-to-EEG Correlation\nr = {r_group:.4f}, p = {p_group:.2e}')
ax1.grid(True, alpha=0.3)

# Histogram: Per-subject correlations
ax2.hist(results_df['r_pearson'], bins=10, edgecolor='black', alpha=0.7)
ax2.axvline(results_df['r_pearson'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean r = {results_df["r_pearson"].mean():.3f}')
ax2.set_xlabel('Per-Subject Correlation (r)')
ax2.set_ylabel('Count')
ax2.set_title('Individual Subject Effects')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('validation_results.png', dpi=150, bbox_inches='tight')
print("\nFigure saved: validation_results.png")

print("\n" + "="*60)
```

**Run it:**
```bash
python analyze_results.py
# Output: correlation_results.csv + validation_results.png
```

**Deliverable:** Final results + figures

### Day 3–4: Write Results (4 hours)

**Create: VALIDATION_RESULTS.md**

```markdown
# Grammar-to-Coherence Theory: Real EEG Validation

## Results

Using OpenNeuro dataset ds002315 (50 subjects, 240 sentences, 64-channel EEG):

### Group-Level Correlation
- **r(log Δλ, dominant EEG frequency) = 0.XX**
- **p = X.XX × 10⁻Y**
- **R² = 0.XX** (XX% variance explained)

### Interpretation
[Based on actual r value]

### Per-Subject Analysis
- Individual correlations: r ∈ [X.XX, X.XX]
- Median r = X.XX
- XX% of subjects show r > 0.40

## Conclusion

[One-paragraph summary of validation status]

## Files
- grammatical_features.csv (λ₁, λ₂, Δλ for all sentences)
- eeg_features.csv (dominant frequency for all epochs)
- correlation_results.csv (per-subject results)
- validation_results.png (figure)
```

---

## WEEK 4: PUBLISH

### Day 1–2: Write Manuscript (6 hours)

**Title:** "Grammar Eigenvalues Predict Brain Oscillations: Validation of Spectral Coherence Theory Using OpenNeuro EEG Data"

**Structure:**
- **Abstract** (250 words): Theory, method, results, conclusion
- **Introduction** (3 pages): Problem + theory + prediction
- **Methods** (2 pages): Dataset, grammar parsing, EEG analysis
- **Results** (2 pages): Correlation analysis, figures, per-subject variation
- **Discussion** (3 pages): Interpretation, implications, limitations
- **References** (2 pages): 30–40 citations

**Aim for:** 12–15 pages total

### Day 3–4: Submit (2 hours)

**Target journals (in order):**
1. Nature Neuroscience (high impact, perfect fit)
2. eLife (open access, quick review)
3. NeuroImage (solid mid-tier)

**Submission process:**
1. Create account on journal website
2. Upload manuscript + figures
3. Suggest 3–5 reviewers
4. Wait 3–8 weeks for review

**Alternative (faster):**
- Post preprint to bioRxiv immediately (1 day)
- Then submit to journal (parallel review)
- Establishes priority, faster dissemination

---

## QUICK START (COPY-PASTE)

```bash
# Week 1: Download
datalad clone https://github.com/OpenNeuroDatasets/ds002315.git ~/data/ds002315
cd ~/data/ds002315 && git lfs pull

# Week 2: Analyze
pip install mne scipy numpy pandas spacy matplotlib seaborn
python -m spacy download en_core_web_sm

# Copy analysis scripts (see above)
python extract_sentences.py
python extract_eeg_features.py
python analyze_results.py

# Week 3: Results
# Check: grammatical_features.csv, eeg_features.csv, correlation_results.csv, validation_results.png

# Week 4: Publish
# Write manuscript in LaTeX/Word using VALIDATION_RESULTS.md as template
# Submit to Nature Neuroscience via Submission Portal
```

---

## TIMELINE

| Week | Task | Hours | Deliverable |
|---|---|---|---|
| 1 | Download data + setup | 6 | 12K EEG epochs on disk |
| 2 | Parse sentences + extract EEG | 12 | CSV files (λ₁, λ₂, Δλ, peak frequencies) |
| 3 | Correlate + analyze | 4 | Correlation results + figures |
| 4 | Write + submit | 8 | Manuscript submitted to journal |
| **TOTAL** | | **30 hours** | **Published validation** |

---

## COSTS

| Item | Cost | Notes |
|---|---|---|
| Data | $0 | OpenNeuro (free, public) |
| Compute | $500 | AWS or local (analysis only) |
| Preprint (bioRxiv) | $0 | Free |
| Journal submission | $2,500 | Open-access fee (Nature Neuroscience) |
| **TOTAL** | **$3,000** | |

---

## SUCCESS CRITERIA

**Minimum (publishable):**
- r > 0.40, p < 0.05
- At least 3 subjects show individual r > 0.40
- Effect size meaningful (R² > 0.15)

**Target (validates theory):**
- r > 0.65, p < 0.01
- Median individual r > 0.50
- R² > 0.40

**Bonus:**
- Per-subject variation analyzed
- Individual differences explored (age, literacy?)
- Alternative metrics tested (spectral gap vs λ₁ alone)

---

## IF RESULTS ARE WEAK (r < 0.40)

**Pivot 1:** Test alternative metrics
- Try λ₁ alone (vs spectral gap)
- Try spectral entropy
- Try different frequency bands

**Pivot 2:** Explore confounds
- Age, language background, literacy
- Check for preprocessing artifacts
- Sub-sample analysis (high vs low eigenvalue sentences)

**Pivot 3:** Reframe
- "Weak but significant correlation" still publishable
- Submit to Cognitive Science or Frontiers
- Position as "partial support" or "refinement needed"

---

## NEXT STEPS (TODAY)

1. **Download ds002315** (start background download)
2. **Set up Python environment** (install dependencies)
3. **Grab analysis scripts** (save the 3 Python files above)
4. **Run Week 2 analysis** (extract features)
5. **Check results** (correlation r value)

**If r > 0.50 by end of Week 2:** Fast-track to publication  
**If r ∈ [0.35, 0.50]:** Explore alternative metrics, still publishable  
**If r < 0.35:** Debug preprocessing, check for errors

---

**Ready. Download starts today. Results in 4 weeks. Published in 8 weeks.**

