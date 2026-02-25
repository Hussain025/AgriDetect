import os
import shutil
import zipfile
from pathlib import Path

# Source and destination paths
source_dir = "New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/train"
dest_dir = "roboflow_dataset"

# Selected classes with 200 images each
selected_classes = [
    "Apple___Apple_scab",
    "Tomato___Early_blight",
    "Potato___Late_blight",
    "Grape___Black_rot",
    "Corn_(maize)___Common_rust_",
    "Pepper,_bell___Bacterial_spot",
    "Strawberry___Leaf_scorch",
    "Tomato___healthy"
]

images_per_class = 200

# Create destination directory structure
if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)

# Create train, valid, test folders
train_dir = os.path.join(dest_dir, "train")
valid_dir = os.path.join(dest_dir, "valid")
test_dir = os.path.join(dest_dir, "test")

os.makedirs(train_dir)
os.makedirs(valid_dir)
os.makedirs(test_dir)

print("Creating Roboflow-compatible dataset...")
print(f"Structure: train (70%), valid (20%), test (10%)")
print(f"Total {images_per_class} images per class\n")

# Split ratios
train_ratio = 0.7
valid_ratio = 0.2
test_ratio = 0.1

# Copy and split images from each class
for class_name in selected_classes:
    source_class_path = os.path.join(source_dir, class_name)
    
    # Create class directories in train/valid/test
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(valid_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)
    
    # Get all images from source class
    images = [f for f in os.listdir(source_class_path) if f.endswith('.JPG')]
    images_to_use = images[:images_per_class]
    
    # Calculate split sizes
    train_size = int(len(images_to_use) * train_ratio)
    valid_size = int(len(images_to_use) * valid_ratio)
    
    train_images = images_to_use[:train_size]
    valid_images = images_to_use[train_size:train_size + valid_size]
    test_images = images_to_use[train_size + valid_size:]
    
    print(f"{class_name}:")
    print(f"  Train: {len(train_images)}, Valid: {len(valid_images)}, Test: {len(test_images)}")
    
    # Copy train images
    for img in train_images:
        src = os.path.join(source_class_path, img)
        dst = os.path.join(train_dir, class_name, img)
        shutil.copy2(src, dst)
    
    # Copy valid images
    for img in valid_images:
        src = os.path.join(source_class_path, img)
        dst = os.path.join(valid_dir, class_name, img)
        shutil.copy2(src, dst)
    
    # Copy test images
    for img in test_images:
        src = os.path.join(source_class_path, img)
        dst = os.path.join(test_dir, class_name, img)
        shutil.copy2(src, dst)

print(f"\n✓ Dataset created with train/valid/test split")

# Create zip file with correct structure for Roboflow
zip_filename = "roboflow_dataset.zip"
print(f"\nCreating Roboflow-compatible zip: {zip_filename}...")

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Walk through the dataset directory
    for root, dirs, files in os.walk(dest_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Create archive path relative to dest_dir (so train/valid/test are at root)
            arcname = os.path.relpath(file_path, dest_dir)
            zipf.write(file_path, arcname)

print(f"✓ Zip created: {zip_filename}")
print(f"\nZip structure:")
print(f"  roboflow_dataset.zip")
print(f"  ├── train/")
print(f"  │   ├── class1/")
print(f"  │   └── ...")
print(f"  ├── valid/")
print(f"  │   ├── class1/")
print(f"  │   └── ...")
print(f"  └── test/")
print(f"      ├── class1/")
print(f"      └── ...")
print(f"\n✓ Ready to upload to Roboflow!")
print(f"\nSelected classes:")
for i, cls in enumerate(selected_classes, 1):
    print(f"  {i}. {cls}")

