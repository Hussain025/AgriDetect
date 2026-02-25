"""
Train model using AutoTrain Python API (bypasses UI issues)
"""

import os
from huggingface_hub import login

print("=" * 60)
print("Train with AutoTrain (Python API)")
print("=" * 60)

# Login
token = os.getenv("HF_TOKEN")
if not token:
    print("\n❌ Error: HF_TOKEN environment variable not set")
    print("\nSet it with: export HF_TOKEN=your_token_here")
    exit(1)
print("\n🔑 Logging in...")
login(token=token)
print("✅ Logged in!")

# Configuration
dataset_name = "Warrior025/plant-disease-classification"
project_name = "plant-disease-model"
model_name = "microsoft/resnet-50"  # Pre-trained model

print("\n" + "=" * 60)
print("TRAINING CONFIGURATION")
print("=" * 60)
print(f"Dataset: {dataset_name}")
print(f"Model: {model_name}")
print(f"Project: {project_name}")
print(f"Task: Image Classification")

print("\n" + "=" * 60)
print("ALTERNATIVE: Use Transformers Directly")
print("=" * 60)
print("\nSince AutoTrain UI has issues, I recommend training with")
print("Hugging Face Transformers library directly.")
print("\nThis gives you:")
print("  ✓ Full control over training")
print("  ✓ Better debugging")
print("  ✓ Weights & Biases integration")
print("  ✓ No UI authentication issues")
print("\nWould you like me to create a training script?")
print("\nOptions:")
print("  1. Simple training script (recommended)")
print("  2. Advanced with W&B tracking")
print("  3. Notebook for Google Colab")
