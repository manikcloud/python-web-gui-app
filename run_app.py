#!/usr/bin/env python3
"""
Script to run the Flask web application
"""

import os
import sys
import subprocess

def main():
    print("🚀 Starting Python Web GUI Application...")
    print("=" * 50)
    
    # Get the current directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"📁 Application Directory: {app_dir}")
    print(f"🐍 Python Version: {sys.version}")
    
    # Activate virtual environment and run the app
    venv_python = os.path.join(app_dir, 'venv', 'bin', 'python')
    app_file = os.path.join(app_dir, 'app.py')
    
    if os.path.exists(venv_python):
        print("✅ Virtual environment found")
        print("🌐 Starting Flask web server...")
        print()
        print("🔗 Access your application at:")
        print("   • Local: http://localhost:5000")
        print("   • Network: http://0.0.0.0:5000")
        print()
        print("📝 Features available:")
        print("   • Interactive name input")
        print("   • Message system")
        print("   • Text editor with save/load")
        print("   • File download functionality")
        print()
        print("⚠️  Press Ctrl+C to stop the server")
        print("=" * 50)
        
        # Run the Flask app
        subprocess.run([venv_python, app_file])
    else:
        print("❌ Virtual environment not found!")
        print("Please run: python3 -m venv venv && source venv/bin/activate && pip install Flask")

if __name__ == "__main__":
    main()
