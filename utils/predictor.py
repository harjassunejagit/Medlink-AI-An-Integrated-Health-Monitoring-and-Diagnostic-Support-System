import joblib
import pandas as pd
import os
import numpy as np

MODEL_PATH = os.path.join("models", "heart_disease_model.pkl")

saved = joblib.load(MODEL_PATH)

model = saved["model"]
scaler = saved["scaler"]

def predict_disease(data):
    try:
        input_data = pd.DataFrame([[
            float(data["age"]),
            float(data["sex"]),
            float(data["cp"]),
            float(data["trestbps"]),
            float(data["chol"]),
            float(data["fbs"]),
            float(data["restecg"]),
            float(data["thalach"]),
            float(data["exang"]),
            float(data["oldpeak"]),
            float(data["slope"]),
            float(data["ca"]),
            float(data["thal"])
        ]], columns=[
            "age","sex","cp","trestbps","chol",
            "fbs","restecg","thalach","exang",
            "oldpeak","slope","ca","thal"
        ])

        input_scaled = scaler.transform(input_data)

        probability = float(model.predict_proba(input_scaled)[0][0])
        confidence = round(probability * 100, 2)

        # --- Risk Stratification ---
        if probability < 0.35:
            risk_level = "Low Risk"
            explanation = "Cardiovascular parameters fall within relatively safe clinical ranges."
        elif probability < 0.65:
            risk_level = "Moderate Risk"
            explanation = "Some parameters indicate elevated cardiovascular stress. Preventive evaluation recommended."
        else:
            risk_level = "High Risk"
            explanation = "Strong pattern similarity with patients diagnosed with heart disease. Immediate medical consultation advised."

        return {
            "prediction": risk_level,
            "confidence_percentage": confidence,
            "probability_score": probability,
            "explanation": explanation
        }

    except Exception as e:
        return {"error": str(e)}
