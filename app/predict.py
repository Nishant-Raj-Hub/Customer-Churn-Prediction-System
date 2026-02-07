from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
pipeline = joblib.load(BASE_DIR.parent / "model" / "churn_pipeline.pkl")


def predict_churn(user_input: dict):
    df = pd.DataFrame([user_input])

    prob = pipeline.predict_proba(df)[0][1]

    if prob >= 0.6:
        risk = "High"
    elif prob >= 0.3:
        risk = "Medium"
    else:
        risk = "Low"

    return round(prob, 2), risk
