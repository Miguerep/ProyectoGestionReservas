from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from src.backend.controllers import api
from src.backend.services.servicio_service import ServicioService


@api.route("/servicios", methods=["POST"])
@jwt_required()
def crear_servicio():
    """Crea un nuevo servicio (solo gerente)"""
    claims = get_jwt()
    if claims.get("rol") != "gerente":
        return jsonify({"msg": "Acceso denegado. Solo gerentes pueden crear servicios"}), 403

    try:
        servicio = ServicioService.crear_servicio(request.get_json())
        return jsonify({
            "msg": "Servicio creado exitosamente",
            "servicio": {
                "id": servicio.id,
                "nombre": servicio.nombre,
                "precio": servicio.precio,
                "duracion": servicio.duracion
            }
        }), 201
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor"}), 500


@api.route("/servicios", methods=["GET"])
def obtener_servicios():
    """Obtiene todos los servicios (público)"""
    try:
        servicios = ServicioService.obtener_todos()
        return jsonify({
            "servicios": [
                {
                    "id": s.id,
                    "nombre": s.nombre,
                    "precio": s.precio,
                    "duracion": s.duracion
                }
                for s in servicios
            ]
        }), 200
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor"}), 500


@api.route("/servicios/<int:id_servicio>", methods=["GET"])
def obtener_servicio(id_servicio):
    """Obtiene un servicio por ID (público)"""
    try:
        servicio = ServicioService.obtener_por_id(id_servicio)
        return jsonify({
            "servicio": {
                "id": servicio.id,
                "nombre": servicio.nombre,
                "precio": servicio.precio,
                "duracion": servicio.duracion
            }
        }), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 404
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor"}), 500


@api.route("/servicios/<int:id_servicio>", methods=["PUT", "PATCH"])
@jwt_required()
def actualizar_servicio(id_servicio):
    """Actualiza un servicio existente (solo gerente)"""
    claims = get_jwt()
    if claims.get("rol") != "gerente":
        return jsonify({"msg": "Acceso denegado. Solo gerentes pueden actualizar servicios"}), 403

    try:
        servicio = ServicioService.actualizar_servicio(id_servicio, request.get_json())
        return jsonify({
            "msg": "Servicio actualizado exitosamente",
            "servicio": {
                "id": servicio.id,
                "nombre": servicio.nombre,
                "precio": servicio.precio,
                "duracion": servicio.duracion
            }
        }), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor"}), 500


@api.route("/servicios/<int:id_servicio>", methods=["DELETE"])
@jwt_required()
def eliminar_servicio(id_servicio):
    """Elimina un servicio (solo gerente)"""
    claims = get_jwt()
    if claims.get("rol") != "gerente":
        return jsonify({"msg": "Acceso denegado. Solo gerentes pueden eliminar servicios"}), 403

    try:
        ServicioService.eliminar_servicio(id_servicio)
        return jsonify({"msg": "Servicio eliminado exitosamente"}), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor"}), 500