import pandas as pd
import joblib
from sentence_transformers import SentenceTransformer
import torch
import os

print("Loading dataset...")
df = pd.read_csv("ai-medical-chatbot.csv")

print("Original size:", df.shape)

# Use only needed columns
df = df[["Patient", "Doctor"]].dropna()

# Reduce dataset for faster training
df = df.sample(10000, random_state=42)

print("Training size:", df.shape)

questions = df["Patient"].astype(str).tolist()
answers = df["Doctor"].astype(str).tolist()

print("Loading transformer model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

print("Encoding questions...")
embeddings = model.encode(
    questions,
    convert_to_tensor=True,
    show_progress_bar=True,
    batch_size=64
)

print("Saving model...")
joblib.dump((questions, answers, embeddings), "chatbot_model.pkl")

print("✅ Transformer chatbot trained successfully.")
