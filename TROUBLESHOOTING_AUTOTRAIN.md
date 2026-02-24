# Troubleshooting: AutoTrain 400 Bad Request Error

## 🔍 Common Causes

The "400 Bad Request" error when creating an AutoTrain project usually happens due to:

1. **Dataset format issues** - AutoTrain expects specific structure
2. **File size limits** - ZIP might be too large
3. **Authentication issues** - Token or permissions problems
4. **Browser/network issues** - Upload interruption

## ✅ Solution Options

### Option 1: Try CSV Format (Recommended)

AutoTrain also accepts CSV format which is more reliable:

```bash
python prepare_autotrain_csv.py
```

This creates `autotrain_plant_disease_csv.zip` with:
- `metadata.csv` (file_name, label, split columns)
- `images/` folder with all images

Upload this instead of the folder structure.

---

### Option 2: Upload to Hugging Face Hub First (Most Reliable)

Instead of uploading directly to AutoTrain, upload to HF Hub first:

**Step 1: Install required libraries**
```bash
pip install datasets huggingface-hub pillow
```

**Step 2: Run the upload script**
```bash
python upload_to_huggingface.py
```

**Step 3: Login to Hugging Face**
```bash
huggingface-cli login
```
(Enter your HF token from https://huggingface.co/settings/tokens)

**Step 4: Upload the dataset**
```python
from datasets import load_from_disk

# Load the saved dataset
dataset = load_from_disk('hf_dataset')

# Push to your HF account (replace YOUR_USERNAME)
dataset.push_to_hub('YOUR_USERNAME/plant-disease-classification')
```

**Step 5: Use in AutoTrain**
- Go to AutoTrain
- Create new project
- Select "Use existing dataset"
- Choose your uploaded dataset
- Start training!

---

### Option 3: Use Smaller Batch

If the ZIP is too large, try uploading in smaller batches:

```python
# Modify prepare_autotrain_dataset.py
# Change line: images_per_class = 200
# To: images_per_class = 100
```

Then re-run the preparation script.

---

### Option 4: Direct AutoTrain API (Advanced)

Use AutoTrain Python library directly:

```bash
pip install autotrain-advanced
```

```python
from autotrain.dataset import ImageClassificationDataset

# Create dataset
dataset = ImageClassificationDataset(
    train_data="roboflow_dataset/train",
    valid_data="roboflow_dataset/valid",
    test_data="roboflow_dataset/test"
)

# Upload and train
# (requires AutoTrain API token)
```

---

## 🔧 Quick Fixes to Try

### 1. Check File Size
```bash
# Windows PowerShell
Get-Item autotrain_plant_disease.zip | Select-Object Name, Length

# If > 500MB, use Option 1 or 3
```

### 2. Verify ZIP Structure
```bash
# Extract and check
unzip -l autotrain_plant_disease.zip | head -20
```

Should show:
```
train/ClassName/image.jpg
valid/ClassName/image.jpg
test/ClassName/image.jpg
```

### 3. Clear Browser Cache
- Clear cookies for huggingface.co
- Try incognito/private mode
- Try different browser

### 4. Check HF Token Permissions
- Go to: https://huggingface.co/settings/tokens
- Ensure token has "write" access
- Regenerate if needed

---

## 📋 Recommended Workflow

**For your project, I recommend Option 2** (Upload to HF Hub first):

1. ✅ Run `python upload_to_huggingface.py`
2. ✅ Login: `huggingface-cli login`
3. ✅ Upload dataset to HF Hub
4. ✅ Use AutoTrain with the uploaded dataset
5. ✅ This avoids UI upload issues entirely

**Benefits:**
- More reliable than direct upload
- Dataset is reusable
- Can share with team
- Better for documentation
- Easier to debug

---

## 🆘 Still Having Issues?

### Alternative: Skip AutoTrain, Use Transformers Directly

You can train directly with Hugging Face Transformers:

```python
from transformers import AutoImageProcessor, AutoModelForImageClassification, TrainingArguments, Trainer

# Load model
model = AutoModelForImageClassification.from_pretrained(
    "microsoft/resnet-50",
    num_labels=8,
    ignore_mismatched_sizes=True
)

# Train with your dataset
# (Full code available if needed)
```

This gives you more control and avoids AutoTrain UI issues.

---

## 📞 Next Steps

**Choose one approach:**

- [ ] Try CSV format (quickest)
- [ ] Upload to HF Hub first (most reliable)
- [ ] Use smaller dataset (if size is issue)
- [ ] Train with Transformers directly (most control)

**For your report:**
- Document which method you used
- Screenshot the successful upload/training
- Note any issues encountered

---

## 💡 Pro Tips

1. **Always test with small subset first** (50 images per class)
2. **Keep original dataset** as backup
3. **Document your HF dataset URL** for the report
4. **Use descriptive dataset names** (e.g., plant-disease-v1-224px)

---

**Need help with any of these options? Let me know which one you want to try!**
