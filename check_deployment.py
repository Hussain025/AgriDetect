"""
Deployment Readiness Checker for AgroDetect AI
Run this script before deploying to Streamlit Cloud
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, required=True):
    """Check if a file exists"""
    exists = Path(filepath).exists()
    status = "✅" if exists else ("❌" if required else "⚠️")
    req_text = "(required)" if required else "(optional)"
    print(f"{status} {filepath} {req_text}")
    return exists

def check_directory_exists(dirpath, required=True):
    """Check if a directory exists"""
    exists = Path(dirpath).is_dir()
    status = "✅" if exists else ("❌" if required else "⚠️")
    req_text = "(required)" if required else "(optional)"
    print(f"{status} {dirpath}/ {req_text}")
    return exists

def check_requirements():
    """Check requirements.txt"""
    print("\n📦 Checking requirements.txt...")
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found!")
        return False
    
    with open("requirements.txt", "r") as f:
        content = f.read()
    
    required_packages = [
        "streamlit",
        "google-generativeai",
        "SpeechRecognition",
        "gTTS",
        "Pillow",
        "torch",
        "transformers"
    ]
    
    all_found = True
    for package in required_packages:
        if package.lower() in content.lower():
            print(f"✅ {package}")
        else:
            print(f"❌ {package} - MISSING!")
            all_found = False
    
    return all_found

def check_secrets_template():
    """Check secrets template"""
    print("\n🔐 Checking secrets configuration...")
    template_exists = check_file_exists(".streamlit/secrets.toml.template", required=True)
    secrets_exists = check_file_exists(".streamlit/secrets.toml", required=False)
    
    if secrets_exists:
        print("⚠️  WARNING: secrets.toml exists locally")
        print("   Make sure it's in .gitignore!")
    
    return template_exists

def check_gitignore():
    """Check .gitignore"""
    print("\n🚫 Checking .gitignore...")
    if not Path(".gitignore").exists():
        print("❌ .gitignore not found!")
        return False
    
    with open(".gitignore", "r") as f:
        content = f.read()
    
    if "secrets.toml" in content:
        print("✅ secrets.toml is gitignored")
        return True
    else:
        print("❌ secrets.toml NOT in .gitignore!")
        print("   Add this line: .streamlit/secrets.toml")
        return False

def check_imports():
    """Check for problematic imports"""
    print("\n🔍 Checking for problematic imports...")
    
    problematic = []
    
    # Check all Python files
    for py_file in Path(".").rglob("*.py"):
        if "venv" in str(py_file) or "__pycache__" in str(py_file):
            continue
        
        with open(py_file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        # Check for OS-specific imports
        if "import win32" in content or "from win32" in content:
            problematic.append((py_file, "win32 (Windows-specific)"))
        
        # Check for absolute paths
        if "C:\\" in content or "D:\\" in content:
            problematic.append((py_file, "Absolute Windows path"))
    
    if problematic:
        print("⚠️  Found potential issues:")
        for file, issue in problematic:
            print(f"   {file}: {issue}")
        return False
    else:
        print("✅ No problematic imports found")
        return True

def check_ml_integration():
    """Check ML integration"""
    print("\n🤖 Checking ML integration...")
    
    ml_ok = True
    
    # Check ML connector exists
    if check_file_exists("components/ml_model_connector.py", required=True):
        print("✅ ML model connector found")
    else:
        print("❌ ML model connector missing!")
        ml_ok = False
    
    # Check database folder
    if check_directory_exists("AgriDetect-main", required=False):
        print("✅ Database folder found")
    else:
        print("⚠️  Database folder not found (OK if using Hugging Face Hub)")
    
    # Check ML connector imports
    try:
        from components.ml_model_connector import (
            load_plant_disease_model,
            predict_disease,
            get_disease_recommendations
        )
        print("✅ ML connector imports working")
    except Exception as e:
        print(f"❌ ML connector import failed: {e}")
        ml_ok = False
    
    return ml_ok

def main():
    """Main deployment check"""
    print("=" * 60)
    print("🚀 AgroDetect AI - Deployment Readiness Check")
    print("=" * 60)
    
    # Check project structure
    print("\n📁 Checking project structure...")
    structure_ok = True
    structure_ok &= check_file_exists("app.py", required=True)
    structure_ok &= check_file_exists("requirements.txt", required=True)
    structure_ok &= check_file_exists("README.md", required=True)
    structure_ok &= check_file_exists(".streamlit/config.toml", required=True)
    structure_ok &= check_directory_exists("pages", required=True)
    structure_ok &= check_directory_exists("components", required=True)
    structure_ok &= check_directory_exists("assets", required=False)
    
    # Check requirements
    requirements_ok = check_requirements()
    
    # Check secrets
    secrets_ok = check_secrets_template()
    
    # Check gitignore
    gitignore_ok = check_gitignore()
    
    # Check imports
    imports_ok = check_imports()
    
    # Check ML integration
    ml_ok = check_ml_integration()
    
    # Final summary
    print("\n" + "=" * 60)
    print("📊 DEPLOYMENT READINESS SUMMARY")
    print("=" * 60)
    
    all_checks = [
        ("Project Structure", structure_ok),
        ("Requirements", requirements_ok),
        ("Secrets Configuration", secrets_ok),
        (".gitignore", gitignore_ok),
        ("Code Compatibility", imports_ok),
        ("ML Integration", ml_ok)
    ]
    
    for check_name, passed in all_checks:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {check_name}")
    
    all_passed = all(passed for _, passed in all_checks)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL CHECKS PASSED!")
        print("✅ Your app is ready for Streamlit Cloud deployment!")
        print("\nNext steps:")
        print("1. Push code to GitHub")
        print("2. Deploy on Streamlit Cloud")
        print("3. Add secrets in dashboard")
        print("4. Test live app")
        print("\n💡 Note: ML model will download from Hugging Face Hub on first use")
    else:
        print("⚠️  SOME CHECKS FAILED")
        print("❌ Please fix the issues above before deploying")
        print("\nSee DEPLOYMENT_GUIDE.md for detailed instructions")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
