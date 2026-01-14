from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

api = Blueprint("api", __name__)

@api.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"msg": "Faltan datos obligatorios."}), 400

