#!/usr/bin/env python3
"""AccuTester - Entry point for the application."""
import sys
import os

# Add src directory to path so imports work correctly
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)

from main import main

if __name__ == "__main__":
    main()
