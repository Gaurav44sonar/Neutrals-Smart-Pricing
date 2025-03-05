from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Initialize Flask app

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/product.html')
def product():
    return render_template('product.html')

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app

# import pandas as pd
# import pickle

# with open("xgb_model.pkl", "rb") as f:
#     loaded_model = pickle.load(f)

# # Load the fitted StandardScaler
# with open("scaler.pkl", "rb") as f:
#     scaler = pickle.load(f)


# new_sample = {
#     "Base Price": [27],
#     "Competitor Price": [30],
#     "Demand": [1],      # Categorical input
#     "Supply": [2],    # Categorical input
#     "Expiry Days": [8]
# }
# new_df = pd.DataFrame(new_sample)

# new_df[["Base Price", "Competitor Price", "Expiry Days"]] = scaler.transform(
#     new_df[["Base Price", "Competitor Price", "Expiry Days"]]
# )

# # Predict using your trained XGBoost model (xgb_model)
# predicted_price = loaded_model.predict(new_df)[0]
# print(f"Predicted Optimized Price: {predicted_price:.2f}")