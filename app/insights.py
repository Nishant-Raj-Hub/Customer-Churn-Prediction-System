import joblib

lr_coeff = joblib.load("../model/lr_coeff.pkl")

def extract_churn_drivers(user_input: dict, top_n=3):
    drivers = []

    for feature, coef in lr_coeff.items():
        # match encoded feature names
        for key, value in user_input.items():
            if key in feature and value in [1, "Yes"] and coef > 0:
                drivers.append((feature, coef))

    drivers.sort(key=lambda x: x[1], reverse=True)

    return [d[0].replace("cat_", "").replace("num_", "") for d in drivers[:top_n]]
