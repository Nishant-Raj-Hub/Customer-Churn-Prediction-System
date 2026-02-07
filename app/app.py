import streamlit as st
from predict import predict_churn
from insights import extract_churn_drivers
from llm_client import generate_actions

st.set_page_config(
    page_title="Customer Churn Predictor",
    layout="centered"
)

st.title("📉 Customer Churn Prediction System")
st.write("Enter customer details to predict churn risk")

# ==============================
# USER INPUTS
# ==============================

gender = st.selectbox("Gender", ["Male", "Female"])

senior = st.selectbox("Senior Citizen", ["Yes", "No"])

partner = st.selectbox("Has Partner?", ["Yes", "No"])

dependents = st.selectbox("Has Dependents?", ["Yes", "No"])

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=100,
    value=12
)

phone_service = st.selectbox("Phone Service", ["Yes", "No"])

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox("Paperless Billing", ["Yes", "No"])

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    max_value=10000.0,
    value=800.0
)

# ==============================
# PACKAGE INPUT DATA
# ==============================

user_data = {
    "gender": gender,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges
}

# ==============================
# PREDICTION
# ==============================

if st.button("Predict Churn Risk"):
    prob, risk = predict_churn(user_data)
    drivers = extract_churn_drivers(user_data)
    explanation, actions = generate_actions(risk, prob, drivers)

    st.subheader("🔍 Prediction Result")
    st.write(f"**Churn Probability:** {prob}")

    if risk == "High":
        st.error("⚠️ High Risk of Churn")
    elif risk == "Medium":
        st.warning("⚠️ Medium Risk of Churn")
    else:
        st.success("✅ Low Risk of Churn")

    st.subheader("📌 Why this customer may churn")
    st.write(explanation)

    st.subheader("🛠 Recommended Actions")
    for a in actions:
        st.write("•", a)














# import streamlit as st
# from predict import predict_churn
# from insights import extract_churn_drivers
# from llm_client import generate_actions

# st.set_page_config("Customer Churn Predictor")

# st.title("📉 Customer Churn Prediction System")

# # --- USER INPUTS ---
# tenure = st.number_input("Tenure (months)", 0, 100, 12)
# monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
# total_charges = st.number_input("Total Charges", 0.0, 10000.0, 800.0)

# contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
# payment_method = st.selectbox(
#     "Payment Method",
#     ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
# )

# user_data = {
#     "tenure": tenure,
#     "MonthlyCharges": monthly_charges,
#     "TotalCharges": total_charges,
#     "Contract": contract,
#     "PaymentMethod": payment_method
# }

# if st.button("Predict Churn Risk"):
#     prob, risk = predict_churn(user_data)
#     drivers = extract_churn_drivers(user_data)
#     explanation, actions = generate_actions(risk, prob, drivers)

#     st.subheader("🔍 Prediction Result")
#     st.write(f"**Churn Probability:** {prob}")

#     if risk == "High":
#         st.error("⚠️ High Risk of Churn")
#     elif risk == "Medium":
#         st.warning("⚠️ Medium Risk of Churn")
#     else:
#         st.success("✅ Low Risk of Churn")

#     st.subheader("📌 Why this customer may churn")
#     st.write(explanation)

#     st.subheader("🛠 Recommended Actions")
#     for a in actions:
#         st.write("•", a)
