"""
Train Plant Disease Classification Model - Using Local Dataset
High-accuracy dataset (99.7%) from AgriDetect.v1i.folder-2.zip
"""

from datasets import load_dataset, DatasetDict
from transformers import (
    AutoImageProcessor,
    AutoModelForImageClassification,
    TrainingArguments,
    Trainer
)
import torch
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import os

print("=" * 60)
print("Plant Disease Classification - Local Dataset Training")
print("=" * 60)

# Configuration - Using new high-accuracy dataset
DATASET_DIR = "AgriDetect_new_model"
MODEL_NAME = "microsoft/resnet-50"  # Pre-trained ResNet-50
OUTPUT_DIR = "./plant-disease-model-v2"
NUM_EPOCHS = 10
BATCH_SIZE = 16
LEARNING_RATE = 2e-5

print(f"\n📊 Configuration:")
print(f"   Dataset: {DATASET_DIR} (99.7% accuracy)")
print(f"   Base Model: {MODEL_NAME}")
print(f"   Epochs: {NUM_EPOCHS}")
print(f"   Batch Size: {BATCH_SIZE}")
print(f"   Learning Rate: {LEARNING_RATE}")

# Load dataset from local folders
print(f"\n📥 Loading dataset from local folders...")
dataset = load_dataset(
    "imagefolder",
    data_dir=DATASET_DIR,
    drop_labels=False
)

print(f"✅ Dataset loaded!")
print(f"   Train: {len(dataset['train'])} images")
print(f"   Validation: {len(dataset['validation'])} images")
print(f"   Test: {len(dataset['test'])} images")

# Get labels
labels = dataset["train"].features["label"].names
num_labels = len(labels)
print(f"\n🏷️  Classes ({num_labels}):")
for i, label in enumerate(labels):
    print(f"   {i}: {label}")

# Load image processor
print(f"\n🔧 Loading image processor...")
image_processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
print(f"✅ Image processor loaded!")

# Preprocessing function
def preprocess_images(examples):
    """Preprocess images for the model"""
    images = [img.convert("RGB") for img in examples["image"]]
    inputs = image_processor(images, return_tensors="pt")
    # Flatten the batch dimension for proper storage
    inputs = {k: v.squeeze() if v.ndim > 1 and v.shape[0] == 1 else v for k, v in inputs.items()}
    inputs["labels"] = examples["label"]
    return inputs

# Apply preprocessing
print(f"\n🔄 Preprocessing images...")
dataset = dataset.map(
    preprocess_images, 
    batched=True, 
    batch_size=32,
    remove_columns=dataset["train"].column_names
)
print(f"✅ Preprocessing complete!")

# Load model
print(f"\n🤖 Loading model...")
model = AutoModelForImageClassification.from_pretrained(
    MODEL_NAME,
    num_labels=num_labels,
    id2label={i: label for i, label in enumerate(labels)},
    label2id={label: i for i, label in enumerate(labels)},
    ignore_mismatched_sizes=True
)
print(f"✅ Model loaded!")

# Metrics function
def compute_metrics(eval_pred):
    """Compute accuracy, precision, recall, F1"""
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    
    accuracy = accuracy_score(labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(
        labels, predictions, average='weighted'
    )
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }

# Training arguments
print(f"\n⚙️  Setting up training...")
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=NUM_EPOCHS,
    per_device_train_batch_size=BATCH_SIZE,
    per_device_eval_batch_size=BATCH_SIZE,
    learning_rate=LEARNING_RATE,
    warmup_steps=100,
    weight_decay=0.01,
    logging_dir=f"{OUTPUT_DIR}/logs",
    logging_steps=10,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    push_to_hub=False,
    report_to="none",
)

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
    compute_metrics=compute_metrics,
)

print(f"✅ Trainer ready!")

# Check for GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"\n💻 Device: {device}")
if device == "cpu":
    print("   ⚠️  Training on CPU will be slow. Consider using GPU/Colab.")

# Start training
print("\n" + "=" * 60)
print("🚀 STARTING TRAINING")
print("=" * 60)
print("\nThis will take some time...")
print("Training progress will be shown below:\n")

try:
    # Train the model
    train_results = trainer.train()
    
    print("\n" + "=" * 60)
    print("✅ TRAINING COMPLETE!")
    print("=" * 60)
    
    # Evaluate on validation set
    print("\n📊 Evaluating on validation set...")
    val_metrics = trainer.evaluate()
    print(f"\nValidation Results:")
    print(f"   Accuracy:  {val_metrics['eval_accuracy']:.4f} ({val_metrics['eval_accuracy']*100:.2f}%)")
    print(f"   Precision: {val_metrics['eval_precision']:.4f}")
    print(f"   Recall:    {val_metrics['eval_recall']:.4f}")
    print(f"   F1 Score:  {val_metrics['eval_f1']:.4f}")
    
    # Evaluate on test set
    print("\n📊 Evaluating on test set...")
    test_metrics = trainer.evaluate(dataset["test"])
    print(f"\nTest Results:")
    print(f"   Accuracy:  {test_metrics['eval_accuracy']:.4f} ({test_metrics['eval_accuracy']*100:.2f}%)")
    print(f"   Precision: {test_metrics['eval_precision']:.4f}")
    print(f"   Recall:    {test_metrics['eval_recall']:.4f}")
    print(f"   F1 Score:  {test_metrics['eval_f1']:.4f}")
    
    # Save model
    print(f"\n💾 Saving model to {OUTPUT_DIR}...")
    trainer.save_model(OUTPUT_DIR)
    image_processor.save_pretrained(OUTPUT_DIR)
    print(f"✅ Model saved!")
    
    # Save metrics to file
    with open(f"{OUTPUT_DIR}/metrics.txt", "w") as f:
        f.write("Plant Disease Classification - Training Results\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Dataset: {DATASET_DIR}\n")
        f.write(f"Model: {MODEL_NAME}\n")
        f.write(f"Epochs: {NUM_EPOCHS}\n\n")
        f.write("Validation Metrics:\n")
        f.write(f"  Accuracy:  {val_metrics['eval_accuracy']:.4f} ({val_metrics['eval_accuracy']*100:.2f}%)\n")
        f.write(f"  Precision: {val_metrics['eval_precision']:.4f}\n")
        f.write(f"  Recall:    {val_metrics['eval_recall']:.4f}\n")
        f.write(f"  F1 Score:  {val_metrics['eval_f1']:.4f}\n\n")
        f.write("Test Metrics:\n")
        f.write(f"  Accuracy:  {test_metrics['eval_accuracy']:.4f} ({test_metrics['eval_accuracy']*100:.2f}%)\n")
        f.write(f"  Precision: {test_metrics['eval_precision']:.4f}\n")
        f.write(f"  Recall:    {test_metrics['eval_recall']:.4f}\n")
        f.write(f"  F1 Score:  {test_metrics['eval_f1']:.4f}\n")
    
    print("\n" + "=" * 60)
    print("🎉 ALL DONE!")
    print("=" * 60)
    print(f"\nYour trained model is in: {OUTPUT_DIR}")
    print(f"Metrics saved to: {OUTPUT_DIR}/metrics.txt")
    print("\nNext steps:")
    print("1. Update streamlit_app.py to use the new model")
    print("2. Test predictions with the improved model")
    print("3. Compare with previous 60-76% accuracy model")
    
except Exception as e:
    print(f"\n❌ Training failed: {e}")
    import traceback
    traceback.print_exc()
    print("\nTroubleshooting:")
    print("1. Ensure dataset folder structure is correct")
    print("2. Check if images are valid")
    print("3. Try reducing batch size if out of memory")
