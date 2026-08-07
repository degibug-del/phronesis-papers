#!/usr/bin/env python3
"""
AUTONOMOUS VALIDATION ENGINE

Monitors for data arrival, then automatically:
1. Runs analysis on all available subjects
2. Generates plots
3. Checks against prediction (r > 0.65)
4. Saves results
5. Reports findings

Runs continuously until success or timeout.
"""

import os
import sys
import time
import json
from pathlib import Path
import subprocess

# Add to path
sys.path.insert(0, str(Path(__file__).parent))

print("""
╔════════════════════════════════════════════════════════════════════════╗
║ AUTONOMOUS VALIDATION ENGINE                                          ║
║ Grammar-to-Coherence Real Data Validation                             ║
╚════════════════════════════════════════════════════════════════════════╝

This engine will:
1. Monitor ~/data/openneuro/ds002315/ for EEG file arrivals
2. Automatically run analysis when ≥3 subjects available
3. Generate correlation plots
4. Check against prediction (r > 0.65)
5. Report results in real-time

Status: ACTIVE
""")

DATA_DIR = Path.home() / "data" / "openneuro" / "ds002315"
OUTPUT_DIR = Path.home() / "phronesis-papers" / "validation-results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Monitor loop
print(f"\n📊 Monitoring: {DATA_DIR}")
print(f"📁 Output: {OUTPUT_DIR}\n")

start_time = time.time()
check_count = 0
last_file_count = 0

while True:
    check_count += 1
    elapsed = (time.time() - start_time) / 60

    # Count available EEG files
    eeg_files = list(DATA_DIR.glob("sub-*/eeg/*.fif"))
    file_count = len(eeg_files)

    # Count subjects with complete data
    subjects_with_data = len(set(f.parent.parent.name for f in eeg_files))

    if file_count > last_file_count:
        print(f"[{elapsed:6.1f} min] Data arrival: {file_count} files, {subjects_with_data} subjects")
        last_file_count = file_count

    # TRIGGER: Analyze when we have ≥3 subjects OR ≥1 subject after long wait
    trigger_condition = (subjects_with_data >= 3) or (elapsed > 30 and subjects_with_data >= 1)

    if trigger_condition and file_count > 0:
        print(f"\n{'='*70}")
        print(f"✅ TRIGGER CONDITION MET - LAUNCHING ANALYSIS")
        print(f"{'='*70}")
        print(f"Subjects available: {subjects_with_data}")
        print(f"EEG files: {file_count}")
        print(f"Running: python3 analyze_eeg_real.py --subjects 1-{subjects_with_data}")
        print()

        # Import and run analysis
        try:
            from analyze_eeg_real import ValidationPipeline

            pipeline = ValidationPipeline(str(DATA_DIR), str(OUTPUT_DIR))
            subject_range = f"1-{min(subjects_with_data, 50)}"
            results = pipeline.run(subject_range=subject_range)

            if results:
                print(f"\n{'='*70}")
                print("✅ VALIDATION COMPLETE")
                print(f"{'='*70}\n")

                # Check prediction
                correlation = results.get('correlation', 0)
                p_value = results.get('p_value', 1.0)
                n_epochs = results.get('n_epochs', 0)

                print(f"RESULTS:")
                print(f"  Correlation: r = {correlation:.4f}")
                print(f"  P-value: p = {p_value:.6f}")
                print(f"  N epochs: {n_epochs}")

                if correlation > 0.65 and p_value < 0.01:
                    print(f"\n✅ PREDICTION MET: Theory validated on real brains!")
                    print(f"\n   Next: Write manuscript + submit to Nature Neuroscience")
                elif correlation > 0.50 and p_value < 0.05:
                    print(f"\n⚠️  PARTIAL SUCCESS: Relationship present but weaker than predicted")
                    print(f"    Still publishable in mid-tier journal")
                else:
                    print(f"\n❌ NULL RESULT: No significant relationship found")
                    print(f"    Explore alternative metrics or refine theory")

                # Save execution report
                report = {
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "execution_time_minutes": round(elapsed, 1),
                    "subjects_analyzed": subjects_with_data,
                    "eeg_files_processed": file_count,
                    "results": results,
                    "success": correlation > 0.65 and p_value < 0.01
                }

                with open(OUTPUT_DIR / "execution_report.json", 'w') as f:
                    json.dump(report, f, indent=2)

                print(f"\n✅ Report saved: {OUTPUT_DIR / 'execution_report.json'}")
                print(f"✅ Plot saved: {OUTPUT_DIR / 'validation_plot.png'}")
                print(f"✅ Results saved: {OUTPUT_DIR / 'validation_results.json'}")

                # Exit on completion
                print(f"\n🎯 VALIDATION ENGINE: MISSION COMPLETE")
                sys.exit(0)

        except Exception as e:
            print(f"\n❌ Analysis failed: {e}")
            import traceback
            traceback.print_exc()
            print(f"\nRetrying in 60 seconds...\n")
            time.sleep(60)
            continue

    # Check timeout (12 hours)
    if elapsed > 720:
        print(f"\n{'='*70}")
        print(f"⏱️  TIMEOUT AFTER 12 HOURS")
        print(f"{'='*70}")
        print(f"\nData status:")
        print(f"  Subjects downloaded: {subjects_with_data}")
        print(f"  EEG files: {file_count}")
        print(f"\nIf data hasn't arrived, try:")
        print(f"  1. git clone https://github.com/OpenNeuroDatasets/ds002315.git")
        print(f"  2. Manual download from https://openneuro.org/datasets/ds002315")
        print(f"  3. Contact dataset authors for direct access")
        sys.exit(1)

    # Wait before next check
    time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    pass
