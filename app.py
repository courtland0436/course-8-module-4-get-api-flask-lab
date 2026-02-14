from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Homepage route
@app.route("/", methods=["GET"])
def home():
    # Returns a welcome message
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200

# GET /products route
@app.route("/products", methods=["GET"])
def get_products():
    # Get optional 'category' query parameter
    category = request.args.get("category")

    if category:
        # Filter products by category (case-insensitive)
        filtered_products = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered_products), 200

    # Return all products if no category filter
    return jsonify(products), 200

# GET /products/<id> route
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    # Find the product with the given ID
    product = next((p for p in products if p["id"] == id), None)

    if product:
        return jsonify(product), 200

    # Return 404 if not found
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
