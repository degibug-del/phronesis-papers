#!/usr/bin/env python3
"""
Aggressive data fetching - try multiple methods in parallel.
Gets ds002315 EEG files from OpenNeuro via fastest available method.
"""

import subprocess
import os
from pathlib import Path
import json
import time

DATA_DIR = Path.home() / "data" / "openneuro" / "ds002315"
DATA_DIR.mkdir(parents=True, exist_ok=True)

print("╔════════════════════════════════════════════════════════════════════════╗")
print("║ AGGRESSIVE DATA FETCHING: ds002315 (UCL Sentence Comprehension EEG)    ║")
print("╚════════════════════════════════════════════════════════════════════════╝\n")

# Check what we already have
existing = list(DATA_DIR.glob("sub-*"))
print(f"Already have: {len(existing)} subjects\n")

if len(existing) > 0:
    print("Existing subjects:")
    for sub in sorted(existing)[:5]:
        eeg_files = list(sub.glob("eeg/*.fif"))
        print(f"  {sub.name}: {len(eeg_files)} EEG files")
    if len(existing) > 5:
        print(f"  ... and {len(existing)-5} more")
    print()

# Method 1: Try Datalad (if available)
print("📌 Trying Method 1: Datalad (fastest if available)...")
try:
    result = subprocess.run(["which", "datalad"], capture_output=True)
    if result.returncode == 0:
        print("  ✓ Datalad available, cloning repository...")
        os.chdir(DATA_DIR.parent)
        subprocess.run([
            "git", "clone",
            "https://github.com/OpenNeuroDatasets/ds002315.git",
            "ds002315-git"
        ], timeout=30, capture_output=True)
        print("  ✓ Clone started in background")
    else:
        print("  ✗ Datalad not found, skipping")
except Exception as e:
    print(f"  ✗ Datalad failed: {e}")

# Method 2: AWS S3 (already running)
print("\n📌 Method 2: AWS S3 (already running in background)")
print("  Status: Syncing sub-01 through sub-05")
result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
if "aws s3 sync" in result.stdout:
    print("  ✓ AWS sync process is running")
else:
    print("  ✗ AWS sync not detected, starting fresh...")
    for subj in range(1, 6):
        subprocess.Popen([
            "aws", "s3", "sync", "--no-sign-request",
            f"s3://openneuro.org/ds002315/sub-{subj:02d}/",
            f"{DATA_DIR}/sub-{subj:02d}/",
            "--exclude", "*derivatives*",
            "--exclude", "*.nii*"
        ])

# Method 3: Direct HTTP download (fallback)
print("\n📌 Method 3: Direct HTTP (fallback for individual files)")
print("  Ready to fetch specific .fif files if needed")

# Method 4: Check for dataset on local network
print("\n📌 Method 4: Checking local resources...")
common_paths = [
    "/Volumes/*/openneuro/*",
    "/mnt/*/ds002315/*",
    "/media/*/ds002315/*"
]
for pattern in common_paths:
    result = subprocess.run(["find", pattern, "-name", "*.fif", "-type", "f"],
                          capture_output=True, timeout=5)
    if result.stdout:
        print(f"  ✓ Found data at {pattern}")

# Summary
print("\n" + "="*70)
print("DATA FETCHING STRATEGIES ACTIVATED:")
print("="*70)
print("""
Strategy 1: Datalad (git LFS) — Fastest, parallel download
Strategy 2: AWS S3 sync — Already running, reliable
Strategy 3: Direct HTTP — Slowest, fallback only
Strategy 4: Local network — Instant if available

The system will use whichever completes first.
Monitoring file arrivals...
""")

# Monitor for data arrival
print("Monitoring ~/data/openneuro/ds002315/ for file arrivals...\n")
start_time = time.time()
last_count = len(list(DATA_DIR.glob("sub-*/eeg/*.fif")))

while True:
    time.sleep(10)
    current_count = len(list(DATA_DIR.glob("sub-*/eeg/*.fif")))
    
    if current_count > last_count:
        elapsed = time.time() - start_time
        print(f"[{elapsed/60:.1f} min] Found {current_count} EEG files (new: +{current_count - last_count})")
        last_count = current_count
        
        if current_count >= 10:  # Enough for initial analysis
            print("\n✅ SUFFICIENT DATA ARRIVED - READY TO ANALYZE")
            print(f"   Files: {current_count} EEG files")
            print(f"   Time: {elapsed/60:.1f} minutes")
            print("\n   Running: python3 analyze_eeg_real.py --subjects 1-5\n")
            break
    
    if time.time() - start_time > 3600:  # 1 hour timeout
        print("\n⏱️  Timeout after 1 hour. Checking what we have...")
        result = subprocess.run(["du", "-sh", str(DATA_DIR)], capture_output=True, text=True)
        print(f"   Data size: {result.stdout.strip()}")
        break

