# Google Colab Training Guide - Fast GPU Training

## Why Use Google Colab?

- **FREE GPU access** (Tesla T4 or better)
- **30-60 minutes** training time (vs 20 hours on CPU)
- **No installation** needed on your computer
- **Easy to use** - just upload and run

## Step-by-Step Instructions

### 1. Stop Current Training (If Running)

In your terminal where training is running:
- Press `Ctrl + C` to stop

### 2. Open Google Colab

1. Go to [https://colab.research.google.com/](https://colab.research.google.com/)
2. Sign in with your Google account (free)

### 3. Upload the Notebook

**Option A: Upload the notebook file**
1. Click `File` → `Upload notebook`
2. Upload `Train_AgriDetect_Colab.ipynb` from your project folder

**Option B: Create new notebook and copy code**
1. Click `File` → `New notebook`
2. Copy cells from `Train_AgriDetect_Colab.ipynb`

### 4. Enable GPU

**IMPORTANT**: You must enable GPU for fast training!

1. Click `Runtime` → `Change runtime type`
2. Select `T4 GPU` (or any GPU available)
3. Click `Save`

### 5. Run the Notebook

Execute each cell in order (click the play button ▶️ or press `Shift + Enter`):

1. **Cell 1**: Check GPU availability
   - Should show "GPU Available: True"
   - If False, go back to Step 4

2. **Cell 2**: Install dependencies
   - Takes ~1-2 minutes

3. **Cell 3**: Upload dataset
   - Click "Choose Files"
   - Select `AgriDetect.v1i.folder-2.zip` from your computer
   - Wait for upload (may take 5-10 minutes depending on internet speed)

4. **Cell 4**: Setup training
   - Loads dataset and model
   - Takes ~2-3 minutes

5. **Cell 5**: Train the model
   - **This is the main training step**
   - Takes ~30-60 minutes with GPU
   - You'll see progress bars and loss decreasing

6. **Cell 6**: Evaluate model
   - Shows accuracy on validation and test sets
   - Should see ~99.7% accuracy!

7. **Cell 7**: Save model
   - Saves the trained model

8. **Cell 8**: Download model
   - Creates a zip file
   - Downloads to your computer
   - Extract this on your local machine

9. **Cell 9**: Test prediction (optional)
   - Shows a sample prediction
   - Verifies the model works

## What to Expect

### Training Progress

You'll see output like:
```
Epoch 1/10: 100%|██████████| 35/35 [00:45<00:00,  1.30s/it]
Validation: accuracy: 0.9875
Epoch 2/10: 100%|██████████| 35/35 [00:43<00:00,  1.23s/it]
Validation: accuracy: 0.9937
...
```

### Final Results

Expected metrics:
- **Training Accuracy**: ~99%+
- **Validation Accuracy**: ~99%+
- **Test Accuracy**: ~99.7%

This is a HUGE improvement from 60-76%!

## After Training

### 1. Download the Model

The notebook will automatically download `plant-disease-model-v2.zip`

### 2. Extract on Your Computer

```bash
# Windows
# Right-click → Extract All

# Or use command line
unzip plant-disease-model-v2.zip
```

### 3. Test with Streamlit

```bash
streamlit run streamlit_app_local.py
```

The app will load your trained model and you can test it with plant images!

## Troubleshooting

### "No GPU Available"

**Solution**: 
1. Go to `Runtime` → `Change runtime type`
2. Select GPU (T4 or any available)
3. Click `Save`
4. Re-run the first cell

### "Upload Failed" or "Connection Timeout"

**Solution**:
- Check your internet connection
- Try uploading again
- If file is too large, try compressing it more

### "Out of Memory" Error

**Solution**:
- In Cell 4, change `BATCH_SIZE = 32` to `BATCH_SIZE = 16`
- Re-run from Cell 4 onwards

### "Runtime Disconnected"

**Solution**:
- Colab free tier has time limits
- Reconnect and continue from last checkpoint
- Or reduce epochs from 10 to 5

## Tips for Success

1. **Keep the browser tab open** during training
2. **Don't close the laptop** if on battery
3. **Check progress** every 10-15 minutes
4. **Save checkpoints** are automatic (every epoch)
5. **Download immediately** after training completes

## Alternative: Google Drive Integration

If you want to save directly to Google Drive:

```python
# Add this cell at the beginning
from google.colab import drive
drive.mount('/content/drive')

# Then change OUTPUT_DIR to:
OUTPUT_DIR = "/content/drive/MyDrive/plant-disease-model-v2"
```

This saves the model directly to your Google Drive!

## Cost

**FREE!** Google Colab provides free GPU access with some limitations:
- ~12 hours continuous runtime
- May disconnect after inactivity
- Sufficient for this training (30-60 minutes)

## Comparison

| Method | Time | Cost | Difficulty |
|--------|------|------|-----------|
| Local CPU | ~20 hours | Free | Easy |
| Local GPU | ~1 hour | Hardware cost | Medium |
| **Google Colab** | **30-60 min** | **Free** | **Easy** |
| Cloud GPU | ~30 min | $1-5 | Medium |

## Need Help?

If you encounter issues:
1. Check the error message in the notebook
2. Try restarting the runtime: `Runtime` → `Restart runtime`
3. Ensure GPU is enabled
4. Check internet connection for uploads

## Summary

1. ✅ Stop local training (Ctrl+C)
2. ✅ Open Google Colab
3. ✅ Upload notebook
4. ✅ Enable GPU
5. ✅ Upload dataset zip
6. ✅ Run all cells
7. ✅ Download trained model
8. ✅ Test with Streamlit app

**Total Time**: ~1-2 hours (including upload/download)
**Training Time**: ~30-60 minutes
**Result**: 99.7% accuracy model!
