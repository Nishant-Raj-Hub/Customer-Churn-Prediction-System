# 📉 Customer Churn Prediction System (End-to-End ML + AI)

## Overview

This project is a **production-ready Customer Churn Prediction System** that predicts churn risk and explains why a customer may churn along with recommended retention actions.

Unlike basic ML notebooks, this system is built end-to-end:

- Data preprocessing
- Model training & evaluation
- Explainability
- Streamlit frontend
- AI-generated business insights (based on prediction)

## 🔍 Problem Statement

Customer churn is expensive.  
The goal is to identify customers at risk of churn early and suggest actions to retain them, not just output a binary prediction.

## 🧠 Solution Architecture

```
User Input (Streamlit UI)
        ↓
Preprocessing Pipeline
        ↓
Logistic Regression (Churn Probability)
        ↓
Feature-based Churn Drivers
        ↓
LLM → Explanation + Retention Actions
```

## 🧪 Tech Stack

- Python
- scikit-learn
- pandas / numpy
- Streamlit
- Groq LLM API
- joblib

## 📊 Example Output

**Churn Probability:** 0.68

**Risk Level:** High

**Why this customer may churn:**

- Month-to-month contract
- High monthly charges
- Fiber optic internet without support services

**Recommended Actions:**

- Offer a long-term contract discount
- Provide free tech support trial
- Adjust pricing or bundle services


## 📁 Project Structure

```
Customer Churn Prediction/
│
├── app/
│   ├── app.py              # Streamlit frontend
│   ├── predict.py          # Model inference
│   ├── insights.py         # Feature-based churn drivers
│   ├── llm_client.py       # LLM integration (Groq)
│
├── model/
│   └── churn_pipeline.pkl  # Trained ML pipeline
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── notebooks/
│   └── Customer Churn Prediction.ipynb
│
├── requirements.txt
└── README.md
```

## 📈 What This Project Demonstrates

- End-to-end ML system design
- Model interpretability and business alignment
- Safe ML deployment using pipelines
- Practical use of LLMs with ML predictions
- Product-oriented thinking (not just accuracy)
