#!/bin/bash
set -e

echo "╔════════════════════════════════════════════════════════════════════════╗"
echo "║ GRAMMAR-TO-COHERENCE: REAL DATA VALIDATION - STARTING NOW            ║"
echo "╚════════════════════════════════════════════════════════════════════════╝"
echo ""

DATA_DIR="$HOME/data/openneuro/ds002315"
mkdir -p "$DATA_DIR"
cd "$DATA_DIR"

echo "📥 STEP 1: Downloading ds002315 (UCL Sentence Comprehension EEG)"
echo "   Target: 50 subjects, 240 sentences, 64-channel EEG"
echo "   Size: ~20-30 GB (downloading first 5 subjects as test)"
echo ""

# Check if AWS CLI is available
if ! command -v aws &> /dev/null; then
    echo "⚠️  AWS CLI not found. Installing..."
    pip install -q awscli
fi

echo "Starting download for sub-01 through sub-05..."
for subj in 01 02 03 04 05; do
    echo ""
    echo "Downloading sub-$subj..."
    aws s3 sync --no-sign-request \
        --exclude "*derivatives*" \
        --exclude "*.nii*" \
        s3://openneuro.org/ds002315/sub-$subj/ \
        "$DATA_DIR/sub-$subj/" || echo "Note: sub-$subj may already exist or download partial"
done

echo ""
echo "✅ Download complete (or in progress)"
echo "   Data location: $DATA_DIR"
echo ""
ls -lh "$DATA_DIR"/ 2>/dev/null | head -10

