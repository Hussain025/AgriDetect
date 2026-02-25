"""
Fully automated upload - just provide username as argument
Usage: python auto_upload.py YOUR_USERNAME
"""

from datasets import load_from_disk
from huggingface_hub import login
import sys
import os

print("=" * 60)
print("Upload Dataset to Hugging Face Hub")
print("=" * 60)

# Check for username argument
if len(sys.argv) < 2:
    print("\n❌ Usage: python auto_upload.py YOUR_USERNAME")
    print("\nExample: python auto_upload.py john_doe")
    sys.exit(1)

username = sys.argv[1]
token = os.getenv("HF_TOKEN")
if not token:
    print("\n❌ Error: HF_TOKEN environment variable not set")
    print("\nSet it with: export HF_TOKEN=your_token_here")
    sys.exit(1)
dataset_name = f"{username}/plant-disease-classification"

# Login
print("\n🔑 Logging in to Hugging Face...")
try:
    login(token=token)
    print("✅ Login successful!")
except Exception as e:
    print(f"❌ Login failed: {e}")
    sys.exit(1)

# Load dataset
print("\n📂 Loading dataset from disk...")
try:
    dataset = load_from_disk('hf_dataset')
    print(f"✅ Dataset loaded!")
    print(f"\nDataset Info:")
    print(f"  Train: {len(dataset['train'])} images")
    print(f"  Validation: {len(dataset['validation'])} images")
    print(f"  Test: {len(dataset['test'])} images")
    print(f"  Classes: {len(dataset['train'].features['label'].names)}")
except Exception as e:
    print(f"❌ Failed to load dataset: {e}")
    sys.exit(1)

# Upload
print(f"\n📤 Uploading to: {dataset_name}")
print("⏳ This may take 2-5 minutes depending on your connection...")
print()

try:
    dataset.push_to_hub(dataset_name, private=False)
    
    print("\n" + "=" * 60)
    print("✅ SUCCESS! DATASET UPLOADED!")
    print("=" * 60)
    print(f"\n🎉 Your dataset is live at:")
    print(f"   https://huggingface.co/datasets/{dataset_name}")
    print()
    print("=" * 60)
    print("📋 NEXT STEPS FOR AUTOTRAIN")
    print("=" * 60)
    print("\n1. Open AutoTrain:")
    print("   https://huggingface.co/autotrain")
    print()
    print("2. Click 'New Project' → 'Image Classification'")
    print()
    print("3. In dataset selection:")
    print(f"   - Choose 'Use existing dataset'")
    print(f"   - Search for: {dataset_name}")
    print(f"   - Select it")
    print()
    print("4. Configure training:")
    print("   - Model: ResNet-50 or EfficientNet-B0")
    print("   - Epochs: 10-20")
    print("   - Batch size: 16 or 32")
    print("   - Learning rate: Auto")
    print()
    print("5. Optional: Enable Weights & Biases integration")
    print()
    print("6. Click 'Start Training'")
    print()
    print("=" * 60)
    print("📸 FOR YOUR REPORT - SCREENSHOT:")
    print("=" * 60)
    print(f"✓ Dataset URL: https://huggingface.co/datasets/{dataset_name}")
    print("✓ AutoTrain configuration page")
    print("✓ Training job URL (after starting)")
    print()
    
except Exception as e:
    print(f"\n❌ Upload failed: {e}")
    print("\nPossible issues:")
    print("- Internet connection interrupted")
    print("- Token doesn't have write access")
    print("- Dataset name already exists")
    sys.exit(1)
