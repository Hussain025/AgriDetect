"""
Upload dataset directly to Hugging Face Hub
This bypasses AutoTrain UI issues and creates a dataset you can use with AutoTrain
"""

import os
from pathlib import Path
from PIL import Image

print("=" * 60)
print("Upload Dataset to Hugging Face Hub")
print("=" * 60)

# Check if datasets library is installed
try:
    from datasets import Dataset, DatasetDict, Image as HFImage, Features, ClassLabel
    print("✓ datasets library found")
except ImportError:
    print("\n⚠️  'datasets' library not installed")
    print("\nInstall it with:")
    print("  pip install datasets huggingface-hub")
    print("\nThen run this script again.")
    exit(1)

# Configuration
source_dir = "roboflow_dataset"
dataset_name = "plant-disease-classification"  # Change this to your HF username/dataset-name

print(f"\n📁 Loading images from: {source_dir}")

# Collect all data
def load_split_data(split_name):
    split_path = os.path.join(source_dir, split_name)
    
    if not os.path.exists(split_path):
        return None
    
    data = {'image': [], 'label': []}
    
    classes = sorted([d for d in os.listdir(split_path) 
                     if os.path.isdir(os.path.join(split_path, d))])
    
    print(f"\n  Processing {split_name}...")
    for class_name in classes:
        class_path = os.path.join(split_path, class_name)
        images = [f for f in os.listdir(class_path) 
                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        for img_name in images:
            img_path = os.path.join(class_path, img_name)
            data['image'].append(img_path)
            data['label'].append(class_name)
        
        print(f"    ✓ {class_name}: {len(images)} images")
    
    return data, classes

# Load all splits
train_data, class_names = load_split_data('train')
valid_data, _ = load_split_data('valid')
test_data, _ = load_split_data('test')

if not train_data:
    print("\n❌ Error: No training data found!")
    exit(1)

print(f"\n📊 Dataset Statistics:")
print(f"  Classes: {len(class_names)}")
print(f"  Train: {len(train_data['image'])} images")
if valid_data:
    print(f"  Valid: {len(valid_data['image'])} images")
if test_data:
    print(f"  Test: {len(test_data['image'])} images")

# Create datasets
print("\n🔨 Creating Hugging Face datasets...")

features = Features({
    'image': HFImage(),
    'label': ClassLabel(names=class_names)
})

train_dataset = Dataset.from_dict(train_data, features=features)

dataset_dict = {'train': train_dataset}
if valid_data:
    valid_dataset = Dataset.from_dict(valid_data, features=features)
    dataset_dict['validation'] = valid_dataset
if test_data:
    test_dataset = Dataset.from_dict(test_data, features=features)
    dataset_dict['test'] = test_dataset

dataset = DatasetDict(dataset_dict)

print("✓ Datasets created")
print(f"\n{dataset}")

# Save locally first
print("\n💾 Saving dataset locally...")
local_save_path = "hf_dataset"
dataset.save_to_disk(local_save_path)
print(f"✓ Saved to: {local_save_path}")

print("\n" + "=" * 60)
print("📤 READY TO UPLOAD TO HUGGING FACE HUB")
print("=" * 60)
print("\nOption 1: Upload via Python (recommended)")
print("-" * 60)
print("Run these commands:")
print()
print("  # Login to Hugging Face")
print("  huggingface-cli login")
print()
print("  # Then run:")
print("  python -c \"from datasets import load_from_disk; ")
print(f"  ds = load_from_disk('{local_save_path}'); ")
print(f"  ds.push_to_hub('YOUR_USERNAME/{dataset_name}')\"")
print()
print("\nOption 2: Use AutoTrain with uploaded dataset")
print("-" * 60)
print("After uploading to HF Hub:")
print("1. Go to: https://huggingface.co/autotrain")
print("2. Create new project → Image Classification")
print(f"3. Select your dataset: YOUR_USERNAME/{dataset_name}")
print("4. Configure and train!")
print()
print("\nOption 3: Manual upload via HF website")
print("-" * 60)
print("1. Go to: https://huggingface.co/new-dataset")
print(f"2. Create dataset: {dataset_name}")
print(f"3. Upload the folder: {local_save_path}")
print()
print("=" * 60)
print("\n💡 Classes in your dataset:")
for i, cls in enumerate(class_names, 1):
    print(f"  {i}. {cls}")
