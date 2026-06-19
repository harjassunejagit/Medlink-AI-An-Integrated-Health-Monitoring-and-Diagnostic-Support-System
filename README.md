🏥 Medlink AI

An Integrated Health Monitoring & Diagnostic Support System
Medlink AI is an intelligent healthcare platform that provides **real-time medical insights** by integrating **machine learning, NLP, and OCR**. It assists users with symptom analysis, disease prediction, medical report understanding, and healthcare recommendations.

AI-driven web platform combining ML prediction · NLP chatbot · OCR report analysis · geolocation

Published at ICSSIT — Vellore Institute of Technology, Chennai

Features • Demo • Architecture • Results • Installation • Usage • Tech Stack • Research


📖 Overview

Medlink AI is a full-stack intelligent healthcare assistance platform that brings hospital-grade medical intelligence to any web browser. It combines four AI-powered modules into a single unified system:

ModuleTechnologyMetric🫀 Heart Disease PredictorXGBoost + UCI Dataset92.13% accuracy · 0.9601 AUC-ROC🤖 Medical ChatbotSentence Transformers (all-MiniLM-L6-v2)88.8% queries above confidence threshold📄 Lab Report AnalyzerTesseract OCR + Rule-Based NLP9 biomarkers · 3-tier risk stratification📍 Clinic FinderOpenStreetMap Overpass APISub-kilometer precision · real-time
- 🤖 **AI Medical Chatbot**  
  Provides conversational health guidance using NLP (OpenAI API)

- ❤️ **Disease Prediction System**  
  Predicts heart disease risk using XGBoost with optimized ML pipeline  

- 📄 **Medical Report Analyzer**  
  Extracts and interprets data from reports using Tesseract OCR + NLP  

- 🏥 **Hospital Recommendation Engine**  
  Suggests nearby healthcare facilities based on user context  

- ⚡ **Real-Time Diagnostic Support**  
  Integrated AI system delivering fast and actionable insights  


⚠️ Medical Disclaimer: Medlink AI is a clinical decision-support tool. All outputs are supplementary to, and not substitutes for, professional medical diagnosis.



✨ Features

## 📊 System Workflow

1. User inputs symptoms or uploads medical reports  
2. OCR extracts relevant medical information  
3. ML models analyze disease risk  
4. Chatbot provides intelligent medical guidance  
5. System suggests hospitals and next steps  

🫀 Cardiovascular Risk Prediction — Input 13 clinical parameters and receive Low / Moderate / High risk classification with probability scores
🤖 Semantic Medical Chatbot — Ask health questions in natural language; retrieves answers from a 10,000-pair physician dialogue corpus using cosine similarity
📄 Medical Report Analyzer — Upload a lab report image or PDF; automatically extracts glucose, hemoglobin, cholesterol, creatinine, LDL, HDL, triglycerides, blood pressure, and platelet count, then generates a clinical risk summary
📍 Nearby Clinic Finder — Finds hospitals and clinics within a configurable radius using your real-time GPS location
🔐 Secure Authentication — Role-based access control, encrypted password storage, session management
📊 Admin Dashboard — Monitor platform usage and user activity
⚡ Lightweight Deployment — Runs on a standard Flask server; no GPU or cloud-scale infrastructure required


- Accurate disease risk prediction using optimized ML models  
- Automated report analysis reducing manual effort  
- Unified AI pipeline for efficient healthcare decision support  

🖥️ Modules At A Glance

🫀 Module 1 — Heart Disease Risk Predictor

Enter 13 clinical features (age, chest pain type, cholesterol, resting blood pressure, etc.) and receive:


Probability score of cardiovascular disease
Risk category: Low (<35%) · Moderate (35–65%) · High (>65%)
Key contributing risk factors highlighted


🤖 Module 2 — AI Medical Chatbot

Ask any health question in plain English:


Powered by all-MiniLM-L6-v2 Sentence Transformer
Matches your query to the most semantically similar physician response using cosine similarity
Falls back to a professional consultation advisory if confidence score < 0.30


📄 Module 3 — Medical Report Analyzer

Upload a lab report (JPG, PNG, or PDF):


Image preprocessing (grayscale → noise reduction → adaptive thresholding)
Tesseract OCR text extraction
Regex-based biomarker detection (9 parameters)
Weighted composite risk score → Low / Moderate / High classification


📍 Module 4 — Nearby Clinic Finder

Share your location and find:


Hospitals, clinics, and pharmacies near you
Sorted by Haversine geodesic distance
Rendered on an interactive OpenStreetMap view



🏛️ System Architecture

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

The platform follows MVC + Layered Architecture deployed on a Flask WSGI server:


Presentation Layer — Browser-based frontend
Application Layer — Flask routing, auth, REST endpoints
AI/ML Layer — Four independent intelligent modules
Data Layer — SQLite, pickled models, filesystem
External Services — OpenStreetMap, Sentence Transformer Hub



📊 Model Performance

Heart Disease Predictor (XGBoost)

MetricScoreAccuracy92.13%AUC-ROC0.9601F1-Score0.9214Precision0.9163Recall0.8980CV Mean Accuracy (5-fold)0.9213 ± 0.0083True Positives44 / 49True Negatives47 / 51

Comparison Against Prior Work (UCI Cleveland Dataset)

MethodAccuracyLogistic Regression84.72%Decision Tree82.16%SVM88.94%Random Forest (Mohan et al.)89.35%Stacking Ensemble (Shah et al.)90.80%Medlink XGBoost (Ours)92.13% ✅

Top Predictive Features (Feature Importance)


🩸 Thalassemia type — 0.241
🫀 Major vessels count — 0.188
💢 Chest pain type — 0.154
💓 Max heart rate achieved — 0.121
⚡ ST depression (oldpeak) — 0.098


Medical Chatbot Performance


Test queries evaluated: 900
Queries above confidence threshold (0.30): 88.8%
Majority similarity scores: 0.65 – 0.80 range
Fallback rate: 11.2%



🛠️ Tech Stack

ComponentTechnologyBackend FrameworkFlask (Python)ML ModelXGBoostNLP / EmbeddingsSentence Transformers (all-MiniLM-L6-v2)Similarity SearchCosine Similarity (scikit-learn)OCR EngineTesseract OCRImage ProcessingOpenCV, PillowGeolocationOpenStreetMap Overpass APIDistance CalculationHaversine formulaDatabaseSQLiteData Processingpandas, NumPy, scikit-learnFrontendHTML5, CSS3, JavaScriptAuthenticationFlask-Login, bcryptModel Serializationjoblib / pickle


📁 Project Structure

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


⚙️ Installation

Prerequisites


Python 3.9+
Tesseract OCR engine installed on your system


Install Tesseract:

bash# Ubuntu / Debian
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract

# Windows
# Download installer from: https://github.com/UB-Mannheim/tesseract/wiki

Setup

bash# 1. Clone the repository
git clone https://github.com/yourusername/medlink-ai.git
cd medlink-ai

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
## ⚙️ Installation & Setup

```bash
git clone https://github.com/harjassunejagit/Medlink-AI-An-Integrated-Health-Monitoring-and-Diagnostic-Support-System.git
cd Medlink-AI-An-Integrated-Health-Monitoring-and-Diagnostic-Support-System
pip install -r requirements.txt

# 4. Train the heart disease model (one-time setup)
python training/train_heart_model.py

# 5. Initialize the database
flask db init
flask db migrate
flask db upgrade

# 6. Run the application
python app.py

Visit http://localhost:5000 in your browser.


🚀 Usage

Heart Disease Prediction

1. Navigate to /heart-disease
2. Enter 13 clinical parameters:
   age, sex, chest pain type, resting BP, cholesterol,
   fasting blood sugar, resting ECG, max heart rate,
   exercise angina, ST depression, ST slope,
   major vessels, thalassemia type
3. Click "Predict Risk"
4. Receive: probability score + Low/Moderate/High classification

Medical Chatbot

1. Navigate to /chatbot
2. Type your health question in natural language
   Example: "What are the symptoms of high blood pressure?"
3. Receive: most semantically matched physician response

Report Analyzer

1. Navigate to /report-analyzer
2. Upload your lab report (JPG, PNG, or PDF)
3. System extracts: glucose, hemoglobin, cholesterol,
   triglycerides, creatinine, BP, HDL, LDL, platelets
4. Receive: per-biomarker status + composite risk score

Clinic Finder

1. Navigate to /clinic-finder
2. Allow browser location access
3. Set search radius (default: 5km)
4. View nearby hospitals and clinics sorted by distance


🔬 Algorithms

Semantic Retrieval (Chatbot)

Input:  User query q, embedding database D = {d₁, d₂, ..., dₙ}
Output: Best-matched physician response r*

1. Encode q using Sentence Transformer → embedding vector eᵢ
2. For each stored embedding eᵢ ∈ D:
      Sᵢ = (eᵢ · eᵢ) / (‖eᵢ‖ · ‖eᵢ‖)   [cosine similarity]
3. k = argmax(Sᵢ)
4. If Sₖ ≥ τ (0.30): return response rₖ
   Else: return fallback medical disclaimer

Cardiovascular Risk Stratification

Input:  Clinical feature vector X
Output: Risk category R

1. Normalize X using saved StandardScaler
2. Compute p = P(y=1|X) using XGBoost ensemble
3. Assign risk:
   p < 0.35  → Low Risk
   p < 0.65  → Moderate Risk
   p ≥ 0.65  → High Risk

Clinical Risk Aggregation (Report Analyzer)

Input:  Extracted report text T
Output: Composite health risk score R

1. Extract biomarkers using regex patterns
2. Compare each bᵢ against clinical threshold θᵢ
3. R = Σ wᵢ · rᵢ  (weighted sum)
4. Normalize R to [0, 100]
5. R < 15 → Low | 15 ≤ R < 35 → Moderate | R ≥ 35 → High


📋 Requirements

txtflask>=2.3
flask-login
flask-sqlalchemy
xgboost>=1.7
scikit-learn>=1.3
sentence-transformers>=2.2
pandas>=2.0
numpy>=1.24
pytesseract>=0.3
opencv-python>=4.8
Pillow>=10.0
requests>=2.31
bcrypt>=4.0
joblib>=1.3


Key findings:


XGBoost achieves 92.13% accuracy and 0.9601 AUC-ROC — outperforming all compared methods on UCI Cleveland dataset
Sentence Transformer semantic retrieval achieves 88.8% query confidence rate on 900 test queries
System delivers end-to-end response in < 2 seconds for prediction and chatbot; 3–5 seconds for report analysis
Full platform runs on standard Flask server — no GPU or cloud infrastructure required



🗺️ Roadmap


 Real-time ECG signal analysis module
 Federated learning for privacy-preserving model updates
 Expansion of report analyzer to include cardiac troponin and thyroid panels
 Mobile application (React Native)
 Cloud deployment (AWS / GCP)
 Longitudinal clinical validation study
 Multi-language chatbot support
 Integration with electronic health record (EHR) systems



⚠️ Limitations


Heart disease model trained on UCI Cleveland dataset (303 samples) — limited demographic diversity
OCR accuracy decreases for handwritten or low-quality scanned documents
Chatbot knowledge base may not cover rare or highly specialized medical conditions
No real-time hospital integration or live health data feeds
Not validated in clinical settings with real patients — should not replace professional diagnosis



🤝 Contributing

Contributions are welcome! Here are ways you can help:


🐛 Report bugs via Issues
💡 Suggest features or improvements
📊 Contribute larger/more diverse clinical datasets
🌐 Add more languages to the chatbot corpus
🧪 Write unit tests

👨‍💻 Author

Harjas Suneja