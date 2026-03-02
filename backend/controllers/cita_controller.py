from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from src.backend.controllers import api
from src.backend.services.cita_service import CitaService
from src.common import Cita, Estilista, Peluqueria

@api.route("/register/citas", methods=["POST"])
@jwt_required()
def solicitar_cita():
    claims = get_jwt()
    if claims.get("rol") != "cliente":
        return jsonify({"msg": "Acceso denegado"}), 403

    try:
        user_id = int(get_jwt_identity())
        # Delegamos toda la complejidad al servicio
        cita = CitaService.crear_cita(user_id, request.get_json())
        return jsonify({"msg": "Cita creada", "id": cita.id}), 201
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor", "error": str(e)}), 500


@api.route("/peluquerias/<int:id_peluqueria>/citas", methods=["GET"])
@jwt_required()
def obtener_citas_peluqueria(id_peluqueria):
    # El controlador solo pide datos y los entrega. No sabe de SQL.
    datos = CitaService.obtener_por_peluqueria(id_peluqueria)
    return jsonify(datos), 200


@api.route("/citas/<int:id_cita>/estado", methods=["PATCH"])
@jwt_required()
def actualizar_estado_cita(id_cita):
    """
    Actualiza el estado de una cita.

    Flujo: Pendiente → Confirmada → Completada

    Solo gerentes y estilistas pueden actualizar el estado.
    """
    claims = get_jwt()
    rol = claims.get("rol")

    # Solo gerentes y estilistas pueden actualizar el estado
    if rol not in ["gerente", "estilista"]:
        return jsonify({"msg": "Acceso denegado. Solo gerentes y estilistas pueden actualizar el estado"}), 403

    try:
        data = request.get_json()
        nuevo_estado = data.get("estado")

        if not nuevo_estado:
            return jsonify({"msg": "El campo 'estado' es obligatorio"}), 400

        # Delegamos la validación y actualización al servicio
        cita = CitaService.actualizar_estado(id_cita, nuevo_estado)

        return jsonify({
            "msg": "Estado actualizado exitosamente",
            "cita": {
                "id": cita.id,
                "estado": cita.estado,
                "fecha": cita.fecha.strftime("%Y-%m-%d %H:%M")
            }
        }), 200

    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor", "error": str(e)}), 500


@api.route("/citas/<int:id_cita>/cancel", methods=["PUT"])
@jwt_required()
def cancelar_cita(id_cita):
    """
    Cancela una cita existente.

    Permisos:
    - Clientes: solo pueden cancelar sus propias citas
    - Gerentes y estilistas: pueden cancelar cualquier cita
    """
    claims = get_jwt()
    rol = claims.get("rol")
    user_id = int(get_jwt_identity())

    try:
        # Si es cliente, verificar que sea su cita
        cita = Cita.query.get(id_cita)
        
        if rol == "cliente":
            if cita.cliente_id != user_id:
                return jsonify({"msg": "No tienes permiso para cancelar esta cita"}), 403
            
        elif rol in ["gerente", "estilista"]:
            if cita.peluqueria_id != claims.get("peluqueria_id"):
                return jsonify({"msg": "No tienes permiso para cancelar esta cita"}), 403

        elif not cita:
            return jsonify({"msg": "La cita no existe"}), 404
        
        # Cancelar la cita usando el servicio
        cita = CitaService.actualizar_estado(id_cita, "Cancelada")

        return jsonify({
            "msg": "Cita cancelada exitosamente",
            "cita": {
                "id": cita.id,
                "estado": cita.estado,
                "fecha": cita.fecha.strftime("%Y-%m-%d %H:%M")
            }
        }), 200

    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Error interno del servidor", "error": str(e)}), 500
