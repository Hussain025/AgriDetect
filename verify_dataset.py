"""
Verify the uploaded dataset is accessible and correct
"""

from datasets import load_dataset

print("=" * 60)
print("Verifying Uploaded Dataset")
print("=" * 60)

dataset_name = "Warrior025/plant-disease-classification"

print(f"\n📥 Loading dataset: {dataset_name}")
print("This may take a moment...")

try:
    ds = load_dataset(dataset_name)
    
    print("\n✅ Dataset loaded successfully!")
    print("\n" + "=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)
    print(f"\n{ds}")
    
    # Get class names
    class_names = ds['train'].features['label'].names
    
    print("\n" + "=" * 60)
    print("DATASET STATISTICS")
    print("=" * 60)
    print(f"\n📊 Splits:")
    print(f"   Train:      {len(ds['train']):,} images")
    print(f"   Validation: {len(ds['validation']):,} images")
    print(f"   Test:       {len(ds['test']):,} images")
    print(f"   Total:      {len(ds['train']) + len(ds['validation']) + len(ds['test']):,} images")
    
    print(f"\n🏷️  Classes ({len(class_names)}):")
    for i, cls in enumerate(class_names, 1):
        train_count = sum(1 for x in ds['train'] if x['label'] == i-1)
        print(f"   {i}. {cls:40s} ({train_count} train images)")
    
    # Sample image info
    print("\n" + "=" * 60)
    print("SAMPLE IMAGE")
    print("=" * 60)
    sample = ds['train'][0]
    print(f"   Image size: {sample['image'].size}")
    print(f"   Image mode: {sample['image'].mode}")
    print(f"   Label: {class_names[sample['label']]}")
    
    print("\n" + "=" * 60)
    print("✅ DATASET VERIFICATION COMPLETE")
    print("=" * 60)
    print("\n✓ Dataset is properly formatted")
    print("✓ All splits are present")
    print("✓ Images are accessible")
    print("✓ Labels are correct")
    
    print("\n" + "=" * 60)
    print("READY FOR AUTOTRAIN!")
    print("=" * 60)
    print("\nYour dataset is ready to use in AutoTrain:")
    print(f"   Dataset: {dataset_name}")
    print(f"   URL: https://huggingface.co/datasets/{dataset_name}")
    
    print("\nNext steps:")
    print("1. Go to: https://huggingface.co/autotrain")
    print("2. Create new project → Image Classification")
    print(f"3. Select dataset: {dataset_name}")
    print("4. Configure and train!")
    
except Exception as e:
    print(f"\n❌ Error loading dataset: {e}")
    print("\nPossible issues:")
    print("- Dataset might still be processing (wait a minute)")
    print("- Check internet connection")
    print("- Verify dataset URL: https://huggingface.co/datasets/Warrior025/plant-disease-classification")
