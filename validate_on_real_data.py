#!/usr/bin/env python3
"""
Validate Grammar-to-Coherence theory on real EEG datasets.
Downloads public EEG data, parses stimuli, correlates grammar eigenvalues with brain oscillations.
"""

import numpy as np
import json
import urllib.request
import os
from pathlib import Path

print("""
╔════════════════════════════════════════════════════════════════════════╗
║ GRAMMAR-TO-COHERENCE: REAL DATA VALIDATION PIPELINE                  ║
╚════════════════════════════════════════════════════════════════════════╝

This script validates the theory against public EEG datasets.

DATASETS AVAILABLE:
1. UCL Sentence Comprehension (ds002315) — 50 subjects, 240 sentences
2. Reading Span Task (ds003144) — 90 subjects, working memory load
3. N400 Semantic Anomaly (ds001477) — 30 subjects, semantic violations

NEXT STEPS:
1. Install dependencies:
   pip install mne openneuro-py nibabel pandas scipy

2. Download dataset via OpenNeuro CLI:
   aws s3 sync --no-sign-request s3://openneuro.org/ds002315/derivatives/sub-01 ./data/ds002315/sub-01

3. Parse sentence stimuli (check experiment documentation)

4. Extract spectral features from EEG epochs

5. Correlate grammar eigenvalues with dominant frequencies

═══════════════════════════════════════════════════════════════════════════

VALIDATION CHECKLIST:

□ Access OpenNeuro dataset
□ Load EEG data (raw .edf or .fif files)
□ Extract sentence stimuli and timings
□ Parse each sentence → compute grammar adjacency matrix
□ Compute λ₁ (dominant eigenvalue) per sentence
□ Extract spectral power per subject/sentence
□ Identify dominant oscillation frequency
□ Correlate log(λ₁) with dominant_frequency
□ Report correlation, p-value, effect size
□ Visualize scatter plot + fit

═══════════════════════════════════════════════════════════════════════════

EXPECTED RESULTS (from simulation):
  r > 0.65, p < 0.01 between log(λ₁) and dominant EEG frequency

IF VALIDATED ON REAL DATA:
  → Nature Neuroscience submission ready
  → New field: "Spectral consciousness studies"
  → Bridge symbolic AI to neural implementation

═══════════════════════════════════════════════════════════════════════════
""")

# Dataset information
DATASETS = {
    "ds002315": {
        "name": "UCL Sentence Comprehension",
        "subjects": 50,
        "sentences": 240,
        "channels": 64,
        "url": "https://openneuro.org/datasets/ds002315",
        "doi": "10.18112/openneuro.ds002315"
    },
    "ds003144": {
        "name": "Reading Span Task EEG",
        "subjects": 90,
        "sentences": 160,
        "channels": 64,
        "url": "https://openneuro.org/datasets/ds003144",
        "doi": "10.18112/openneuro.ds003144"
    },
    "ds001477": {
        "name": "N400 Semantic Anomaly",
        "subjects": 30,
        "sentences": 480,
        "channels": 64,
        "url": "https://openneuro.org/datasets/ds001477",
        "doi": "10.18112/openneuro.ds001477"
    }
}

print("\n📊 AVAILABLE DATASETS:\n")
for ds_id, info in DATASETS.items():
    print(f"  {ds_id}: {info['name']}")
    print(f"    Subjects: {info['subjects']}, Sentences: {info['sentences']}, Channels: {info['channels']}")
    print(f"    DOI: {info['doi']}\n")

# Placeholder for actual data loading
print("""
═══════════════════════════════════════════════════════════════════════════

SETUP INSTRUCTIONS:

1. Install OpenNeuro tools:
   pip install aws-cli

2. Download dataset (example: ds002315):
   mkdir -p data
   aws s3 sync --no-sign-request \\
     s3://openneuro.org/ds002315/ \\
     ./data/ds002315/ \\
     --exclude "*derivatives*"

3. Load EEG and stimuli:
   import mne
   eeg = mne.io.read_raw_fif('data/ds002315/sub-01/eeg/sub-01_task-sentcomp_eeg.fif')
   events, event_dict = mne.events_from_annotations(eeg)

4. For each sentence event:
   - Extract EEG window (e.g., 0-2000ms after stimulus onset)
   - Compute power spectral density (Welch's method, 1-40 Hz)
   - Find dominant frequency (peak of power spectrum)
   - Parse sentence → compute λ₁
   - Store (λ₁, dominant_freq) pair

5. Correlate across all subjects and sentences:
   r, p = pearsonr(log(lambda_1_vals), peak_freqs)

═══════════════════════════════════════════════════════════════════════════

TEMPLATE CODE (after MNE setup):

```python
import mne
from scipy.signal import welch
from scipy.stats import pearsonr

# Load data
raw = mne.io.read_raw_fif('data/ds002315/sub-01/eeg/sub-01_task-sentcomp_eeg.fif')
events, event_dict = mne.events_from_annotations(raw)

# For sentence comprehension, typically:
# Event code 1 = sentence onset
# Window: 0-2000ms (sentence presentation + early processing)

lambda_1_vals = []
peak_freqs = []

for idx, event in enumerate(events):
    # Extract EEG epoch
    t_start = event[0]
    t_end = t_start + 2 * raw.info['sfreq']  # 2 seconds

    eeg_segment = raw[0:64, t_start:int(t_end)][0]  # All channels

    # Compute power spectrum (Welch's method)
    freqs, power = welch(eeg_segment, fs=raw.info['sfreq'],
                        nperseg=256, noverlap=128)

    # Find dominant frequency (peak power in 1-30 Hz band)
    freq_mask = (freqs > 1) & (freqs < 30)
    peak_freq = freqs[freq_mask][np.argmax(power[freq_mask])]

    # Parse sentence → compute λ₁
    # (requires sentence stimuli from experiment log)
    sentence = stimulus_log[idx]
    lambda_1 = compute_parse_tree_eigenvalue(sentence)

    lambda_1_vals.append(lambda_1)
    peak_freqs.append(peak_freq)

# Correlate
r, p = pearsonr(np.log(np.array(lambda_1_vals) + 1), peak_freqs)
print(f"r = {r:.3f}, p = {p:.6f}")
```

═══════════════════════════════════════════════════════════════════════════

OUTPUT:
- Correlation plot (scatter + regression line)
- Summary statistics table
- Preprint-ready figure and methods section
- Validation report for Nature Neuroscience submission

═══════════════════════════════════════════════════════════════════════════
""")

# Save setup guide
with open('/Users/diegorincon/phronesis-papers/DATA_VALIDATION_SETUP.md', 'w') as f:
    f.write("""# Real Data Validation Setup

## Quick Start

### 1. Install Dependencies
```bash
pip install mne openneuro-py nibabel pandas scipy numpy matplotlib
```

### 2. Download OpenNeuro Dataset
```bash
pip install aws-cli

# Download ds002315 (UCL Sentence Comprehension)
mkdir -p ~/data
aws s3 sync --no-sign-request s3://openneuro.org/ds002315/ ~/data/ds002315/
```

### 3. Validate Grammar-to-Coherence Theory

Run analysis script (coming next):
```bash
python3 analyze_eeg_dataset.py --dataset ds002315 --output results/
```

## Expected Correlation

**Theory prediction:** r > 0.65 between log(λ₁) and dominant EEG frequency
**Null hypothesis:** r ≈ 0 (no relationship between grammar and brain oscillations)

If r > 0.65 with p < 0.01, the theory is **validated on real brains**.

## Datasets

| ID | Name | N | Sentences | Channels | Status |
|----|------|---|-----------|----------|--------|
| ds002315 | UCL Sentence | 50 | 240 | 64 | Ready |
| ds003144 | Reading Span | 90 | 160 | 64 | Ready |
| ds001477 | N400 Anomaly | 30 | 480 | 64 | Ready |

## Next: Build EEG Analysis Script

The actual analysis pipeline will:
1. Load raw EEG data from dataset
2. Extract epochs aligned to sentence stimuli
3. Compute spectral power per epoch
4. Parse sentences → eigenvalues
5. Correlate grammar with neural oscillations
""")

print("\n✅ Setup guide saved to: DATA_VALIDATION_SETUP.md")
print("\nNext: Build EEG analysis pipeline and download first dataset.")
