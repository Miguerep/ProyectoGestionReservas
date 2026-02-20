from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from src.backend.controllers import api
from src.backend.services.peluqueria_service import PeluqueriaService


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
