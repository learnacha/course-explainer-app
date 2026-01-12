#!/usr/bin/env python3
"""
Start Flask application and prepare for visual verification.
This ensures the app is running before Playwright takes screenshots.
"""

import subprocess
import time
import sys
import os
import requests

def is_flask_running():
    """Check if Flask server is running"""
    try:
        requests.get('http://127.0.0.1:5000', timeout=2)
        return True
    except requests.exceptions.RequestException:
        return False

def main():
    """Start Flask server if needed and guide through verification"""
    
    # Check if we're in the right directory
    if not os.path.exists('src/app.py'):
        print("❌ Error: src/app.py not found!")
        print("Make sure you run this from the project root directory.")
        sys.exit(1)

    # Check if Flask is already running
    if is_flask_running():
        print("✅ Flask server is already running!")
    else:
        print("🚀 Starting Flask development server...")

        try:
            proc = subprocess.Popen(
                [sys.executable, "src/app.py"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        
            # Wait for server to initialize
            time.sleep(3)
        
            if is_flask_running():
                print("✅ Flask server started successfully!")
            else:
                print("❌ Failed to start Flask server.")
                sys.exit(1)    
            
        except Exception as e:
            print(f"❌ Error starting Flask: {e}")
            sys.exit(1)

    print("-"*50)
    print("👉 Now you can run your Playwright visual verification script.")
    print("Navigate to http://127.0.0.1:5000")
    print("Take a screenshot and save as test-output/before-design.png")
    print("-"*50)

if __name__ == "__main__":
    main()