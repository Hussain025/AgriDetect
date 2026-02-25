import os
import shutil
import zipfile
from pathlib import Path
from PIL import Image

# Configuration
source_dir = "roboflow_dataset"  # Your existing dataset
output_dir = "autotrain_dataset"
output_zip = "autotrain_plant_disease.zip"
target_size = (224, 224)  # Resize to 224x224 as per your requirements

print("=" * 60)
print("Preparing Dataset for Hugging Face AutoTrain")
print("=" * 60)

# Clean up existing output
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
if os.path.exists(output_zip):
    os.remove(output_zip)

os.makedirs(output_dir)

# Process each split (train, valid, test)
splits = ['train', 'valid', 'test']
total_images = 0

for split in splits:
    split_path = os.path.join(source_dir, split)
    
    if not os.path.exists(split_path):
        print(f"⚠️  Warning: {split} folder not found, skipping...")
        continue
    
    print(f"\n📁 Processing {split} split...")
    
    # Get all class folders
    classes = [d for d in os.listdir(split_path) 
               if os.path.isdir(os.path.join(split_path, d))]
    
    split_count = 0
    for class_name in classes:
        class_path = os.path.join(split_path, class_name)
        output_class_path = os.path.join(output_dir, split, class_name)
        os.makedirs(output_class_path, exist_ok=True)
        
        # Get all images
        images = [f for f in os.listdir(class_path) 
                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        # Resize and copy images
        for img_name in images:
            src_img_path = os.path.join(class_path, img_name)
            dst_img_path = os.path.join(output_class_path, img_name)
            
            try:
                # Open, resize, and save image
                with Image.open(src_img_path) as img:
                    # Convert to RGB if needed
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # Resize to 224x224
                    img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                    
                    # Save as JPEG
                    output_name = os.path.splitext(img_name)[0] + '.jpg'
                    img_resized.save(os.path.join(output_class_path, output_name), 
                                   'JPEG', quality=95)
                
                split_count += 1
                total_images += 1
            except Exception as e:
                print(f"  ⚠️  Error processing {img_name}: {e}")
        
        print(f"  ✓ {class_name}: {len(images)} images")
    
    print(f"  Total in {split}: {split_count} images")

print(f"\n✓ Total images processed: {total_images}")

# Create metadata file
print("\n📝 Creating metadata.txt...")
with open(os.path.join(output_dir, "metadata.txt"), "w") as f:
    f.write("Dataset: Plant Disease Classification\n")
    f.write("Image Size: 224x224\n")
    f.write("Format: Image Classification (Folder Structure)\n")
    f.write(f"Total Images: {total_images}\n")
    f.write("\nSplits:\n")
    for split in splits:
        split_path = os.path.join(output_dir, split)
        if os.path.exists(split_path):
            count = sum([len(files) for r, d, files in os.walk(split_path)])
            f.write(f"  {split}: {count} images\n")

# Create ZIP file for AutoTrain
print(f"\n📦 Creating ZIP file: {output_zip}...")
with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, output_dir)
            zipf.write(file_path, arcname)
            
print(f"✓ ZIP created successfully!")

# Display final structure
print("\n" + "=" * 60)
print("📊 DATASET SUMMARY")
print("=" * 60)
print(f"Output ZIP: {output_zip}")
print(f"Image Size: {target_size[0]}x{target_size[1]}")
print(f"\nStructure inside ZIP:")
print(f"  {output_zip}")
print(f"  ├── train/")
print(f"  │   ├── Apple___Apple_scab/")
print(f"  │   ├── Tomato___Early_blight/")
print(f"  │   └── ... (8 classes)")
print(f"  ├── valid/")
print(f"  │   └── ... (same classes)")
print(f"  ├── test/")
print(f"  │   └── ... (same classes)")
print(f"  └── metadata.txt")

print("\n" + "=" * 60)
print("✅ READY FOR HUGGING FACE AUTOTRAIN!")
print("=" * 60)
print("\nNext Steps:")
print("1. Go to: https://huggingface.co/autotrain")
print("2. Click 'New Project' → 'Image Classification'")
print(f"3. Upload: {output_zip}")
print("4. Configure training settings")
print("5. Start training!")
print("\n💡 Tip: Keep this terminal output for your report documentation")
