#!/usr/bin/env python3
"""
Simulate the four validation experiments for Grammar-to-Coherence theory.
Tests all core predictions before running real EEG/behavioral studies.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh
import json

np.random.seed(42)

# ============================================================================
# EXPERIMENT 1: EEG Spectral Matching
# ============================================================================

def simulate_parse_tree(depth, branching_factor, noise=0.1):
    """
    Generate a random parse tree adjacency matrix.
    deeper/bushier trees have different eigenvalue spectra.
    """
    n_nodes = branching_factor ** depth
    A = np.zeros((n_nodes, n_nodes))

    # Build tree structure
    for parent in range(n_nodes // branching_factor):
        for child in range(branching_factor):
            child_idx = parent * branching_factor + child + 1
            if child_idx < n_nodes:
                A[parent, child_idx] = 1
                A[child_idx, parent] = 1

    # Add symmetric structure (grammatical nesting)
    A = (A + A.T) / 2

    # Add noise (real grammars are not perfectly symmetric)
    A += np.random.normal(0, noise, A.shape) * (A > 0)
    A = (A + A.T) / 2  # Re-symmetrize

    return A

def get_dominant_eigenvalue(A, k=1):
    """Compute largest eigenvalue via sparse eigenvalue decomposition."""
    if A.shape[0] > 100:
        A_sparse = csr_matrix(A)
        eigenvalues = eigsh(A_sparse, k=k, which='LA', return_eigenvectors=False)
        return eigenvalues[-1]
    else:
        eigenvalues = np.linalg.eigvalsh(A)
        return eigenvalues[-1]

def simulate_eeg_spectrum(lambda_1, noise_level=0.1):
    """
    Simulate EEG power spectral density.
    Dominant frequency correlates with λ₁.
    """
    frequencies = np.linspace(1, 30, 100)

    # Dominant frequency ~ log(λ₁) * 5 + 10 Hz
    dominant_freq = np.log(lambda_1 + 1) * 5 + 10
    dominant_freq = np.clip(dominant_freq, 1, 30)

    # Generate spectrum with dominant peak
    power = np.exp(-((frequencies - dominant_freq) ** 2) / 2)
    power += np.random.normal(0, noise_level, len(power))
    power = np.abs(power)

    # Measure peak frequency
    peak_freq = frequencies[np.argmax(power)]
    return peak_freq, frequencies, power

def experiment_1_eeg():
    """Test: EEG dominant frequency correlates with λ₁"""
    print("\n" + "="*70)
    print("EXPERIMENT 1: EEG Spectral Matching")
    print("="*70)

    n_sentences = 50
    lambda_1_vals = []
    peak_freqs = []

    for i in range(n_sentences):
        # Generate sentences of varying complexity
        depth = np.random.randint(2, 6)
        branching = np.random.randint(2, 4)

        A = simulate_parse_tree(depth, branching)
        lambda_1 = get_dominant_eigenvalue(A)
        peak_freq, _, _ = simulate_eeg_spectrum(lambda_1)

        lambda_1_vals.append(lambda_1)
        peak_freqs.append(peak_freq)

    # Correlate
    correlation = np.corrcoef(np.log(np.array(lambda_1_vals) + 1), peak_freqs)[0, 1]
    p_value = stats.pearsonr(np.log(np.array(lambda_1_vals) + 1), peak_freqs)[1]

    print(f"Correlation (log(λ₁), dominant_frequency): r = {correlation:.3f}, p = {p_value:.6f}")
    print(f"Prediction: r > 0.65")
    print(f"✓ PASSED" if correlation > 0.65 and p_value < 0.01 else "✗ FAILED")

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(np.log(np.array(lambda_1_vals) + 1), peak_freqs, alpha=0.6)
    z = np.polyfit(np.log(np.array(lambda_1_vals) + 1), peak_freqs, 1)
    p = np.poly1d(z)
    plt.plot(np.log(np.array(lambda_1_vals) + 1),
             p(np.log(np.array(lambda_1_vals) + 1)), "r--", alpha=0.8, label=f'fit: r={correlation:.3f}')
    plt.xlabel('log(λ₁)')
    plt.ylabel('Dominant EEG Frequency (Hz)')
    plt.title('Experiment 1: EEG Spectral Matching')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('/Users/diegorincon/phronesis-papers/sim_exp1_eeg.png', dpi=150, bbox_inches='tight')
    plt.close()

    return {'correlation': correlation, 'p_value': p_value, 'passed': correlation > 0.65 and p_value < 0.01}

# ============================================================================
# EXPERIMENT 2: Reaction Time Power Law
# ============================================================================

def simulate_reaction_time(spectral_gap, noise_level=0.15):
    """
    RT = a + b / (gap^c)
    Harder problems (small gap) → longer RT
    """
    a, b, c = 0.3, 1.5, 1.0  # True parameters
    rt = a + b / (spectral_gap ** c)
    rt += np.random.normal(0, noise_level)
    rt = np.clip(rt, 0.2, 3.0)  # Realistic RT range (0.2 - 3 seconds)
    return rt

def simulate_spectral_gap(depth, branching, n_vals=3):
    """Compute spectral gap: λ₁ - λ₂"""
    A = simulate_parse_tree(depth, branching)

    if A.shape[0] > 100:
        A_sparse = csr_matrix(A)
        eigenvalues = eigsh(A_sparse, k=n_vals, which='LA', return_eigenvectors=False)
    else:
        eigenvalues = np.linalg.eigvalsh(A)[-n_vals:]

    eigenvalues = np.sort(eigenvalues)[::-1]
    gap = eigenvalues[0] - eigenvalues[1] if len(eigenvalues) > 1 else eigenvalues[0]
    return gap

def experiment_2_reaction_time():
    """Test: RT scales as 1/spectral_gap (power law)"""
    print("\n" + "="*70)
    print("EXPERIMENT 2: Reaction Time Power Law")
    print("="*70)

    n_sentences = 60
    gaps = []
    rts = []

    for i in range(n_sentences):
        depth = np.random.randint(2, 6)
        branching = np.random.randint(2, 4)
        gap = simulate_spectral_gap(depth, branching)
        rt = simulate_reaction_time(gap)

        gaps.append(gap)
        rts.append(rt)

    gaps = np.array(gaps)
    rts = np.array(rts)

    # Fit power law: RT = a + b / (gap^c)
    # Log-linear fit
    log_gaps = np.log(gaps)
    log_rts = np.log(rts)

    # Linear regression on log space
    coeffs = np.polyfit(log_gaps, log_rts, 1)
    c_estimate = -coeffs[0]  # From log(RT) = c*log(gap) + ...
    r_squared = np.corrcoef(log_gaps, log_rts)[0, 1] ** 2

    print(f"Power law exponent: c = {c_estimate:.3f}")
    print(f"R² = {r_squared:.3f}")
    print(f"Prediction: c ∈ [0.8, 1.2], R² > 0.50")
    print(f"✓ PASSED" if 0.8 <= c_estimate <= 1.2 and r_squared > 0.50 else "✗ FAILED")

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(gaps, rts, alpha=0.6)
    gap_fit = np.linspace(np.min(gaps), np.max(gaps), 100)
    rt_fit = np.exp(np.polyval(coeffs, np.log(gap_fit)))
    plt.plot(gap_fit, rt_fit, 'r--', alpha=0.8, label=f'fit: c={c_estimate:.2f}, R²={r_squared:.3f}')
    plt.xlabel('Spectral Gap (λ₁ - λ₂)')
    plt.ylabel('Reaction Time (seconds)')
    plt.title('Experiment 2: Reaction Time Power Law')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('/Users/diegorincon/phronesis-papers/sim_exp2_rt.png', dpi=150, bbox_inches='tight')
    plt.close()

    return {'c_estimate': c_estimate, 'r_squared': r_squared,
            'passed': 0.8 <= c_estimate <= 1.2 and r_squared > 0.50}

# ============================================================================
# EXPERIMENT 3: Ambiguity and Eigenvalue Degeneracy
# ============================================================================

def simulate_ambiguous_sentence(n_parses=3):
    """
    Ambiguous sentences have multiple valid parse trees.
    Compute eigenvalues for each parse; degeneracy = variance of top eigenvalues.
    """
    eigenvalues_per_parse = []

    for parse_idx in range(n_parses):
        depth = np.random.randint(2, 5)
        branching = np.random.randint(2, 3)
        A = simulate_parse_tree(depth, branching, noise=0.05)

        if A.shape[0] > 100:
            A_sparse = csr_matrix(A)
            eigenvals = eigsh(A_sparse, k=3, which='LA', return_eigenvectors=False)
        else:
            eigenvals = np.linalg.eigvalsh(A)[-3:]

        eigenvalues_per_parse.append(eigenvals)

    eigenvalues_per_parse = np.array(eigenvalues_per_parse)

    # Degeneracy: how much do top eigenvalues vary across parses?
    degeneracy = np.std(eigenvalues_per_parse[:, 0])
    return degeneracy

def simulate_unambiguous_sentence():
    """Unambiguous: single dominant parse, no degeneracy"""
    A = simulate_parse_tree(3, 2.5, noise=0.01)  # Low noise = clear structure

    if A.shape[0] > 100:
        A_sparse = csr_matrix(A)
        eigenvals = eigsh(A_sparse, k=3, which='LA', return_eigenvectors=False)
    else:
        eigenvals = np.linalg.eigvalsh(A)[-3:]

    # Single parse: no variance, just spectral gap
    degeneracy = eigenvals[0] - eigenvals[1]
    return degeneracy

def experiment_3_ambiguity():
    """Test: Ambiguous sentences show eigenvalue degeneracy"""
    print("\n" + "="*70)
    print("EXPERIMENT 3: Ambiguity and Eigenvalue Degeneracy")
    print("="*70)

    # Generate ambiguous and unambiguous sentences
    ambiguous_degeneracy = []
    unambiguous_degeneracy = []

    for _ in range(30):
        ambiguous_degeneracy.append(simulate_ambiguous_sentence(n_parses=3))
        unambiguous_degeneracy.append(simulate_unambiguous_sentence())

    ambiguous_degeneracy = np.array(ambiguous_degeneracy)
    unambiguous_degeneracy = np.array(unambiguous_degeneracy)

    # T-test
    t_stat, p_value = stats.ttest_ind(ambiguous_degeneracy, unambiguous_degeneracy)

    print(f"Ambiguous sentences: degeneracy = {np.mean(ambiguous_degeneracy):.3f} ± {np.std(ambiguous_degeneracy):.3f}")
    print(f"Unambiguous sentences: degeneracy = {np.mean(unambiguous_degeneracy):.3f} ± {np.std(unambiguous_degeneracy):.3f}")
    print(f"t-test: t = {t_stat:.3f}, p = {p_value:.6f}")
    print(f"Prediction: p < 0.05 (ambiguous > unambiguous)")
    print(f"✓ PASSED" if p_value < 0.05 and np.mean(ambiguous_degeneracy) > np.mean(unambiguous_degeneracy) else "✗ FAILED")

    # Plot
    plt.figure(figsize=(10, 6))
    plt.boxplot([unambiguous_degeneracy, ambiguous_degeneracy],
                labels=['Unambiguous', 'Ambiguous'])
    plt.ylabel('Eigenvalue Degeneracy')
    plt.title('Experiment 3: Ambiguity and Eigenvalue Degeneracy')
    plt.grid(True, alpha=0.3, axis='y')
    plt.savefig('/Users/diegorincon/phronesis-papers/sim_exp3_ambiguity.png', dpi=150, bbox_inches='tight')
    plt.close()

    return {'ambiguous_mean': np.mean(ambiguous_degeneracy),
            'unambiguous_mean': np.mean(unambiguous_degeneracy),
            'p_value': p_value,
            'passed': p_value < 0.05 and np.mean(ambiguous_degeneracy) > np.mean(unambiguous_degeneracy)}

# ============================================================================
# EXPERIMENT 4: Dialogue Entanglement
# ============================================================================

def simulate_coupled_coherence(t_max=10):
    """
    Simulate two people (explainer and listener) engaging in dialogue.
    Over time, their coherence states couple.

    Prediction: λ_coupled > λ_E * λ_L early, then stabilizes.
    """
    time_steps = np.linspace(0, t_max, 50)
    lambda_e_trajectory = []
    lambda_l_trajectory = []
    lambda_coupled_trajectory = []

    for t in time_steps:
        # Explainer's coherence (slightly increasing as they explain)
        lambda_e = 0.5 + 0.3 * (1 - np.exp(-t / 3))  # Asymptotes at 0.8

        # Listener's coherence (starts low, increases as understanding grows)
        lambda_l = 0.3 + 0.4 * (1 - np.exp(-t / 4))  # Asymptotes at 0.7

        # Coupled coherence: initially boosted, then converges to product
        coupling_strength = 1.3 * np.exp(-t / 2)  # Coupling decays over time
        lambda_coupled = lambda_e * lambda_l * coupling_strength + lambda_e * lambda_l * (1 - coupling_strength)

        # Add noise
        lambda_e += np.random.normal(0, 0.02)
        lambda_l += np.random.normal(0, 0.02)
        lambda_coupled += np.random.normal(0, 0.02)

        lambda_e_trajectory.append(np.clip(lambda_e, 0, 1))
        lambda_l_trajectory.append(np.clip(lambda_l, 0, 1))
        lambda_coupled_trajectory.append(np.clip(lambda_coupled, 0, 1))

    return np.array(time_steps), np.array(lambda_e_trajectory), np.array(lambda_l_trajectory), np.array(lambda_coupled_trajectory)

def experiment_4_dialogue():
    """Test: Dialogue shows coupling signature"""
    print("\n" + "="*70)
    print("EXPERIMENT 4: Dialogue Entanglement")
    print("="*70)

    # Simulate 10 dialogue pairs
    coupling_boosts = []
    convergence_patterns = []

    for _ in range(10):
        t, lambda_e, lambda_l, lambda_coupled = simulate_coupled_coherence()

        # Early coupling boost (first 20% of dialogue)
        early_product = lambda_e[:10] * lambda_l[:10]
        early_coupled = lambda_coupled[:10]
        boost = np.mean(early_coupled) / (np.mean(early_product) + 1e-6)
        coupling_boosts.append(boost)

        # Late convergence (last 20% of dialogue)
        late_product = lambda_e[-10:] * lambda_l[-10:]
        late_coupled = lambda_coupled[-10:]
        convergence = np.mean(late_coupled) / (np.mean(late_product) + 1e-6)
        convergence_patterns.append(convergence)

    coupling_boosts = np.array(coupling_boosts)
    convergence_patterns = np.array(convergence_patterns)

    early_boost_mean = np.mean(coupling_boosts)
    late_convergence_mean = np.mean(convergence_patterns)

    print(f"Early coupling boost (λ_coupled / (λ_E * λ_L)): {early_boost_mean:.3f}")
    print(f"Late convergence: {late_convergence_mean:.3f}")
    print(f"Prediction: early boost > 1.0, late convergence ≈ 1.0")
    passed = early_boost_mean > 1.1 and 0.9 < late_convergence_mean < 1.1
    print(f"✓ PASSED" if passed else "✗ FAILED")

    # Plot one example trajectory
    t, lambda_e, lambda_l, lambda_coupled = simulate_coupled_coherence()

    plt.figure(figsize=(10, 6))
    plt.plot(t, lambda_e, label='Explainer (λ_E)', linewidth=2)
    plt.plot(t, lambda_l, label='Listener (λ_L)', linewidth=2)
    plt.plot(t, lambda_coupled, label='Coupled (λ_coupled)', linewidth=2)
    plt.plot(t, lambda_e * lambda_l, '--', label='Product (λ_E × λ_L)', linewidth=2, alpha=0.7)
    plt.xlabel('Time (minutes)')
    plt.ylabel('Coherence (λ)')
    plt.title('Experiment 4: Dialogue Entanglement (Example Trajectory)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('/Users/diegorincon/phronesis-papers/sim_exp4_dialogue.png', dpi=150, bbox_inches='tight')
    plt.close()

    return {'early_boost': early_boost_mean, 'late_convergence': late_convergence_mean, 'passed': passed}

# ============================================================================
# MAIN: Run all simulations
# ============================================================================

if __name__ == "__main__":
    results = {}

    print("\n" + "█" * 70)
    print("SIMULATING GRAMMAR-TO-COHERENCE EXPERIMENTS")
    print("█" * 70)

    results['exp1'] = experiment_1_eeg()
    results['exp2'] = experiment_2_reaction_time()
    results['exp3'] = experiment_3_ambiguity()
    results['exp4'] = experiment_4_dialogue()

    # Summary
    print("\n" + "█" * 70)
    print("SIMULATION SUMMARY")
    print("█" * 70)

    passed_count = sum(1 for r in results.values() if r['passed'])
    total_count = len(results)

    print(f"\nExperiment 1 (EEG Spectral Matching): {'✓ PASSED' if results['exp1']['passed'] else '✗ FAILED'}")
    print(f"  Correlation r = {results['exp1']['correlation']:.3f} (target: >0.65)")

    print(f"\nExperiment 2 (Reaction Time Power Law): {'✓ PASSED' if results['exp2']['passed'] else '✗ FAILED'}")
    print(f"  Power law exponent c = {results['exp2']['c_estimate']:.3f} (target: 0.8-1.2)")
    print(f"  R² = {results['exp2']['r_squared']:.3f} (target: >0.50)")

    print(f"\nExperiment 3 (Ambiguity & Degeneracy): {'✓ PASSED' if results['exp3']['passed'] else '✗ FAILED'}")
    print(f"  Ambiguous degeneracy: {results['exp3']['ambiguous_mean']:.3f}")
    print(f"  Unambiguous degeneracy: {results['exp3']['unambiguous_mean']:.3f}")

    print(f"\nExperiment 4 (Dialogue Entanglement): {'✓ PASSED' if results['exp4']['passed'] else '✗ FAILED'}")
    print(f"  Early coupling boost: {results['exp4']['early_boost']:.3f} (target: >1.1)")
    print(f"  Late convergence: {results['exp4']['late_convergence']:.3f} (target: ≈1.0)")

    print(f"\n{'█' * 70}")
    print(f"OVERALL: {passed_count}/{total_count} experiments passed")
    print(f"{'█' * 70}")

    # Save results to JSON
    with open('/Users/diegorincon/phronesis-papers/simulation_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: /Users/diegorincon/phronesis-papers/simulation_results.json")
    print(f"Plots saved to: /Users/diegorincon/phronesis-papers/sim_exp*.png")
