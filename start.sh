#!/bin/bash

# DevTechAI WebApp v2.0 Startup Script
# This script starts the development server for the webapp

echo "🚀 Starting DevTechAI WebApp v2.0..."
echo "=================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 to run the server."
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ index.html not found. Please run this script from the project root directory."
    exit 1
fi

# Check if assets directory exists
if [ ! -d "assets" ]; then
    echo "❌ Assets directory not found. Please ensure assets are copied from the theme."
    exit 1
fi

# Make server.py executable
chmod +x server.py

echo "✅ All checks passed!"
echo "🌐 Starting development server..."
echo ""

# Start the server
python3 server.py
