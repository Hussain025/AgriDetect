# Complete Workflow Guide
## Roboflow → Hugging Face → Training → Streamlit

---

## ✅ Step 1: Dataset Preparation (COMPLETED)
- ✅ Created subset of 1,600 images (8 classes)
- ✅ Split: 70% train, 20% validation, 10% test
- ✅ Resized to 224×224
- ✅ Organized in proper folder structure

**Files**: `create_subset.py`, `roboflow_dataset/`

---

## ✅ Step 2: Upload to Hugging Face (COMPLETED)
- ✅ Uploaded to Hugging Face Hub
- ✅ Dataset URL: https://huggingface.co/datasets/Warrior025/plant-disease-classification
- ✅ Publicly accessible
- ✅ Verified and working

**Files**: `upload_to_huggingface.py`, `verify_dataset.py`

---

## 🔄 Step 3: Train Model (IN PROGRESS)

### Option A: Google Colab (RECOMMENDED)

**Why Colab?**
- Free GPU (T4)
- Fast training (~15-20 min)
- No local setup needed
- Easy to use

**Steps**:
1. Open https://colab.research.google.com/
2. Upload `Plant_Disease_Training.ipynb`
3. Runtime → Change runtime type → GPU
4. Runtime → Run all
5. Wait for training to complete
6. Download trained model

**Expected Results**:
- Accuracy: 85-95%
- Training time: 15-20 minutes
- Model size: ~100MB

**Files**: `Plant_Disease_Training.ipynb`, `COLAB_TRAINING_GUIDE.md`

### Option B: Local Training

```bash
python train_model.py
```

**Note**: Will be slow on CPU (1-2 hours)

**Files**: `train_model.py`

---

## ⏭️ Step 4: Weights & Biases (OPTIONAL)

To enable W&B tracking, modify the notebook:

```python
# In training_args, change:
report_to="wandb"  # instead of "none"

# Add before training:
import wandb
wandb.login()
```

This will automatically log:
- Training/validation loss
- Accuracy curves
- Learning rate schedule
- System metrics

---

## 🖥️ Step 5: Streamlit Demo App

### After Training Completes:

1. **Download model from Colab**:
   ```python
   from google.colab import files
   !zip -r plant-disease-model.zip plant-disease-model
   files.download('plant-disease-model.zip')
   ```

2. **Extract in project folder**:
   ```bash
   unzip plant-disease-model.zip
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Open browser**: http://localhost:8501

### Demo Features:
- ✅ Upload plant leaf images
- ✅ Real-time disease detection
- ✅ Confidence scores
- ✅ All class probabilities
- ✅ Treatment recommendations
- ✅ Clean, professional UI

**Files**: `streamlit_app.py`, `requirements.txt`

---

## 📊 For Your Report

### Deliverables Checklist:

#### Step 1 (Roboflow/Preprocessing):
- [x] Dataset structure screenshot
- [x] Preprocessing settings (224×224, augmentation)
- [x] Class distribution (200 images each)
- [x] Train/val/test split (70/20/10)

#### Step 2 (Hugging Face):
- [x] Dataset URL: https://huggingface.co/datasets/Warrior025/plant-disease-classification
- [x] Upload confirmation
- [x] Dataset card/info page

#### Step 3 (Training):
- [ ] Training configuration screenshot
- [ ] Training progress/loss curves
- [ ] Validation metrics (accuracy, precision, recall, F1)
- [ ] Test set results
- [ ] Training time and hardware used

#### Step 4 (W&B - Optional):
- [ ] W&B dashboard link
- [ ] Loss/accuracy curves
- [ ] Confusion matrix
- [ ] System metrics

#### Step 5 (Streamlit):
- [ ] Demo app screenshot
- [ ] Sample predictions
- [ ] Confidence scores
- [ ] App running locally

---

## 🎯 Current Status

### Completed:
✅ Dataset preparation  
✅ Upload to Hugging Face Hub  
✅ Dataset verification  
✅ Training scripts created  
✅ Streamlit app created  

### Next Action:
🔄 **Train model in Google Colab**

### To Do:
⏳ Download trained model  
⏳ Run Streamlit demo  
⏳ Document results  

---

## 📝 Quick Commands Reference

```bash
# Verify dataset
python verify_dataset.py

# Train locally (slow)
python train_model.py

# Run Streamlit app (after training)
streamlit run streamlit_app.py

# Install dependencies
pip install -r requirements.txt
```

---

## 🆘 Troubleshooting

### "Model not found" in Streamlit
- Make sure `plant-disease-model/` folder is in same directory
- Check that model files were extracted correctly

### "CUDA out of memory" in Colab
- Reduce batch size in notebook (32 → 16 → 8)
- Restart runtime and try again

### Slow training locally
- Use Google Colab instead (free GPU)
- Or reduce epochs (10 → 5)

---

## 📞 Support

If you encounter issues:
1. Check error messages carefully
2. Verify file paths and folder structure
3. Ensure all dependencies are installed
4. Try restarting runtime/kernel

---

**Ready to train? Open `Plant_Disease_Training.ipynb` in Google Colab!**
