import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase using your service account key
cred = credentials.Certificate("retrieve.json")  # Replace with your JSON key file
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

def fetch_all_products():
    products_ref = db.collection("products")  # Reference to 'products' collection
    docs = products_ref.stream()  # Retrieve all documents

    all_products = []
    for doc in docs:
        product_data = doc.to_dict()  # Convert document to dictionary
        product_data["id"] = doc.id  # Include document ID
        all_products.append(product_data)

    return all_products

# Fetch and print all products
# products = fetch_all_products()
# for product in products:
#     print(product)
