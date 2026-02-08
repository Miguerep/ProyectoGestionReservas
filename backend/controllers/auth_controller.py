from flask import request, jsonify
from flask_jwt_extended import jwt_required
from src.backend.controllers import api
from src.backend.services.auth_service import AuthService


@api.route("/register/cliente", methods=["POST"])
def register_cliente():
    try:
        user = AuthService.registrar_usuario("cliente", request.get_json())
        return jsonify({"msg": "Cliente registrado", "id": user.id}), 201
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400


@api.route("/register/gerente", methods=["POST"])
def register_gerente():
    try:
        user = AuthService.registrar_usuario("gerente", request.get_json())
        return jsonify({"msg": "Gerente registrado", "id": user.id}), 201
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400


@api.route("/register/estilista", methods=["POST"])
def register_estilista():
    try:
        user = AuthService.registrar_usuario("estilista", request.get_json())
        return jsonify({"msg": "Estilista registrado", "id": user.id}), 201
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400


@api.route("/login", methods=["POST"])
def login():
    try:
        resultado = AuthService.login(request.get_json())
        return jsonify({"msg": "Login exitoso", **resultado}), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 401


@api.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """Endpoint para refrescar el access token usando el refresh token"""
    try:
        resultado = AuthService.refresh_access_token()
        return jsonify({"msg": "Token refrescado exitosamente", **resultado}), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 401
    except Exception as e:
        return jsonify({"msg": "Error al refrescar el token"}), 500


@api.route("/verify", methods=["GET"])
@jwt_required()
def verify_token():
    """Endpoint para verificar si el token es válido y obtener info del usuario"""
    try:
        resultado = AuthService.verificar_token()
        return jsonify({"msg": "Token válido", **resultado}), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 404
    except Exception as e:
        return jsonify({"msg": "Error al verificar el token"}), 500
