from flask import Blueprint, request, jsonify
from ..models import Admin
from ..extensions import db, bcrypt
from itsdangerous import URLSafeTimedSerializer

auth_bp = Blueprint("auth", __name__)
serializer = URLSafeTimedSerializer("secretkey123")


# SIGNUP
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json

    if Admin.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Account already exists"}), 400

    hashed = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    admin = Admin(
        full_name=data["full_name"],
        email=data["email"],
        password=hashed
    )

    db.session.add(admin)
    db.session.commit()

    return jsonify({"message": "Signup successful"})


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    admin = Admin.query.filter_by(email=data["email"]).first()

    if not admin or not bcrypt.check_password_hash(admin.password, data["password"]):
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({"admin_id": admin.id})


# FORGOT PASSWORD
@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.json
    admin = Admin.query.filter_by(email=data["email"]).first()

    if admin:
        token = serializer.dumps(admin.email)
        print(f"Reset Link: http://127.0.0.1:5000/reset/{token}")

    return jsonify({"message": "If email exists, reset link sent"})


# RESET PASSWORD
@auth_bp.route("/reset/<token>", methods=["POST"])
def reset_password(token):
    try:
        email = serializer.loads(token, max_age=3600)
    except:
        return jsonify({"error": "Link expired"}), 400

    data = request.json
    admin = Admin.query.filter_by(email=email).first()

    admin.password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    db.session.commit()

    return jsonify({"message": "Password updated"})