from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

# Importamos los servicios (Patrón Service Layer)
from src.backend.services.auth_service import AuthService
from src.backend.services.cita_service import CitaService
from src.backend.services.peluqueria_service import PeluqueriaService

api = Blueprint("api", __name__)

# --- RUTAS DE AUTENTICACIÓN ---

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

# --- RUTAS DE GESTIÓN (Peluquerías) ---

@api.route("/register/peluquerias", methods=["POST"])
@jwt_required()
def crear_peluqueria():
    claims = get_jwt()
    if claims.get("rol") != "gerente":
        return jsonify({"msg": "Acceso denegado"}), 403
        
    try:
        pelu = PeluqueriaService.crear_peluqueria(request.get_json())
        return jsonify({"msg": "Peluquería creada", "id": pelu.id}), 201
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400

# --- RUTAS DE CITAS ---

@api.route("/register/citas", methods=["POST"])
@jwt_required()
def solicitar_cita():
    claims = get_jwt()
    if claims.get("rol") != "cliente":
        return jsonify({"msg": "Acceso denegado"}), 403
    
    try:
        user_id = int(get_jwt_identity())
        cita = CitaService.crear_cita(user_id, request.get_json())
        return jsonify({"msg": "Cita creada", "id": cita.id}), 201
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400

@api.route("/peluquerias/<int:id_peluqueria>/citas", methods=["GET"])
@jwt_required()
def obtener_citas_peluqueria(id_peluqueria):
    # Ya no hay lógica SQL aquí, solo llamada al servicio
    datos = CitaService.obtener_por_peluqueria(id_peluqueria)
    return jsonify(datos), 200