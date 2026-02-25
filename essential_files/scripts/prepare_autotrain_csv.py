import os
import shutil
import zipfile
import csv
from pathlib import Path
from PIL import Image

# Configuration
source_dir = "roboflow_dataset"
output_dir = "autotrain_csv_format"
output_zip = "autotrain_plant_disease_csv.zip"
target_size = (224, 224)

print("=" * 60)
print("Preparing Dataset for Hugging Face AutoTrain (CSV Format)")
print("=" * 60)

# Clean up
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
if os.path.exists(output_zip):
    os.remove(output_zip)

os.makedirs(output_dir)
os.makedirs(os.path.join(output_dir, "images"))

# Prepare CSV data
csv_data = []
image_counter = 0

splits = ['train', 'valid', 'test']

for split in splits:
    split_path = os.path.join(source_dir, split)
    
    if not os.path.exists(split_path):
        continue
    
    print(f"\n📁 Processing {split} split...")
    
    classes = [d for d in os.listdir(split_path) 
               if os.path.isdir(os.path.join(split_path, d))]
    
    for class_name in classes:
        class_path = os.path.join(split_path, class_name)
        images = [f for f in os.listdir(class_path) 
                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        for img_name in images:
            src_img_path = os.path.join(class_path, img_name)
            
            # Create unique filename
            new_img_name = f"{split}_{class_name}_{image_counter:04d}.jpg"
            dst_img_path = os.path.join(output_dir, "images", new_img_name)
            
            try:
                # Resize and save
                with Image.open(src_img_path) as img:
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                    img_resized.save(dst_img_path, 'JPEG', quality=95)
                
                # Add to CSV data
                csv_data.append({
                    'file_name': f"images/{new_img_name}",
                    'label': class_name,
                    'split': split
                })
                
                image_counter += 1
            except Exception as e:
                print(f"  ⚠️  Error: {e}")
        
        print(f"  ✓ {class_name}: {len(images)} images")

# Write CSV file
csv_path = os.path.join(output_dir, "metadata.csv")
print(f"\n📝 Creating metadata.csv with {len(csv_data)} entries...")

with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['file_name', 'label', 'split']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(csv_data)

print(f"✓ CSV created: {len(csv_data)} rows")

# Create ZIP
print(f"\n📦 Creating ZIP: {output_zip}...")
with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, output_dir)
            zipf.write(file_path, arcname)

print(f"✓ ZIP created!")

# Summary
print("\n" + "=" * 60)
print("📊 DATASET SUMMARY (CSV Format)")
print("=" * 60)
print(f"Output ZIP: {output_zip}")
print(f"Total Images: {len(csv_data)}")
print(f"Image Size: 224x224")
print(f"\nStructure:")
print(f"  {output_zip}")
print(f"  ├── metadata.csv (file_name, label, split)")
print(f"  └── images/")
print(f"      └── [all {len(csv_data)} images]")

# Count by split
train_count = sum(1 for row in csv_data if row['split'] == 'train')
valid_count = sum(1 for row in csv_data if row['split'] == 'valid')
test_count = sum(1 for row in csv_data if row['split'] == 'test')

print(f"\nSplit Distribution:")
print(f"  Train: {train_count}")
print(f"  Valid: {valid_count}")
print(f"  Test: {test_count}")

print("\n" + "=" * 60)
print("✅ ALTERNATIVE FORMAT READY!")
print("=" * 60)
print("\nTry uploading this CSV format if folder structure failed")
