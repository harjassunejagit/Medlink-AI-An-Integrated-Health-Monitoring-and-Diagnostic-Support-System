import joblib
from sentence_transformers import SentenceTransformer, util
import torch
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "chatbot_model.pkl")

# Load model + embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
questions, answers, embeddings = joblib.load(MODEL_PATH)

def chatbot_response(user_input):
    query_embedding = model.encode(user_input, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, embeddings)
    best_match = torch.argmax(scores)
    confidence = torch.max(scores).item()

    # Optional: Confidence threshold
    if confidence < 0.3:
        return "I'm not fully confident. Please consult a healthcare professional."

    return answers[best_match]
import joblib
from sentence_transformers import SentenceTransformer, util
import torch
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "chatbot_model.pkl")

# Load model + embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
questions, answers, embeddings = joblib.load(MODEL_PATH)

def chatbot_response(user_input):
    query_embedding = model.encode(user_input, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, embeddings)
    best_match = torch.argmax(scores)
    confidence = torch.max(scores).item()

    # Optional: Confidence threshold
    if confidence < 0.3:
        return "I'm not fully confident. Please consult a healthcare professional."

    return answers[best_match]
