from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import pickle

# 🔥 Firebase Setup
cred = credentials.Certificate("retrieve.json")  # Use your Firebase key
firebase_admin.initialize_app(cred)
db = firestore.client()

# 🔍 Load ML Model & Scaler
with open("xgb_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# 🔥 Flask App Initialization
app = Flask(__name__)

# Function to fetch all products
def fetch_all_products():
    products_ref = db.collection("products")
    docs = products_ref.stream()

    all_products = []
    for doc in docs:
        product_data = doc.to_dict()
        product_data["id"] = doc.id
        all_products.append(product_data)

    return all_products

# Home Route
@app.route("/")
def home():
    all_products = fetch_all_products()

    for i in range(min(9, len(all_products))):
        new_sample = {
            "Base Price": all_products[i]["BasePrice"],
            "Competitor Price": all_products[i]["CompetitorPrice"],
            "Demand": all_products[i]["Demand"],
            "Supply": all_products[i]["Supply"],
            "Expiry Days": all_products[i]["Expiry"]
        }

        # Convert to DataFrame and scale numerical values
        new_df = pd.DataFrame([new_sample])
        new_df[["Base Price", "Competitor Price", "Expiry Days"]] = scaler.transform(
            new_df[["Base Price", "Competitor Price", "Expiry Days"]]
        )

        # Predict optimized price using ML model
        predicted_price = int(loaded_model.predict(new_df)[0])

        # Update Firestore with optimized price
        product_id = all_products[i]["id"]
        db.collection("products").document(product_id).update({
            "OptimizedPrice": predicted_price
        })

    return render_template('index.html')

# 🔍 Search Route
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    # Fetch matching products
    products_ref = db.collection("products")
    docs = products_ref.stream()

    matching_products = []
    for doc in docs:
        product = doc.to_dict()
        if query.lower() in product.get("ProductName", "").lower():
            product["id"] = doc.id
            matching_products.append(product)

    return jsonify(matching_products)

# Route for different pages
@app.route('/product.html')
def product():
    return render_template('product.html')

@app.route('/cart.html')
def cart():
    return render_template('cart.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/search.html')
def search_page():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app
