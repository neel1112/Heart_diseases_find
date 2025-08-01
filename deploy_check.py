#!/usr/bin/env python3
"""
Deployment check script for Heart Disease Prediction Django project
This script verifies that all dependencies and settings are compatible
"""

import sys
import os

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 8:
        print("✓ Python version is compatible")
        return True
    else:
        print("✗ Python version should be 3.8 or higher")
        return False

def check_django_settings():
    """Check Django settings compatibility"""
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_desease.settings')
        import django
        django.setup()
        print("✓ Django settings are compatible")
        return True
    except Exception as e:
        print(f"✗ Django settings error: {e}")
        return False

def check_models():
    """Check if models are compatible"""
    try:
        from health.models import Patient, Doctor, Admin_Helath_CSV, Search_Data, Appointment, Feedback
        print("✓ All models are compatible")
        return True
    except Exception as e:
        print(f"✗ Models error: {e}")
        return False

def main():
    print("=== Deployment Compatibility Check ===")
    
    checks = [
        check_python_version(),
        check_django_settings(),
        check_models(),
    ]
    
    print("\n=== Summary ===")
    if all(checks):
        print("✓ All checks passed! Ready for deployment.")
        return 0
    else:
        print("✗ Some checks failed. Please fix the issues before deploying.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 
