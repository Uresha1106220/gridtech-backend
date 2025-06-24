from flask import Blueprint, request, jsonify
from .models import Category, Product, Purchase
from . import db

bp = Blueprint('routes', __name__)

@bp.route("/api/categories")
def get_categories():
    categories = Category.query.all()
    return jsonify([
        {
            "id": c.id,
            "name": c.name,
            "type": c.type,
            "subcategories": c.subcategories
        } for c in categories
    ])

@bp.route("/api/products")
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "price": p.price,
            "category": p.category,
            "subcategory": p.subcategory,
            "image_url": p.image_url,
            "status": p.status
        } for p in products
    ])

@bp.route("/api/purchase/<int:product_id>", methods=["POST"])
def purchase_product(product_id):
    data = request.get_json()
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    purchase = Purchase(product_id=product_id, user_email=email)
    db.session.add(purchase)
    db.session.commit()

    return jsonify({
        "message": "Purchase successful. Status: Booked",
        "purchase_id": purchase.id
    })
