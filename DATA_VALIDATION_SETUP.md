# Real Data Validation Setup

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
