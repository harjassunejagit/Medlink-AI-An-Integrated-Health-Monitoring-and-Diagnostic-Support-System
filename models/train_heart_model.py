import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

# -----------------------
# Load Dataset
# -----------------------
df = pd.read_csv("heart.csv")

X = df.drop("target", axis=1)
y = df["target"]

# -----------------------
# Train/Test Split
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------
# Scaling
# -----------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------
# XGBoost Model
# -----------------------
model = XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss",
    random_state=42
)

# -----------------------
# Cross Validation
# -----------------------
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
print("Cross Validation Accuracy:", cv_scores.mean())

# -----------------------
# Train Model
# -----------------------
model.fit(X_train_scaled, y_train)

# -----------------------
# Evaluate
# -----------------------
y_pred = model.predict(X_test_scaled)

print("\nTest Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------
# Feature Importance Plot
# -----------------------
importance = model.feature_importances_
features = X.columns

plt.figure(figsize=(10,6))
plt.barh(features, importance)
plt.xlabel("Importance Score")
plt.title("Feature Importance - Heart Disease Model")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()

print("Feature importance chart saved.")

# -----------------------
# Save Model
# -----------------------
joblib.dump({
    "model": model,
    "scaler": scaler
}, "heart_disease_model.pkl")

print("\n🔥 Optimized Heart Disease Model Trained Successfully.")
