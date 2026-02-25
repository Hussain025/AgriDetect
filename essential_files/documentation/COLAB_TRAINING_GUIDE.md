# Google Colab Training Guide

## 🚀 Quick Start (5 minutes setup)

### Step 1: Upload Notebook to Colab
1. Go to: https://colab.research.google.com/
2. Click "File" → "Upload notebook"
3. Upload `Plant_Disease_Training.ipynb` from your project folder
4. Or use "GitHub" tab and paste this repo URL

### Step 2: Enable GPU
1. Click "Runtime" → "Change runtime type"
2. Hardware accelerator: Select **GPU** (T4 GPU is free)
3. Click "Save"

### Step 3: Run Training
1. Click "Runtime" → "Run all" (or press Ctrl+F9)
2. Wait ~15-20 minutes for training to complete
3. All cells will execute automatically

## 📊 What to Expect

### Training Progress
You'll see:
- Dataset loading (1-2 minutes)
- Model initialization
- Training progress bars for each epoch
- Validation metrics after each epoch
- Final test metrics

### Expected Results
With ResNet-50 on this dataset, you should get:
- **Accuracy**: 85-95%
- **Training time**: 15-20 minutes on T4 GPU
- **Model size**: ~100MB

## 📸 Screenshots for Report

Capture these for your documentation:

1. **Training Configuration**
   - Dataset info (1,600 images, 8 classes)
   - Model: ResNet-50
   - Hyperparameters

2. **Training Progress**
   - Epoch progress bars
   - Loss decreasing over time

3. **Validation Metrics**
   - Accuracy, Precision, Recall, F1

4. **Test Results**
   - Final test set performance

## 💾 Download Trained Model

After training completes, run this in a new cell:

```python
from google.colab import files
import shutil

# Zip the model
!zip -r plant-disease-model.zip plant-disease-model

# Download
files.download('plant-disease-model.zip')
```

## 🔧 Troubleshooting

### "GPU not available"
- Make sure you selected GPU in runtime settings
- Free Colab has usage limits - try again later if quota exceeded

### "Out of memory"
- Reduce BATCH_SIZE from 32 to 16 or 8
- Edit the configuration cell

### "Dataset loading slow"
- Normal on first run (downloads ~27MB)
- Subsequent runs use cached data

## 📋 For Your Report

### Step 3 Documentation:

**Training Platform**: Google Colab (Free T4 GPU)

**Model Architecture**: 
- Base: ResNet-50 (pre-trained on ImageNet)
- Fine-tuned on plant disease dataset
- Transfer learning approach

**Training Configuration**:
- Epochs: 10
- Batch size: 32
- Learning rate: 2e-5
- Optimizer: AdamW
- Warmup steps: 100

**Dataset**:
- Source: Hugging Face Hub (Warrior025/plant-disease-classification)
- Train: 1,120 images
- Validation: 320 images
- Test: 160 images
- Classes: 8 plant diseases

**Results**: (Fill in after training)
- Validation Accuracy: ____%
- Test Accuracy: ____%
- Precision: ____
- Recall: ____
- F1 Score: ____

## ⏭️ Next Steps

After training completes:
1. ✅ Download the trained model
2. ✅ Extract `plant-disease-model.zip`
3. ✅ Move to your project folder
4. ✅ Run the Streamlit demo app (Step 5)

---

**Need help?** Check the notebook output for error messages or ask for assistance.
