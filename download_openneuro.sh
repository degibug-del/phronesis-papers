#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════════════╗"
echo "║ DOWNLOADING ds002315: UCL Sentence Comprehension EEG                  ║"
echo "╚════════════════════════════════════════════════════════════════════════╝"
echo ""
echo "Dataset info:"
echo "  - 50 subjects"
echo "  - 240 sentences (varying syntactic complexity)"
echo "  - 64-channel EEG (10-20 placement)"
echo "  - 1000 Hz sampling rate"
echo "  - Event markers for sentence onset"
echo ""

DATA_DIR="$HOME/data/openneuro/ds002315"
mkdir -p "$DATA_DIR"

echo "Downloading minimal dataset (first 2 subjects, ~1.5 GB)..."
echo ""

# Option 1: Using AWS CLI (if available)
if command -v aws &> /dev/null; then
    echo "Using AWS CLI to sync from OpenNeuro S3..."
    aws s3 sync --no-sign-request \
        s3://openneuro.org/ds002315/sub-01 "$DATA_DIR/sub-01" \
        --exclude "*.nii.gz" --exclude "derivatives/*"
    
    aws s3 sync --no-sign-request \
        s3://openneuro.org/ds002315/sub-02 "$DATA_DIR/sub-02" \
        --exclude "*.nii.gz" --exclude "derivatives/*"
else
    echo "AWS CLI not found. Use one of these alternatives:"
    echo ""
    echo "1. Install AWS CLI:"
    echo "   pip install awscli"
    echo ""
    echo "2. Download via HTTPS:"
    echo "   curl -X GET 'https://openneuro.org/crn/datasets/ds002315/snapshots/7.0.1/files' | grep '.fif'"
    echo ""
    echo "3. Use Datalad (recommended):"
    echo "   pip install datalad"
    echo "   datalad clone https://github.com/OpenNeuroDatasets/ds002315.git"
fi

echo ""
echo "Dataset will be saved to: $DATA_DIR"
echo ""
