#!/bin/bash

# Create product development structure for all 4 lines

BASE_DIR="$HOME/phronesis-products"
mkdir -p "$BASE_DIR"

echo "🏗️ Creating product development structure...\n"

# Product 1: Coherence Monitor
echo "📱 Product 1: Coherence Monitor"
mkdir -p "$BASE_DIR/coherence-monitor"/{app,engine,tests,docs}
touch "$BASE_DIR/coherence-monitor"/{README.md,package.json,requirements.txt}

# Product 2: Clarity OS
echo "💻 Product 2: Clarity OS"
mkdir -p "$BASE_DIR/clarity-os"/{browser-ext,web-app,core,tests,docs}
touch "$BASE_DIR/clarity-os"/{README.md,package.json,manifest.json}

# Product 3: Logic Engine
echo "🧠 Product 3: Pure Logic AI Engine"
mkdir -p "$BASE_DIR/logic-engine"/{api,core,examples,tests,docs}
touch "$BASE_DIR/logic-engine"/{README.md,requirements.txt,setup.py}

# Product 4: Dialogue Coupling
echo "🤝 Product 4: Dialogue Coupling Platform"
mkdir -p "$BASE_DIR/dialogue-platform"/{app,backend,analysis,tests,docs}
touch "$BASE_DIR/dialogue-platform"/{README.md,package.json,requirements.txt}

# Shared resources
echo "📚 Shared Resources"
mkdir -p "$BASE_DIR/shared"/{icm-engine,theory,datasets,benchmarks}
touch "$BASE_DIR/shared"/{README.md,requirements.txt}

echo ""
echo "✅ Project structure created at: $BASE_DIR"
echo ""
echo "Directory tree:"
tree -L 2 "$BASE_DIR" 2>/dev/null || find "$BASE_DIR" -type d | head -20

