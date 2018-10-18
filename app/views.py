from app import app
from flask import request
from .models.product import Product
from app.validation import Validation

@app.route("/api/v1/products",methods=["POST"])
"""Add the product route"""
def add_product():
    add_product = Product(request.get_json())
    new_product = add_product.add_product()
    return new_product

@app.route("/api/v1/products", methods=["GET"])
"""This route for fetching all products"""
def fetch_all_products():
    all_products = Product.fetch_all_products()
    return all_products 

@app.route("/api/v1/products/<product_id>", methods=["GET"])
"""route for a single product"""
def fetch_single_product(product_id):
    valid = validation.validate_input_type(product_id)
    if valid:
        return jsonify({"message":valid}), 400
    product = Product(product_id)
    single_product = product.fetch_single_product()
    return single_product



