import re
import os
import pytesseract
from PIL import Image

# ✅ Set Tesseract path (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# -----------------------------
# Helper Function
# -----------------------------
def extract_value(text, pattern):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return None


# -----------------------------
# Main Analysis Function
# -----------------------------
def analyze_report(file_path):

    # ==============================
    # 📄 TEXT OR IMAGE DETECTION
    # ==============================

    if file_path.lower().endswith((".png", ".jpg", ".jpeg")):
        # Use OCR for images
        text = pytesseract.image_to_string(Image.open(file_path))
    else:
        # Read as text file
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    sections = []
    critical_flags = []
    total_risk_score = 0
    organ_scores = {
        "Hematology": 0,
        "Metabolic": 0,
        "Cardiovascular": 0,
        "Liver": 0,
        "Renal": 0
    }

    # =====================================================
    # 🩸 COMPLETE BLOOD COUNT
    # =====================================================

    cbc = []
    hemoglobin = extract_value(text, r"hemoglobin\s*[:\-]?\s*(\d+\.?\d*)")
    wbc = extract_value(text, r"\bwbc\b\s*[:\-]?\s*(\d+\.?\d*)")
    platelets = extract_value(text, r"platelets?\s*[:\-]?\s*(\d+\.?\d*)")

    if hemoglobin:
        if hemoglobin < 10:
            severity = "Severe Anemia"
            score = 15
            critical_flags.append("Severe anemia detected — urgent evaluation required.")
        elif hemoglobin < 12:
            severity = "Moderate Anemia"
            score = 8
        else:
            severity = "Normal"
            score = 0

        organ_scores["Hematology"] += score
        total_risk_score += score

        cbc.append(
            f"Hemoglobin: {hemoglobin} g/dL\n"
            f"Severity: {severity}\n"
            "Clinical Interpretation: Low hemoglobin reduces oxygen delivery to tissues.\n"
            "Possible Causes: Iron deficiency, chronic disease, blood loss.\n"
        )

    if wbc:
        if wbc > 11000:
            organ_scores["Hematology"] += 5
            total_risk_score += 5
            cbc.append(
                f"WBC: {wbc}/µL (Elevated)\n"
                "Interpretation: Suggestive of infection or inflammation.\n"
            )

    if platelets:
        if platelets < 150000:
            organ_scores["Hematology"] += 6
            total_risk_score += 6
            critical_flags.append("Low platelet count — bleeding risk.")
            cbc.append(
                f"Platelets: {platelets}/µL (Low)\n"
                "Clinical Risk: Increased bleeding tendency.\n"
            )

    if cbc:
        sections.append("=== COMPLETE BLOOD COUNT (CBC) ===\n" + "\n".join(cbc))

    # =====================================================
    # 🧪 METABOLIC PANEL
    # =====================================================

    metabolic = []
    glucose = extract_value(text, r"glucose\s*[:\-]?\s*(\d+\.?\d*)")
    creatinine = extract_value(text, r"creatinine\s*[:\-]?\s*(\d+\.?\d*)")
    hba1c = extract_value(text, r"hba1c\s*[:\-]?\s*(\d+\.?\d*)")

    if glucose:
        if glucose >= 200:
            severity = "Severe Hyperglycemia"
            score = 20
            critical_flags.append("Critical hyperglycemia detected.")
        elif glucose >= 126:
            severity = "Diabetic Range"
            score = 12
        elif glucose >= 100:
            severity = "Prediabetes"
            score = 6
        else:
            severity = "Normal"
            score = 0

        organ_scores["Metabolic"] += score
        total_risk_score += score

        metabolic.append(
            f"Fasting Glucose: {glucose} mg/dL\n"
            f"Assessment: {severity}\n"
            "Persistent elevation increases cardiovascular & renal risk.\n"
        )

    if hba1c:
        if hba1c >= 6.5:
            organ_scores["Metabolic"] += 10
            total_risk_score += 10
            metabolic.append(
                f"HbA1c: {hba1c}%\n"
                "Indicates chronic hyperglycemia over last 2–3 months.\n"
            )

    if creatinine:
        if creatinine > 1.5:
            organ_scores["Renal"] += 12
            total_risk_score += 12
            critical_flags.append("Renal function impairment suspected.")
            metabolic.append(
                f"Creatinine: {creatinine} mg/dL\n"
                "Possible kidney dysfunction — recommend eGFR assessment.\n"
            )

    if metabolic:
        sections.append("=== METABOLIC PANEL ===\n" + "\n".join(metabolic))

    # =====================================================
    # ❤️ LIPID PROFILE
    # =====================================================

    lipid = []
    cholesterol = extract_value(text, r"cholesterol\s*[:\-]?\s*(\d+\.?\d*)")
    ldl = extract_value(text, r"\bldl\b\s*[:\-]?\s*(\d+\.?\d*)")
    hdl = extract_value(text, r"\bhdl\b\s*[:\-]?\s*(\d+\.?\d*)")

    if cholesterol:
        if cholesterol > 240:
            severity = "High Risk"
            score = 12
        elif cholesterol > 200:
            severity = "Borderline High"
            score = 6
        else:
            severity = "Normal"
            score = 0

        organ_scores["Cardiovascular"] += score
        total_risk_score += score

        lipid.append(
            f"Total Cholesterol: {cholesterol} mg/dL\n"
            f"Risk Category: {severity}\n"
            "Elevated levels increase atherosclerotic risk.\n"
        )

    if ldl and ldl > 160:
        organ_scores["Cardiovascular"] += 8
        total_risk_score += 8
        lipid.append(f"LDL: {ldl} mg/dL (High)\n")

    if hdl and hdl < 40:
        organ_scores["Cardiovascular"] += 5
        total_risk_score += 5
        lipid.append(f"HDL: {hdl} mg/dL (Low — reduced cardioprotection)\n")

    if lipid:
        sections.append("=== LIPID PROFILE ===\n" + "\n".join(lipid))

    # =====================================================
    # 🧠 FINAL RISK SCORING
    # =====================================================

    if total_risk_score < 15:
        overall = "Low Risk"
    elif total_risk_score < 35:
        overall = "Moderate Risk"
    else:
        overall = "High Risk"

    final_summary = (
        "\n=== ORGAN SYSTEM RISK SCORES ===\n" +
        "\n".join([f"{k}: {v}" for k, v in organ_scores.items()]) +
        f"\n\nOverall Health Risk Score: {total_risk_score} / 100\n"
        f"Risk Category: {overall}\n"
    )

    if critical_flags:
        final_summary += "\n⚠ CRITICAL ALERTS:\n" + "\n".join(critical_flags)

    final_summary += (
        "\n\nClinical Summary:\n"
        "Laboratory abnormalities require physician correlation. "
        "Early intervention may reduce long-term complications.\n\n"
        "Disclaimer: AI-generated analysis — not a substitute for professional diagnosis."
    )

    sections.append(final_summary)

    return {
        "detailed_report": "\n\n".join(sections),
        "overall_score": total_risk_score,
        "risk_category": overall
    }