"""
Automated upload script
"""

from datasets import load_from_disk
from huggingface_hub import login
import sys
import os

print("=" * 60)
print("Upload Dataset to Hugging Face Hub")
print("=" * 60)

# Login with provided token
token = os.getenv("HF_TOKEN")
if not token:
    print("\n❌ Error: HF_TOKEN environment variable not set")
    print("\nSet it with: export HF_TOKEN=your_token_here")
    sys.exit(1)

print("\n🔑 Logging in to Hugging Face...")
try:
    login(token=token)
    print("✅ Login successful!")
except Exception as e:
    print(f"❌ Login failed: {e}")
    sys.exit(1)

# Get username
print("\n👤 Enter your Hugging Face username")
username = input("Your HF username: ").strip()

if not username:
    print("❌ No username provided. Exiting.")
    sys.exit(1)

dataset_name = f"{username}/plant-disease-classification"

# Load dataset
print("\n📂 Loading dataset from disk...")
try:
    dataset = load_from_disk('hf_dataset')
    print(f"✅ Dataset loaded!")
    print(f"\n{dataset}")
except Exception as e:
    print(f"❌ Failed to load dataset: {e}")
    sys.exit(1)

# Upload
print(f"\n📤 Uploading to {dataset_name}...")
print("This may take a few minutes...")

try:
    dataset.push_to_hub(dataset_name, private=False)
    print(f"\n✅ SUCCESS! Dataset uploaded!")
    print(f"\n🎉 Your dataset is now available at:")
    print(f"   https://huggingface.co/datasets/{dataset_name}")
    print()
    print("=" * 60)
    print("NEXT STEPS FOR AUTOTRAIN")
    print("=" * 60)
    print("1. Visit your dataset page (URL above)")
    print("2. Go to: https://huggingface.co/autotrain")
    print("3. Create new project → Image Classification")
    print(f"4. Select dataset: {dataset_name}")
    print("5. Configure training settings")
    print("6. Start training!")
    print()
    print("💡 Save the dataset URL for your report!")
    
except Exception as e:
    print(f"\n❌ Upload failed: {e}")
    print("\nTroubleshooting:")
    print("- Check your internet connection")
    print("- Verify your token has WRITE access")
    sys.exit(1)
