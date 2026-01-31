from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt,  get_jwt_identity
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from src.common import db, Cliente, Servicio, Cita, Peluqueria, Estilista, CitaServicio, PeluqueriaServicio, Gerente

api = Blueprint("api", __name__)

# ... [MANTEN LOS ENDPOINTS DE REGISTER Y LOGIN IGUAL QUE ANTES] ...
# (Solo pongo aquí la función que daba error corregida para no hacer spam de código, 
#  pero asegúrate de mantener el resto del archivo)

@api.route("/register/cliente", methods=["POST"])
def register_cliente():
    # ... (Tu código de registro de cliente) ...
    data = request.get_json()
    if not data or not data.get("nombre") or not data.get("email") or not data.get("password"):
        return jsonify({"msg": "Faltan datos obligatorios."}), 400
    try:
        email_valido = validate_email(data.get("email"))
        email_limpio = email_valido.normalized
        if Cliente.query.filter_by(_email = email_limpio).first():
            return jsonify({"msg":"El usuario ya existe"})
        nuevo_cliente = Cliente()
        nuevo_cliente.set_nombre(data.get("nombre"))
        nuevo_cliente.set_email(email_limpio)
        nuevo_cliente.set_password_hash(generate_password_hash(data.get("password")))
        if data.get("apellidos"): nuevo_cliente.set_apellidos(data.get("apellidos"))
        if data.get("telefono"): nuevo_cliente.set_telefono(data.get("telefono"))
        db.session.add(nuevo_cliente)
        db.session.commit()
        return jsonify({"msg": "Usuario registrado correctamente", "id": nuevo_cliente.get_id()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Error: {str(e)}"}), 500

@api.route("/register/gerente", methods=["POST"])
def register_gerente():
    # ... (Tu código de registro de gerente) ...
    data = request.get_json()
    try:
        email_valido = validate_email(data.get("email"))
        email_limpio = email_valido.normalized
        if Gerente.query.filter_by(_email = email_limpio).first(): return ({"msg": "El usuario ya existe."})
        nuevo_gerente = Gerente()
        nuevo_gerente.set_nombre(data.get("nombre"))
        nuevo_gerente.set_email(email_limpio)
        nuevo_gerente.set_password_hash(generate_password_hash(data.get("password")))
        if data.get("apellidos"): nuevo_gerente.set_apellidos(data.get("apellidos"))
        if data.get("telefono"): nuevo_gerente.set_telefono(data.get("telefono"))
        db.session.add(nuevo_gerente)
        db.session.commit()
        return jsonify({"msg": "Gerente registrado", "id": nuevo_gerente.get_id()}), 201
    except Exception as e: return jsonify({"msg": str(e)}), 400

@api.route("/register/estilista", methods=["POST"])
def register_estilista():
    # ... (Tu código de registro de estilista) ...
    data = request.get_json()
    try:
        email_valido = validate_email(data.get("email"))
        email_limpio = email_valido.normalized
        if Estilista.query.filter_by(_email = email_limpio).first(): return ({"msg": "El usuario ya existe."})
        nuevo_estilista = Estilista()
        nuevo_estilista.set_peluqueria(data.get("id_peluqueria"))
        nuevo_estilista.set_nombre(data.get("nombre"))
        nuevo_estilista.set_email(email_limpio)
        nuevo_estilista.set_password_hash(generate_password_hash(data.get("password")))
        nuevo_estilista.set_activo(True)
        db.session.add(nuevo_estilista)
        db.session.commit()
        return jsonify({"msg": "Estilista registrado", "id": nuevo_estilista.get_id()}), 201
    except Exception as e: return jsonify({"msg": str(e)}), 400

@api.route("/login", methods = ["POST"])
def login():
    # ... (Tu código de login) ...
    data = request.get_json()
    try:
        email_valido = validate_email(data.get("email"))
        email = email_valido.normalized     
        password = data.get("password")
        rol = data.get("rol").lower().strip()
        user = None
        if rol == "cliente": user = Cliente.query.filter_by(_email = email).first()
        elif rol == "gerente": user = Gerente.query.filter_by(_email = email).first()
        else: return jsonify({"msg": "Rol invalido"}), 400
        
        if user and check_password_hash(user.get_password_hash(), password):
            access_token = create_access_token(identity=str(user.get_id()), additional_claims={"rol": rol})
            return jsonify({"msg": "Login exitoso", "access_token": access_token, "user": {"id": user.get_id(), "nombre": user.get_nombre(), "rol": rol}}), 200
        return jsonify({"msg": "Credenciales incorrectas"}), 401
    except Exception as e: return jsonify({"msg": str(e)}), 400

@api.route("/register/citas", methods=["POST"])
@jwt_required()
def solicitar_cita():
    # ... (Tu código de solicitar cita) ...
    claims = get_jwt()
    if claims.get("rol") != "cliente": return jsonify({"msg": "Acceso Denegado"}), 403
    data = request.get_json()
    try:
        servicio = Servicio.query.get(data.get("id_servicio"))
        if not servicio: return jsonify({"msg": "Servicio no existe"}), 404
        
        nueva_cita = Cita()
        nueva_cita.set_cliente(int(get_jwt_identity()))
        nueva_cita.set_peluqueria(data.get("id_peluqueria"))
        nueva_cita.set_servicio(data.get("id_servicio"))
        nueva_cita.set_fecha(datetime.strptime(data.get("fecha"), "%Y-%m-%d %H:%M"))
        nueva_cita.set_estado("Solicitada")
        db.session.add(nueva_cita)
        db.session.flush()
        
        # GUARDAMOS EL PRECIO EN LA TABLA INTERMEDIA
        nuevo_detalle = CitaServicio()
        nuevo_detalle.set_cita(nueva_cita.get_id())
        nuevo_detalle.set_servicio(data.get("id_servicio"))
        nuevo_detalle.set_precioAplicado(servicio.get_precio())
        db.session.add(nuevo_detalle)
        db.session.commit()
        return jsonify({"msg": "Cita creada"}), 201
    except Exception as e: 
        db.session.rollback()
        return jsonify({"msg": str(e)}), 400

@api.route("/register/peluquerias", methods=["POST"])
@jwt_required()
def crear_peluqueria():
    # ... (Tu código de crear peluquería) ...
    claims = get_jwt()
    if claims.get("rol") != "gerente": return jsonify({"msg": "Acceso denegado"}), 403
    data = request.get_json()
    try:
        nueva_peluqueria = Peluqueria()
        nueva_peluqueria.set_nombre(data.get("nombre"))
        nueva_peluqueria.set_direccion(data.get("direccion"))
        nueva_peluqueria.set_telefono(data.get("telefono"))
        db.session.add(nueva_peluqueria)
        db.session.commit()
        return jsonify({"msg": "Peluquería creada"}), 201
    except Exception as e: return jsonify({"msg": str(e)}), 500

# 👇 AQUÍ ESTÁ LA CORRECCIÓN IMPORTANTE 👇
@api.route("/peluquerias/<int:id_peluqueria>/citas", methods=["GET"])
@jwt_required()
def obtener_citas_peluqueria(id_peluqueria):
    try:
        # 1. Unimos Cita con Cliente y Servicio (Tablas maestras)
        # 2. Unimos con CitaServicio (Tabla Intermedia) para obtener el precio real
        citas = db.session.query(Cita, Cliente, Servicio, CitaServicio)\
            .join(Cliente, Cita._id_cliente == Cliente._id_cliente)\
            .join(Servicio, Cita._id_servicio == Servicio._id_servicio)\
            .join(CitaServicio, Cita._id_cita == CitaServicio._id_cita)\
            .filter(Cita._id_peluqueria == id_peluqueria)\
            .all()

        resultado = []
        for cita, cliente, servicio, cita_servicio in citas:
            resultado.append({
                "id": cita.get_id(),
                "fecha": cita.get_fecha().strftime("%Y-%m-%d %H:%M"),
                "cliente": cliente.get_nombre(),
                "servicio": servicio.get_nombre(),
                "estilista": "Por asignar", # Ponemos un placeholder porque Cita no tiene el campo estilista aun
                "estado": cita.get_estado(),
                "precio_congelado": cita_servicio._precioAplicado # ¡DATO DESDE LA TABLA INTERMEDIA!
            })

        return jsonify(resultado), 200
    except Exception as e:
        print(f"DEBUG ERROR: {str(e)}")
        return jsonify({"msg": f"Error al obtener citas: {str(e)}"}), 500