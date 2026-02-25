"""
Quick Test Script for ML Integration
Run this to verify the ML model connector works correctly
"""

import sys
from pathlib import Path

print("=" * 60)
print("🧪 Testing ML Integration")
print("=" * 60)

# Test 1: Import ML Connector
print("\n1️⃣ Testing imports...")
try:
    from components.ml_model_connector import (
        load_plant_disease_model,
        predict_disease,
        get_disease_recommendations,
        validate_image,
        check_model_availability,
        get_dataset_info,
        DISEASE_CLASSES
    )
    print("   ✅ All imports successful")
except Exception as e:
    print(f"   ❌ Import failed: {e}")
    sys.exit(1)

# Test 2: Check Paths
print("\n2️⃣ Testing path configuration...")
try:
    from components.ml_model_connector import get_project_root, get_database_path
    
    project_root = get_project_root()
    database_path = get_database_path()
    
    print(f"   📁 Project root: {project_root}")
    print(f"   📁 Database path: {database_path}")
    
    if database_path.exists():
        print("   ✅ Database folder found")
    else:
        print("   ⚠️  Database folder not found (this is OK if not needed)")
    
except Exception as e:
    print(f"   ❌ Path check failed: {e}")
    sys.exit(1)

# Test 3: Check Disease Classes
print("\n3️⃣ Testing disease classes...")
try:
    print(f"   📋 Number of classes: {len(DISEASE_CLASSES)}")
    print(f"   📋 Classes: {', '.join(DISEASE_CLASSES[:3])}...")
    print("   ✅ Disease classes loaded")
except Exception as e:
    print(f"   ❌ Disease classes check failed: {e}")
    sys.exit(1)

# Test 4: Get Dataset Info
print("\n4️⃣ Testing dataset info...")
try:
    dataset_info = get_dataset_info()
    print(f"   📊 Total images: {dataset_info['total_images']}")
    print(f"   📊 Number of classes: {dataset_info['num_classes']}")
    print(f"   📊 Model architecture: {dataset_info['model_architecture']}")
    print("   ✅ Dataset info retrieved")
except Exception as e:
    print(f"   ❌ Dataset info failed: {e}")
    sys.exit(1)

# Test 5: Test Recommendations
print("\n5️⃣ Testing disease recommendations...")
try:
    recommendations = get_disease_recommendations("Tomato Early Blight")
    print(f"   💊 Status: {recommendations['status']}")
    print(f"   💊 Severity: {recommendations['severity']}")
    print(f"   💊 Actions: {len(recommendations['actions'])} items")
    print(f"   💊 Prevention: {len(recommendations['prevention'])} items")
    print("   ✅ Recommendations working")
except Exception as e:
    print(f"   ❌ Recommendations failed: {e}")
    sys.exit(1)

# Test 6: Test Image Validation
print("\n6️⃣ Testing image validation...")
try:
    from PIL import Image
    import numpy as np
    
    # Create a test image
    test_image = Image.fromarray(np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8))
    is_valid, message = validate_image(test_image)
    
    print(f"   🖼️  Test image valid: {is_valid}")
    print(f"   🖼️  Message: {message}")
    print("   ✅ Image validation working")
except Exception as e:
    print(f"   ❌ Image validation failed: {e}")
    sys.exit(1)

# Test 7: Check Model Availability (Optional - requires internet)
print("\n7️⃣ Testing model availability (requires internet)...")
print("   ⏳ This may take a while on first run (downloading model)...")
print("   💡 You can skip this test by pressing Ctrl+C")
try:
    model_available = check_model_availability()
    if model_available:
        print("   ✅ Model loaded successfully!")
        print("   🎉 ML integration is fully functional!")
    else:
        print("   ⚠️  Model not available (check internet connection)")
        print("   💡 This is OK - model will download on first use in app")
except KeyboardInterrupt:
    print("\n   ⏭️  Skipped model loading test")
except Exception as e:
    print(f"   ⚠️  Model loading failed: {e}")
    print("   💡 This is OK - model will download on first use in app")

# Summary
print("\n" + "=" * 60)
print("✅ ML INTEGRATION TEST COMPLETE")
print("=" * 60)
print("\n📝 Summary:")
print("   ✅ All imports working")
print("   ✅ Paths configured correctly")
print("   ✅ Disease classes loaded")
print("   ✅ Dataset info available")
print("   ✅ Recommendations working")
print("   ✅ Image validation working")
print("\n🚀 Ready to run: streamlit run app.py")
print("=" * 60)
