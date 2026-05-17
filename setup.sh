#!/bin/bash

# Setup script for fastmcp-http-basics with fastmcp
# This script creates a virtual environment and installs fastmcp

set -e  # Exit on error

echo "==================================="
echo "FastMCP Setup Script"
echo "==================================="
echo ""

# Step 1: Create virtual environment
echo "Step 1: Creating Python virtual environment..."
python3 -m venv venv
echo "✓ Virtual environment created"
echo ""

# Step 2: Activate virtual environment
echo "Step 2: Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Step 3: Install required packages
echo "Step 3: Installing required packages..."
pip install --upgrade pip
pip install fastmcp
pip install tavily
echo "✓ All packages installed (fastmcp, tavily)"
echo ""

# Step 4: Verify installation
echo "Step 4: Verifying installation..."
python -c "import fastmcp; print(f'✓ fastmcp version: {fastmcp.__version__}')"
echo ""

echo "==================================="
echo "Setup completed successfully!"
echo "==================================="
echo ""
echo "To activate the environment in future sessions, run:"
echo "  source venv/bin/activate"
echo ""
