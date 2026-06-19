<div align="center">

<img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/XGBoost-92.13%25_Acc-FF6600?style=for-the-badge"/>
<img src="https://img.shields.io/badge/NLP-Sentence_Transformers-8A2BE2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/OCR-Tesseract-4CAF50?style=for-the-badge"/>

# 🏥 Medlink AI

### An Integrated Health Monitoring & Diagnostic Support System

**AI-driven web platform combining ML prediction · NLP chatbot · OCR report analysis · geolocation**


[Features](#-features) • [Demo](#-modules-at-a-glance) • [Architecture](#-system-architecture) • [Results](#-model-performance) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) 

</div>

---

## 📖 Overview

Medlink AI is a **full-stack intelligent healthcare assistance platform** that brings hospital-grade medical intelligence to any web browser. It combines four AI-powered modules into a single unified system:

| Module | Technology | Metric |
|--------|-----------|--------|
| 🫀 **Heart Disease Predictor** | XGBoost + UCI Dataset | **92.13% accuracy · 0.9601 AUC-ROC** |
| 🤖 **Medical Chatbot** | Sentence Transformers (all-MiniLM-L6-v2) | **88.8% queries above confidence threshold** |
| 📄 **Lab Report Analyzer** | Tesseract OCR + Rule-Based NLP | 9 biomarkers · 3-tier risk stratification |
| 📍 **Clinic Finder** | OpenStreetMap Overpass API | Sub-kilometer precision · real-time |

> ⚠️ **Medical Disclaimer:** Medlink AI is a clinical decision-support tool. All outputs are supplementary to, and not substitutes for, professional medical diagnosis.

---

## ✨ Features

- 🫀 **Cardiovascular Risk Prediction** — Input 13 clinical parameters and receive Low / Moderate / High risk classification with probability scores
- 🤖 **Semantic Medical Chatbot** — Ask health questions in natural language; retrieves answers from a 10,000-pair physician dialogue corpus using cosine similarity
- 📄 **Medical Report Analyzer** — Upload a lab report image or PDF; automatically extracts glucose, hemoglobin, cholesterol, creatinine, LDL, HDL, triglycerides, blood pressure, and platelet count, then generates a clinical risk summary
- 📍 **Nearby Clinic Finder** — Finds hospitals and clinics within a configurable radius using your real-time GPS location
- 🔐 **Secure Authentication** — Role-based access control, encrypted password storage, session management
- 📊 **Admin Dashboard** — Monitor platform usage and user activity
- ⚡ **Lightweight Deployment** — Runs on a standard Flask server; no GPU or cloud-scale infrastructure required

---

## 🖥️ Modules At A Glance

### 🫀 Module 1 — Heart Disease Risk Predictor
Enter 13 clinical features (age, chest pain type, cholesterol, resting blood pressure, etc.) and receive:
- Probability score of cardiovascular disease
- Risk category: **Low** (<35%) · **Moderate** (35–65%) · **High** (>65%)
- Key contributing risk factors highlighted

### 🤖 Module 2 — AI Medical Chatbot
Ask any health question in plain English:
- Powered by `all-MiniLM-L6-v2` Sentence Transformer
- Matches your query to the most semantically similar physician response using cosine similarity
- Falls back to a professional consultation advisory if confidence score < 0.30

### 📄 Module 3 — Medical Report Analyzer
Upload a lab report (JPG, PNG, or PDF):
1. Image preprocessing (grayscale → noise reduction → adaptive thresholding)
2. Tesseract OCR text extraction
3. Regex-based biomarker detection (9 parameters)
4. Weighted composite risk score → Low / Moderate / High classification

### 📍 Module 4 — Nearby Clinic Finder
Share your location and find:
- Hospitals, clinics, and pharmacies near you
- Sorted by Haversine geodesic distance
- Rendered on an interactive OpenStreetMap view

---

## 🏛️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE LAYER                     │
│              Web Browser (HTML/CSS/JavaScript)              │
└───────────────────────┬─────────────────────────────────────┘
                        │ HTTP / REST API (JSON)
┌───────────────────────▼─────────────────────────────────────┐
│                  APPLICATION LAYER (Flask)                  │
│   Auth & Session │ Route Handlers │ API Controllers         │
└──────┬───────────┬──────────────┬──────────────┬────────────┘
       │           │              │              │
┌──────▼──┐  ┌─────▼──┐  ┌───────▼──┐  ┌───────▼──────────┐
│ Medical │  │ Heart  │  │ Report   │  │ Clinic           │
│ Chatbot │  │ Disease│  │ Analyzer │  │ Finder           │
│ Module  │  │ Module │  │ Module   │  │ Module           │
│         │  │        │  │          │  │                  │
│Sentence │  │XGBoost │  │Tesseract │  │OpenStreetMap     │
│Transform│  │Classifier  │OCR+Regex│  │Overpass API      │
└──────┬──┘  └─────┬──┘  └───────┬──┘  └───────┬──────────┘
       └───────────┴──────────────┴──────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────┐
│                     DATA LAYER                              │
│  SQLite DB  │  Serialized ML Models  │  Embedding Store     │
└─────────────────────────────────────────────────────────────┘
```

The platform follows **MVC + Layered Architecture** deployed on a Flask WSGI server:
- **Presentation Layer** — Browser-based frontend
- **Application Layer** — Flask routing, auth, REST endpoints
- **AI/ML Layer** — Four independent intelligent modules
- **Data Layer** — SQLite, pickled models, filesystem
- **External Services** — OpenStreetMap, Sentence Transformer Hub

---

## 📊 Model Performance

### Heart Disease Predictor (XGBoost)

| Metric | Score |
|--------|-------|
| **Accuracy** | **92.13%** |
| **AUC-ROC** | **0.9601** |
| F1-Score | 0.9214 |
| Precision | 0.9163 |
| Recall | 0.8980 |
| CV Mean Accuracy (5-fold) | 0.9213 ± 0.0083 |
| True Positives | 44 / 49 |
| True Negatives | 47 / 51 |

### Comparison Against Prior Work (UCI Cleveland Dataset)

| Method | Accuracy |
|--------|----------|
| Logistic Regression | 84.72% |
| Decision Tree | 82.16% |
| SVM | 88.94% |
| Random Forest (Mohan et al.) | 89.35% |
| Stacking Ensemble (Shah et al.) | 90.80% |
| **Medlink XGBoost (Ours)** | **92.13%** ✅ |

### Top Predictive Features (Feature Importance)
1. 🩸 **Thalassemia type** — 0.241
2. 🫀 **Major vessels count** — 0.188
3. 💢 **Chest pain type** — 0.154
4. 💓 **Max heart rate achieved** — 0.121
5. ⚡ **ST depression (oldpeak)** — 0.098

### Medical Chatbot Performance
- Test queries evaluated: **900**
- Queries above confidence threshold (0.30): **88.8%**
- Majority similarity scores: **0.65 – 0.80 range**
- Fallback rate: **11.2%**

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Flask (Python) |
| **ML Model** | XGBoost |
| **NLP / Embeddings** | Sentence Transformers (`all-MiniLM-L6-v2`) |
| **Similarity Search** | Cosine Similarity (scikit-learn) |
| **OCR Engine** | Tesseract OCR |
| **Image Processing** | OpenCV, Pillow |
| **Geolocation** | OpenStreetMap Overpass API |
| **Distance Calculation** | Haversine formula |
| **Database** | SQLite |
| **Data Processing** | pandas, NumPy, scikit-learn |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Authentication** | Flask-Login, bcrypt |
| **Model Serialization** | joblib / pickle |

---

## 📁 Project Structure

```
medlink-ai/
│
├── app.py                      # Flask application entry point
├── config.py                   # Configuration settings
│
├── models/
│   ├── heart_model.pkl         # Trained XGBoost model
│   ├── scaler.pkl              # StandardScaler for feature normalization
│   └── chatbot_embeddings.pkl  # Pre-encoded dialogue embeddings
│
├── modules/
│   ├── chatbot/
│   │   ├── chatbot.py          # Semantic retrieval logic
│   │   └── medical_qa.json     # 10,000-pair Q&A corpus
│   ├── heart_disease/
│   │   ├── predictor.py        # XGBoost inference pipeline
│   │   └── train.py            # Model training script
│   ├── report_analyzer/
│   │   ├── ocr.py              # Tesseract OCR + preprocessing
│   │   ├── extractor.py        # Regex biomarker extraction
│   │   └── risk_scorer.py      # Weighted risk aggregation
│   └── clinic_finder/
│       └── geolocation.py      # Overpass API + Haversine ranking
│
├── auth/
│   ├── routes.py               # Login, register, logout routes
│   └── models.py               # User model (SQLite)
│
├── templates/                  # Jinja2 HTML templates
│   ├── index.html
│   ├── chatbot.html
│   ├── heart_disease.html
│   ├── report_analyzer.html
│   ├── clinic_finder.html
│   └── dashboard.html
│
├── static/                     # CSS, JS, images
│
├── training/
│   └── train_heart_model.py    # Offline training pipeline
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.9+
- Tesseract OCR engine installed on your system

**Install Tesseract:**
```bash
# Ubuntu / Debian
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract

# Windows
# Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
```

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/medlink-ai.git
cd medlink-ai

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the heart disease model (one-time setup)
python training/train_heart_model.py

# 5. Initialize the database
flask db init
flask db migrate
flask db upgrade

# 6. Run the application
python app.py
```

Visit **http://localhost:5000** in your browser.

---

## 🚀 Usage

### Heart Disease Prediction
```
1. Navigate to /heart-disease
2. Enter 13 clinical parameters:
   age, sex, chest pain type, resting BP, cholesterol,
   fasting blood sugar, resting ECG, max heart rate,
   exercise angina, ST depression, ST slope,
   major vessels, thalassemia type
3. Click "Predict Risk"
4. Receive: probability score + Low/Moderate/High classification
```

### Medical Chatbot
```
1. Navigate to /chatbot
2. Type your health question in natural language
   Example: "What are the symptoms of high blood pressure?"
3. Receive: most semantically matched physician response
```

### Report Analyzer
```
1. Navigate to /report-analyzer
2. Upload your lab report (JPG, PNG, or PDF)
3. System extracts: glucose, hemoglobin, cholesterol,
   triglycerides, creatinine, BP, HDL, LDL, platelets
4. Receive: per-biomarker status + composite risk score
```

### Clinic Finder
```
1. Navigate to /clinic-finder
2. Allow browser location access
3. Set search radius (default: 5km)
4. View nearby hospitals and clinics sorted by distance
```

---

## 🔬 Algorithms

### Semantic Retrieval (Chatbot)
```
Input:  User query q, embedding database D = {d₁, d₂, ..., dₙ}
Output: Best-matched physician response r*

1. Encode q using Sentence Transformer → embedding vector eᵢ
2. For each stored embedding eᵢ ∈ D:
      Sᵢ = (eᵢ · eᵢ) / (‖eᵢ‖ · ‖eᵢ‖)   [cosine similarity]
3. k = argmax(Sᵢ)
4. If Sₖ ≥ τ (0.30): return response rₖ
   Else: return fallback medical disclaimer
```

### Cardiovascular Risk Stratification
```
Input:  Clinical feature vector X
Output: Risk category R

1. Normalize X using saved StandardScaler
2. Compute p = P(y=1|X) using XGBoost ensemble
3. Assign risk:
   p < 0.35  → Low Risk
   p < 0.65  → Moderate Risk
   p ≥ 0.65  → High Risk
```

### Clinical Risk Aggregation (Report Analyzer)
```
Input:  Extracted report text T
Output: Composite health risk score R

1. Extract biomarkers using regex patterns
2. Compare each bᵢ against clinical threshold θᵢ
3. R = Σ wᵢ · rᵢ  (weighted sum)
4. Normalize R to [0, 100]
5. R < 15 → Low | 15 ≤ R < 35 → Moderate | R ≥ 35 → High
```

---

## 🗺️ Roadmap

- [ ] Real-time ECG signal analysis module
- [ ] Federated learning for privacy-preserving model updates
- [ ] Expansion of report analyzer to include cardiac troponin and thyroid panels
- [ ] Mobile application (React Native)
- [ ] Cloud deployment (AWS / GCP)
- [ ] Longitudinal clinical validation study
- [ ] Multi-language chatbot support
- [ ] Integration with electronic health record (EHR) systems

---

## ⚠️ Limitations

- Heart disease model trained on UCI Cleveland dataset (303 samples) — limited demographic diversity
- OCR accuracy decreases for handwritten or low-quality scanned documents
- Chatbot knowledge base may not cover rare or highly specialized medical conditions
- No real-time hospital integration or live health data feeds
- Not validated in clinical settings with real patients — should not replace professional diagnosis

---

## 🤝 Contributing

Contributions are welcome! Here are ways you can help:

## 👨‍💻 Author

Harjas Suneja
