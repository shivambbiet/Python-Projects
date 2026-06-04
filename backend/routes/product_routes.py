from flask import Blueprint, request, jsonify
from backend.models.product_model import Product, products_db
from backend.services.s3_service import upload_file, generate_presigned_url
import uuid

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/upload", methods=["POST"])
def upload_product():
    file = request.files.get("file")
    name = request.form.get("name")
    description = request.form.get("description")
    price = request.form.get("price")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    filename = f"{uuid.uuid4()}_{file.filename}"

    image_url = upload_file(file, filename)

    product = Product(name, description, price, image_url)
    products_db.append(product)

    return jsonify(product.to_dict())


@product_bp.route("/", methods=["GET"])
def get_products():
    return jsonify([p.to_dict() for p in products_db])


@product_bp.route("/secure/<key>", methods=["GET"])
def get_secure_url(key):
    url = generate_presigned_url(key)
    return jsonify({"url": url})