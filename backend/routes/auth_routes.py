from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth_bp", __name__)

users = []

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    users.append(data)
    return jsonify({"message": "User registered"})


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    return jsonify({"message": "Login successful"})