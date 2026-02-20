from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from src.backend.controllers import api
from src.backend.services.estilista_service import EstilistaService


@api.route("/peluquerias/<int:id_peluqueria>/estilistas", methods=["GET"])
@jwt_required()
def obtener_estilistas_peluqueria(id_peluqueria):
    """
    Obtiene todos los estilistas de una peluquería

    Query params:
        incluir_inactivos: true/false (default: false)
    """
    claims = get_jwt()
    rol = claims.get("rol")

    # Solo gerentes pueden ver estilistas
    if rol != "gerente":
        return jsonify({"msg": "Acceso denegado. Solo gerentes pueden gestionar estilistas"}), 403

    incluir_inactivos = request.args.get("incluir_inactivos", "false").lower() == "true"
    estilistas = EstilistaService.obtener_por_peluqueria(id_peluqueria, incluir_inactivos)

    return jsonify(estilistas), 200


@api.route("/peluquerias/<int:id_peluqueria>/estilistas", methods=["POST"])
@jwt_required()
def crear_estilista(id_peluqueria):
    """
    Crea un nuevo estilista para una peluquería

    Body:
        {
            "nombre": "string (required)",
            "apellidos": "string (optional)",
            "telefono": "string (optional)",
            "email": "string (required)",
            "password": "string (required)"
        }
    """
    claims = get_jwt()
    rol = claims.get("rol")

    # Solo gerentes pueden crear estilistas
    if rol != "gerente":
        return jsonify({"msg": "Acceso denegado. Solo gerentes pueden crear estilistas"}), 403

    try:
        data = request.get_json()
        estilista = EstilistaService.crear_estilista(id_peluqueria, data)

        return jsonify({
            "msg": "Estilista creado exitosamente",
            "id": estilista.id,
            "nombre": estilista.nombre,
            "email": estilista.email
        }), 201

    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor", "error": str(e)}), 500


@api.route("/estilistas/<int:id_estilista>", methods=["GET"])
@jwt_required()
def obtener_estilista(id_estilista):
    """
    Obtiene un estilista por su ID
    """
    claims = get_jwt()
    rol = claims.get("rol")

    # Solo gerentes pueden ver detalles de estilistas
    if rol != "gerente":
        return jsonify({"msg": "Acceso denegado"}), 403

    estilista = EstilistaService.obtener_por_id(id_estilista)

    if not estilista:
        return jsonify({"msg": "Estilista no encontrado"}), 404

    return jsonify({
        "id": estilista.id,
        "nombre": estilista.nombre,
        "apellidos": estilista.apellidos,
        "telefono": estilista.telefono,
        "email": estilista.email,
        "activo": estilista.activo
    }), 200


@api.route("/estilistas/<int:id_estilista>", methods=["PUT"])
@jwt_required()
def actualizar_estilista(id_estilista):
    """
    Actualiza los datos de un estilista

    Body:
        {
            "nombre": "string (optional)",
            "apellidos": "string (optional)",
            "telefono": "string (optional)",
            "email": "string (optional)",
            "password": "string (optional)",
            "activo": "boolean (optional)"
        }
    """
    claims = get_jwt()
    rol = claims.get("rol")

    # Solo gerentes pueden actualizar estilistas
    if rol != "gerente":
        return jsonify({"msg": "Acceso denegado. Solo gerentes pueden actualizar estilistas"}), 403

    try:
        data = request.get_json()
        estilista = EstilistaService.actualizar_estilista(id_estilista, data)

        return jsonify({
            "msg": "Estilista actualizado exitosamente",
            "id": estilista.id,
            "nombre": estilista.nombre,
            "email": estilista.email,
            "activo": estilista.activo
        }), 200

    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor", "error": str(e)}), 500


@api.route("/estilistas/<int:id_estilista>", methods=["DELETE"])
@jwt_required()
def desactivar_estilista(id_estilista):
    """
    Desactiva un estilista (borrado lógico)
    """
    claims = get_jwt()
    rol = claims.get("rol")

    # Solo gerentes pueden desactivar estilistas
    if rol != "gerente":
        return jsonify({"msg": "Acceso denegado. Solo gerentes pueden desactivar estilistas"}), 403

    try:
        estilista = EstilistaService.desactivar_estilista(id_estilista)

        return jsonify({
            "msg": "Estilista desactivado exitosamente",
            "id": estilista.id,
            "nombre": estilista.nombre
        }), 200

    except ValueError as e:
        return jsonify({"msg": str(e)}), 404
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor", "error": str(e)}), 500
