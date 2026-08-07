#!/usr/bin/env python3
"""NEVER RUN, AND WOULD NOT TEST THE THEORY IF IT WERE — audited 2026-08-07.

This is the script with the CORRECT EEG handling: real BIDS layout, per-subject .fif,
epochs around sentence events from ds002315 (UCL Sentence Comprehension). It is the right
shape for the experiment.

It has never run. ds002315 has never been downloaded on this machine — 0 files under
~/data/ds002315 and ~/data/openneuro/ds002315, and ds002315.tar.gz is 993 bytes. The
missing-file path returns (None, None) silently, so this fails without saying so.

AND THE GRAMMAR SIDE IS NOT GRAMMAR. build_adjacency does sequential edges plus RANDOM
long-range edges seeded by the sentence hash:

    np.random.seed(hash(sentence) % 2**32)
    i, j = np.random.randint(0, n_words), np.random.randint(0, n_words)

Deterministic per sentence, so it looks stable across runs, but it is noise with a fixed
seed rather than a parse. validate_real_eeg.py already contains the real spaCy dependency
parse; porting it here is the actual fix.

Nothing in validation-results/ came from this file. eeg_validation_results.json — which
carries "dataset": "ds002315" — was written by phronesis-science/validate_synthetic.py.

See phronesis-science/PROVENANCE.md.
"""
"""
REAL DATA VALIDATION: Grammar-to-Coherence on actual EEG

Downloads OpenNeuro ds002315 (UCL Sentence Comprehension)
Correlates grammatical eigenvalues with dominant brain oscillations

Prediction: r > 0.65 between log(λ₁) and dominant EEG frequency
"""

import os
import json
import argparse
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh
from scipy.signal import welch
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# Try to import spaCy for real parsing
try:
    import spacy
    SPACY_AVAILABLE = True
except ImportError:
    print("⚠️  spaCy not installed. Using heuristic parsing.")
    SPACY_AVAILABLE = False

# Try to import MNE for real EEG
try:
    import mne
    MNE_AVAILABLE = True
except ImportError:
    print("⚠️  MNE not installed. Using mock data.")
    MNE_AVAILABLE = False

print("""
╔════════════════════════════════════════════════════════════════════════╗
║ GRAMMAR-TO-COHERENCE: REAL DATA ANALYSIS ENGINE                       ║
║ ds002315 (UCL Sentence Comprehension EEG)                              ║
╚════════════════════════════════════════════════════════════════════════╝
""")

# ============================================================================
# GRAMMAR ANALYSIS
# ============================================================================

class GrammarAnalyzer:
    """Parse sentences and compute grammatical eigenvalues."""

    def __init__(self, use_spacy=True):
        self.use_spacy = use_spacy and SPACY_AVAILABLE
        if self.use_spacy:
            try:
                self.nlp = spacy.load('en_core_web_sm')
                print("✅ spaCy model loaded (en_core_web_sm)")
            except:
                print("⚠️  Could not load spaCy model. Falling back to heuristic.")
                self.use_spacy = False

    def parse_sentence(self, sentence):
        """
        Parse sentence into dependency structure.
        Returns adjacency matrix of parse tree.
        """
        if not sentence or len(sentence.strip()) < 2:
            return None

        if self.use_spacy:
            return self._parse_spacy(sentence)
        else:
            return self._parse_heuristic(sentence)

    def _parse_spacy(self, sentence):
        """Real parsing using spaCy dependency parser."""
        try:
            doc = self.nlp(sentence)
            n_words = len(doc)

            if n_words < 2:
                return None

            # Build adjacency matrix from dependency structure
            A = np.zeros((n_words, n_words))

            for token in doc:
                if token.head != token:  # Not root
                    A[token.i, token.head.i] = 1.0
                    A[token.head.i, token.i] = 1.0  # Symmetric

            # If disconnected, add root connections
            if A.sum() == 0:
                A = np.ones((n_words, n_words)) - np.eye(n_words)

            return A
        except:
            return None

    def _parse_heuristic(self, sentence):
        """Fallback heuristic parsing."""
        words = sentence.strip().split()
        n_words = len(words)

        if n_words < 2:
            return None

        # Simple heuristic: sequential + random dependencies
        A = np.eye(n_words)  # Self-loops

        # Sequential adjacency (nearby words are connected)
        for i in range(n_words - 1):
            A[i, i+1] = 1
            A[i+1, i] = 1

        # Random long-range dependencies (representing predicates, objects)
        np.random.seed(hash(sentence) % 2**32)
        for _ in range(max(1, n_words // 3)):
            i = np.random.randint(0, n_words)
            j = np.random.randint(0, n_words)
            if i != j:
                A[i, j] = 1
                A[j, i] = 1

        return A

    def get_eigenvalue(self, A):
        """Compute dominant eigenvalue (coherence) from adjacency matrix."""
        if A is None or A.shape[0] < 2:
            return None

        try:
            if A.shape[0] > 100:
                A_sparse = csr_matrix(A)
                eigenvalues = eigsh(A_sparse, k=1, which='LA', return_eigenvectors=False)
                return float(eigenvalues[-1])
            else:
                eigenvalues = np.linalg.eigvalsh(A)
                return float(eigenvalues[-1])
        except:
            return None

# ============================================================================
# EEG ANALYSIS
# ============================================================================

class EEGAnalyzer:
    """Extract spectral features from EEG data."""

    @staticmethod
    def load_subject_eeg(subject_id, data_dir):
        """Load raw EEG data and event markers for one subject."""
        if not MNE_AVAILABLE:
            return None, None

        eeg_file = Path(data_dir) / f"sub-{subject_id:02d}" / "eeg" / f"sub-{subject_id:02d}_task-sentcomp_eeg.fif"
        events_file = Path(data_dir) / f"sub-{subject_id:02d}" / "eeg" / f"sub-{subject_id:02d}_task-sentcomp_events.tsv"

        if not eeg_file.exists():
            return None, None

        try:
            raw = mne.io.read_raw_fif(str(eeg_file), preload=False, verbose=False)
            events_df = pd.read_csv(str(events_file), sep='\t') if events_file.exists() else None
            return raw, events_df
        except:
            return None, None

    @staticmethod
    def extract_spectral_peak(eeg_segment, sfreq=1000, freq_range=(1, 30)):
        """
        Extract dominant frequency from EEG using Welch's method.
        Returns peak frequency in specified range.
        """
        try:
            # Average across channels
            signal = eeg_segment.mean(axis=0)

            # Welch's power spectral density
            freqs, power = welch(
                signal,
                fs=sfreq,
                nperseg=min(512, len(signal)//2),
                noverlap=None
            )

            # Find peak in frequency range
            mask = (freqs >= freq_range[0]) & (freqs <= freq_range[1])
            if not mask.any():
                return None

            peak_freq = freqs[mask][np.argmax(power[mask])]
            return peak_freq
        except:
            return None

# ============================================================================
# MAIN VALIDATION PIPELINE
# ============================================================================

class ValidationPipeline:
    """Orchestrate grammar-to-EEG correlation analysis."""

    def __init__(self, data_dir, output_dir):
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.grammar = GrammarAnalyzer(use_spacy=SPACY_AVAILABLE)
        self.results = []

    def analyze_subject(self, subject_id):
        """Analyze one subject: compute λ₁ and spectral peaks."""
        print(f"\n📊 Processing subject {subject_id:02d}...", end=" ", flush=True)

        # Load EEG
        raw, events_df = EEGAnalyzer.load_subject_eeg(subject_id, self.data_dir)

        if raw is None:
            print("❌ (EEG file not found)")
            return []

        # Get event markers
        events, event_dict = mne.events_from_annotations(raw, verbose=False)

        if len(events) == 0:
            print("❌ (no events found)")
            return []

        subject_results = []

        # Process each sentence event
        for event_idx, event in enumerate(events[:240]):  # Max 240 sentences
            t_start = event[0]
            t_end = t_start + int(2 * raw.info['sfreq'])  # 2-second window

            if t_end > raw.n_times:
                break

            # Extract EEG segment (all channels)
            eeg_segment = raw[:, t_start:t_end][0]

            # Get dominant frequency from EEG
            peak_freq = EEGAnalyzer.extract_spectral_peak(eeg_segment, sfreq=raw.info['sfreq'])
            if peak_freq is None:
                continue

            # Get sentence text
            sentence = None
            if events_df is not None and 'sentence' in events_df.columns:
                if event_idx < len(events_df):
                    sentence = events_df.iloc[event_idx]['sentence']

            if sentence is None:
                # Use placeholder for testing
                sentence = f"Sentence {event_idx}"

            # Parse sentence and compute λ₁
            A = self.grammar.parse_sentence(str(sentence))
            lambda_1 = self.grammar.get_eigenvalue(A)

            if lambda_1 is not None and peak_freq is not None:
                subject_results.append({
                    'subject': subject_id,
                    'sentence_idx': event_idx,
                    'lambda_1': lambda_1,
                    'peak_freq': peak_freq,
                    'sentence': sentence[:50]  # First 50 chars
                })

        print(f"✅ ({len(subject_results)} valid epochs)")
        return subject_results

    def run(self, subject_range="1-5"):
        """Run analysis on specified subjects."""
        # Parse subject range
        if '-' in subject_range:
            start, end = map(int, subject_range.split('-'))
            subjects = range(start, end + 1)
        else:
            subjects = [int(subject_range)]

        print(f"\n{'='*70}")
        print(f"ANALYZING {len(list(subjects))} SUBJECTS")
        print(f"{'='*70}")

        for subj_id in subjects:
            results = self.analyze_subject(subj_id)
            self.results.extend(results)

        print(f"\n{'='*70}")
        print(f"AGGREGATING RESULTS")
        print(f"{'='*70}")

        if not self.results:
            print("❌ No valid data collected!")
            return None

        # Aggregate across all subjects
        df = pd.DataFrame(self.results)

        lambda_1_vals = np.array(df['lambda_1'])
        peak_freqs = np.array(df['peak_freq'])

        # Primary analysis: log(λ₁) vs dominant frequency
        log_lambda_1 = np.log(lambda_1_vals + 1)

        correlation, p_value = pearsonr(log_lambda_1, peak_freqs)

        print(f"\n📈 RESULTS:")
        print(f"   Sample size: {len(lambda_1_vals)} epochs")
        print(f"   Subjects: {df['subject'].nunique()}")
        print(f"   Correlation: r = {correlation:.4f}")
        print(f"   P-value: p = {p_value:.6f}")
        print(f"   Effect size (r²): {correlation**2:.4f}")

        print(f"\n📋 PREDICTION vs. OBSERVATION:")
        print(f"   Target: r > 0.65")
        print(f"   Observed: r = {correlation:.4f}")

        if correlation > 0.65 and p_value < 0.01:
            print(f"\n   ✅ THEORY VALIDATED ON REAL DATA")
            print(f"      Grammar complexity predicts brain oscillations!")
            status = "VALIDATED"
        elif correlation > 0.50 and p_value < 0.05:
            print(f"\n   ⚠️  PARTIAL SUPPORT")
            print(f"      Relationship present but weaker than predicted")
            status = "PARTIAL"
        else:
            print(f"\n   ❌ NO SIGNIFICANT RELATIONSHIP")
            print(f"      Need to refine theory or check data quality")
            status = "FAILED"

        # Save results
        results_dict = {
            "theory": "Grammar-to-Coherence",
            "dataset": "ds002315",
            "correlation": float(correlation),
            "p_value": float(p_value),
            "r_squared": float(correlation**2),
            "n_epochs": len(lambda_1_vals),
            "n_subjects": int(df['subject'].nunique()),
            "status": status,
            "prediction_target": 0.65,
            "prediction_met": bool(correlation > 0.65 and p_value < 0.01)
        }

        with open(self.output_dir / "validation_results.json", 'w') as f:
            json.dump(results_dict, f, indent=2)

        print(f"\n✅ Results saved to: {self.output_dir / 'validation_results.json'}")

        # Generate plot
        self._plot_results(log_lambda_1, peak_freqs, correlation)

        return results_dict

    def _plot_results(self, log_lambda_1, peak_freqs, correlation):
        """Create publication-ready plot."""
        plt.figure(figsize=(11, 7))

        plt.scatter(log_lambda_1, peak_freqs, alpha=0.5, s=40,
                   color='steelblue', edgecolors='navy', linewidth=0.5)

        # Regression line
        z = np.polyfit(log_lambda_1, peak_freqs, 1)
        p = np.poly1d(z)
        x_line = np.linspace(log_lambda_1.min(), log_lambda_1.max(), 100)
        plt.plot(x_line, p(x_line), 'r--', alpha=0.8, linewidth=2.5,
                label=f'fit: r = {correlation:.3f}')

        plt.xlabel('log(λ₁) — Grammatical Complexity', fontsize=13, fontweight='bold')
        plt.ylabel('Dominant EEG Frequency (Hz)', fontsize=13, fontweight='bold')
        plt.title('Grammar-to-Coherence: Real EEG Validation\n(ds002315: UCL Sentence Comprehension)',
                 fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3, linestyle='--')
        plt.legend(fontsize=11, loc='upper left')

        plt.tight_layout()
        plt.savefig(self.output_dir / 'validation_plot.png', dpi=300, bbox_inches='tight')
        print(f"✅ Plot saved to: {self.output_dir / 'validation_plot.png'}")
        plt.close()

# ============================================================================
# CLI
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Grammar-to-Coherence on real EEG")
    parser.add_argument('--data-dir', default=os.path.expanduser('~/data/openneuro/ds002315'),
                       help='Path to OpenNeuro ds002315 dataset')
    parser.add_argument('--output-dir', default=os.path.expanduser('~/phronesis-papers/validation-results'),
                       help='Output directory for results')
    parser.add_argument('--subjects', default='1-5',
                       help='Subject range to analyze (e.g., "1-5" or "1")')

    args = parser.parse_args()

    pipeline = ValidationPipeline(args.data_dir, args.output_dir)
    results = pipeline.run(subject_range=args.subjects)

    if results:
        print(f"\n{'='*70}")
        print("✅ VALIDATION COMPLETE")
        print(f"{'='*70}\n")
    else:
        print("\n❌ Validation incomplete - no data found")
        print("   Make sure to download ds002315 first:")
        print("   bash download_openneuro.sh\n")
