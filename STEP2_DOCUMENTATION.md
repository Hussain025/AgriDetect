# Step 2: Export Dataset for Hugging Face AutoTrain

## ✅ Completed Tasks

### Dataset Preparation
- **Source Dataset**: New Plant Diseases Dataset (Augmented)
- **Selected Classes**: 8 disease categories
- **Total Images**: 1,600 images
- **Image Resize**: 224×224 pixels (as required)
- **Format**: Image Classification (Folder Structure)

### Dataset Split
- **Train**: 1,120 images (70%)
- **Validation**: 320 images (20%)
- **Test**: 160 images (10%)

### Classes Included
1. Apple___Apple_scab (200 images)
2. Corn_(maize)___Common_rust_ (200 images)
3. Grape___Black_rot (200 images)
4. Pepper,_bell___Bacterial_spot (200 images)
5. Potato___Late_blight (200 images)
6. Strawberry___Leaf_scorch (200 images)
7. Tomato___Early_blight (200 images)
8. Tomato___healthy (200 images)

### Preprocessing Applied
✔️ Resize = 224×224 (LANCZOS resampling)
✔️ RGB conversion (standardized)
✔️ JPEG format with 95% quality
✔️ Train/Validation/Test split maintained

## 📦 Output File
**File**: `autotrain_plant_disease.zip`

**Structure**:
```
autotrain_plant_disease.zip
├── train/
│   ├── Apple___Apple_scab/ (140 images)
│   ├── Corn_(maize)___Common_rust_/ (140 images)
│   ├── Grape___Black_rot/ (140 images)
│   ├── Pepper,_bell___Bacterial_spot/ (140 images)
│   ├── Potato___Late_blight/ (140 images)
│   ├── Strawberry___Leaf_scorch/ (140 images)
│   ├── Tomato___Early_blight/ (140 images)
│   └── Tomato___healthy/ (140 images)
├── valid/
│   └── [same 8 classes, 40 images each]
├── test/
│   └── [same 8 classes, 20 images each]
└── metadata.txt
```

## 🚀 Next Steps for Hugging Face AutoTrain

### Step-by-Step Instructions:

1. **Go to Hugging Face AutoTrain**
   - URL: https://huggingface.co/autotrain
   - Sign in with your Hugging Face account

2. **Create New Project**
   - Click "New Project"
   - Select "Image Classification"
   - Give it a name: e.g., "plant-disease-classifier"

3. **Upload Dataset**
   - Upload: `autotrain_plant_disease.zip`
   - AutoTrain will automatically detect the folder structure
   - Verify it recognizes 8 classes

4. **Configure Training**
   - Model: Choose a pre-trained model (e.g., ResNet, EfficientNet, ViT)
   - Training parameters:
     - Epochs: 10-20 (start with 10)
     - Batch size: 16 or 32
     - Learning rate: Auto (or 1e-4)

5. **Connect Weights & Biases (Optional)**
   - In AutoTrain settings, enable W&B integration
   - Enter your W&B API key
   - This will track metrics automatically

6. **Start Training**
   - Click "Start Training"
   - Save the training job URL for your report
   - Monitor progress in AutoTrain dashboard

## 📸 Screenshots Needed for Report

For your milestone report, capture:
1. ✅ Dataset upload confirmation in AutoTrain
2. ✅ Training configuration settings
3. ✅ Training job URL/ID
4. Training progress (during Step 3)
5. Final accuracy/loss metrics (after training)

## 📊 Expected Deliverables

### For Milestone Report:
- [x] Dataset version: v1-resize224-8classes
- [x] Preprocessing settings: 224×224, RGB, JPEG
- [x] Dataset split: 70/20/10
- [x] Total images: 1,600
- [x] Export format: Folder structure ZIP
- [ ] AutoTrain job link (after upload)
- [ ] Training configuration screenshot (after setup)

## 💡 Tips

- Keep the ZIP file (`autotrain_plant_disease.zip`) - you may need to re-upload
- Document your AutoTrain job URL immediately after starting
- If AutoTrain doesn't support W&B, you can integrate it later in Step 4
- The 224×224 size is optimal for most pre-trained models

## ⚠️ Troubleshooting

**If AutoTrain doesn't recognize the structure:**
- Ensure the ZIP contains train/valid/test folders at the root level
- Each class folder should contain only image files
- Check that all images are valid JPEGs

**If upload fails:**
- Check file size (should be manageable at ~1600 images)
- Try uploading from a stable internet connection
- Verify your Hugging Face account has sufficient quota

---

**Status**: ✅ Step 2 Complete - Ready for AutoTrain Upload
**Next**: Step 3 - Train Model with Hugging Face AutoTrain
