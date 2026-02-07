from flask import request, jsonify
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
