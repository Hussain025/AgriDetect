"""
Simple script to login and upload dataset to Hugging Face Hub
"""

from datasets import load_from_disk
from huggingface_hub import login
import sys

print("=" * 60)
print("Upload Dataset to Hugging Face Hub")
print("=" * 60)

# Step 1: Login
print("\n🔑 Step 1: Login to Hugging Face")
print("-" * 60)
print("You need a Hugging Face token with WRITE access.")
print("Get it from: https://huggingface.co/settings/tokens")
print()

token = input("Paste your HF token here (starts with hf_...): ").strip()

if not token:
    print("❌ No token provided. Exiting.")
    sys.exit(1)

try:
    login(token=token)
    print("✅ Login successful!")
except Exception as e:
    print(f"❌ Login failed: {e}")
    sys.exit(1)

# Step 2: Get username
print("\n👤 Step 2: Enter your Hugging Face username")
print("-" * 60)
username = input("Your HF username: ").strip()

if not username:
    print("❌ No username provided. Exiting.")
    sys.exit(1)

dataset_name = f"{username}/plant-disease-classification"

# Step 3: Load dataset
print("\n📂 Step 3: Loading dataset from disk...")
print("-" * 60)
try:
    dataset = load_from_disk('hf_dataset')
    print(f"✅ Dataset loaded successfully!")
    print(f"\n{dataset}")
except Exception as e:
    print(f"❌ Failed to load dataset: {e}")
    sys.exit(1)

# Step 4: Upload
print(f"\n📤 Step 4: Uploading to {dataset_name}...")
print("-" * 60)
print("This may take a few minutes...")

try:
    dataset.push_to_hub(dataset_name, private=False)
    print(f"\n✅ SUCCESS! Dataset uploaded!")
    print(f"\n🎉 Your dataset is now available at:")
    print(f"   https://huggingface.co/datasets/{dataset_name}")
    print()
    print("=" * 60)
    print("NEXT STEPS")
    print("=" * 60)
    print("1. Visit your dataset page (URL above)")
    print("2. Go to: https://huggingface.co/autotrain")
    print("3. Create new project → Image Classification")
    print(f"4. Select dataset: {dataset_name}")
    print("5. Configure and start training!")
    print()
    print("💡 Save the dataset URL for your report!")
    
except Exception as e:
    print(f"\n❌ Upload failed: {e}")
    print("\nTroubleshooting:")
    print("- Check your internet connection")
    print("- Verify your token has WRITE access")
    print("- Try again in a few minutes")
    sys.exit(1)
