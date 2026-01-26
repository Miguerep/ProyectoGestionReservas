from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt,  get_jwt_identity
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from src.common import db, Cliente, Servicio, Cita, Peluqueria, Estilista, CitaServicio, PeluqueriaServicio, Gerente

api = Blueprint("api", __name__)

@api.route("/register/cliente", methods=["POST"])
def register_cliente():
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
        
        if data.get("apellidos"):
            nuevo_cliente.set_apellidos(data.get("apellidos"))
        
        if data.get("telefono"):
            nuevo_cliente.set_telefono(data.get("telefono"))
            
        db.session.add(nuevo_cliente)
        db.session.commit()
        
        return jsonify({"msg": "Usuario registrado correctamente", 
                        "id": nuevo_cliente.get_id()
                        }), 201
    except ValueError as e:
        return jsonify({"msg": f"Error de validación: {str(e)}"}), 400
    
    except EmailNotValidError as e:
        return jsonify({"msg": f"Email inválido: {str(e)}"}), 400
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Error interno: {str(e)}"}), 500
    
@api.route("/register/gerente", methods=["POST"])
def register_gerente():
    data = request.get_json()
    
    if not data or not data.get("nombre") or not data.get("email") or not data.get("password"):
        return jsonify({"msg": "Faltan datos obligatorios"}), 400

    try:
        email_valido = validate_email(data.get("email"))
        email_limpio = email_valido.normalized
        if Gerente.query.filter_by(_email = email_limpio).first():
            return ({"msg": "El usuario ya existe."})
        
        nuevo_gerente = Gerente()
        nuevo_gerente.set_nombre(data.get("nombre"))
        nuevo_gerente.set_email(data.get("email"))
        nuevo_gerente.set_password_hash(generate_password_hash(data.get("password")))
        if data.get("apellidos"):
            nuevo_gerente.set_apellidos(data.get("apellidos"))
        
        if data.get("telefono"):
            nuevo_gerente.set_telefono(data.get("telefono"))
            
        db.session.add(nuevo_gerente)
        db.session.commit()
        
        return jsonify({"msg": "El usuario se registro correctamente.",
                        "id": nuevo_gerente.get_id()
                        }), 201
        
    except ValueError as e:
        return jsonify({"msg":f"Error de validación: {str(e)}"}), 400
    
    except EmailNotValidError as e:
        return jsonify({"msg": f"Email invalido: {str(e)}"}), 400
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Email invalido: {str(e)}"}), 400

@api.route("/register/estilista", methods=["POST"])
def register_estilista():
    data = request.get_json()
    
    if not data or not data.get("nombre") or not data.get("email") or not data.get("password") or not data.get("id_peluqueria"):
        return jsonify({"msg": "Faltan datos obligatorios"}), 400

    id_peluqueria = data.get("id_peluqueria")
    peluqueria = Peluqueria.query.get(id_peluqueria)
    if not peluqueria:
        return jsonify({"msg": "No existe es pelqueria."})
    
    try:
        print(f"datos: {data}")
        email_valido = validate_email(data.get("email"))
        email_limpio = email_valido.normalized
        
        if Estilista.query.filter_by(_email = email_limpio).first():
            return ({"msg": "El usuario ya existe."})
        
        nuevo_estilista = Estilista()
        
        nuevo_estilista.set_peluqueria(data.get("id_peluqueria"))
        nuevo_estilista.set_nombre(data.get("nombre"))
        nuevo_estilista.set_email(data.get("email"))
        nuevo_estilista.set_password_hash(generate_password_hash(data.get("password")))
        nuevo_estilista.set_activo(True)
        
        
        if data.get("apellidos"):
            nuevo_estilista.set_apellidos(data.get("apellidos"))
        if data.get("telefono"):
            nuevo_estilista.set_telefono(data.get("telefono"))

        db.session.add(nuevo_estilista)
        db.session.commit()
        
        return jsonify({
                    "msg": "Estilista registrado con éxito",
                    "id": nuevo_estilista.get_id(),
                    "id_peluqueria": id_peluqueria,
                    "estado": nuevo_estilista.get_activo()
                }), 201
    
    except ValueError as e:
        return jsonify({"msg":f"Error de validación: {str(e)}"}), 400
    
    except EmailNotValidError as e:
        return jsonify({"msg": f"Email invalido: {str(e)}"}), 400
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Error: {str(e)}"}), 400
    
@api.route("/login", methods = ["POST"])
def login():
    data = request.get_json()
    
    if not data or not data.get("rol") or not data.get("email") or not data.get("password"):
        return jsonify({"msg": "Faltan datos obligatorios."}), 400
    
    
    try:
            email_valido = validate_email(data.get("email"))
            email = email_valido.normalized     
            password = data.get("password")
            rol = data.get("rol").lower().strip()
            
            user = None
            
            if rol == "cliente":
                user = Cliente.query.filter_by(_email = email).first()

            elif rol == "gerente":
                user = Gerente.query.filter_by(_email = email).first()
            
            else:
                return jsonify({"msg": "Error: rol invalido."}), 400
            
            if user and check_password_hash(user.get_password_hash(), password):
                
                access_token = create_access_token(
                identity=str(user.get_id()),          
                additional_claims={"rol": rol}   
            )
                return jsonify({"msg": "Login exitoso",
                    "access_token": access_token,
                    "user": {
                        "id": user.get_id(),
                        "nombre": user.get_nombre(),
                        "email": user.get_email(),
                        "rol": rol
                    }
                    }), 200
            
            return jsonify({"msg": "Error: El email o la contraseña son incorrectos"}), 401
        
    
    except ValueError as e:
        return jsonify({"msg":f"Error de validación: {str(e)}"}), 400
    
    except EmailNotValidError as e:
        return jsonify({"msg": f"Email invalido: {str(e)}"}), 400
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Error: {str(e)}"}), 400
    
@api.route("/register/citas", methods=["POST"])
@jwt_required()
def solicitar_cita():
    
    
    claims = get_jwt()
    if claims.get("rol") != "cliente":
        return jsonify({"msg": "Acceso Denegado: Solo clientes pueden reservar citas."}), 403
    
    current_user_id = get_jwt_identity()
    data = request.get_json()
    print("\n--- DEBUG CITA ---")
    print(f"Datos recibidos: {data}")
    
    if not data or not data.get("id_peluqueria") or not data.get("id_servicio") or not data.get("fecha"):
        return jsonify({"msg": "Error, faltan datos obligatorios."}), 400    
    
    try:
        #Sacamos la peluqueria y el servicio para validar que existe
        peluqueria = Peluqueria.query.get(data.get("id_peluqueria"))
        servicio = Servicio.query.get(data.get("id_servicio"))
        
        if not servicio:
            return jsonify({"msg": "El servicio no existe"}), 404
        
        elif not peluqueria:
            return jsonify({"msg": "La peluqueria no existe"}), 404

        precio_actual = servicio.get_precio()
        
        
        #Crear cita si tenemos los datos
        nueva_cita = Cita()
        nueva_cita.set_cliente(int(current_user_id))
        nueva_cita.set_peluqueria(data.get("id_peluqueria"))
        nueva_cita.set_servicio(data.get("id_servicio"))
        fecha_str = data.get("fecha")
        nueva_cita.set_fecha(datetime.strptime(fecha_str, "%Y-%m-%d %H:%M"))
        
        nueva_cita.set_estado("Solicitada")
        
        db.session.add(nueva_cita)
        
        #a partir de la cita creamos su relacion con el servicio
        db.session.flush()
        id_cita_generado = nueva_cita.get_id()

      
        nuevo_detalle = CitaServicio()
        nuevo_detalle.set_cita(id_cita_generado)
        nuevo_detalle.set_servicio(data.get("id_servicio"))
        nuevo_detalle.set_precioAplicado(precio_actual)

        db.session.add(nuevo_detalle)
        db.session.commit()
        
        return jsonify({
            "msg": "Cita solicitada con éxito",
            "id": nueva_cita.get_id(),
            "fecha": str(nueva_cita.get_fecha()), 
            "estado": "Solicitada",
            "precio_congelado": precio_actual
        }), 201

        
    except ValueError as e:
        return jsonify({"msg":f"Error de validación: {str(e)}"}), 400
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Error: {str(e)}"}), 400@api.route("/peluquerias", methods=["POST"])
    
@api.route("/register/peluquerias", methods=["POST"])
@jwt_required()
def crear_peluqueria():
    # 1. Seguridad: Verificar que es un Gerente
    claims = get_jwt()
    if claims.get("rol") != "gerente":
        return jsonify({"msg": "Acceso denegado: Solo los gerentes pueden crear peluquerías."}), 403

    data = request.get_json()
    
    # 2. Validar datos obligatorios
    if not data or not data.get("nombre") or not data.get("direccion") or not data.get("telefono"):
        return jsonify({"msg": "Faltan datos obligatorios (nombre, direccion, telefono)."}), 400
    
    try:
        # 3. Validar duplicidad 
        telefono = data.get("telefono")
        if Peluqueria.query.filter_by(_telefono=telefono).first():
            return jsonify({"msg": "Ya existe una peluquería con ese teléfono."}), 400
            
        # 4. Crear la Peluquería
        nueva_peluqueria = Peluqueria()
        nueva_peluqueria.set_nombre(data.get("nombre"))
        nueva_peluqueria.set_direccion(data.get("direccion"))
        nueva_peluqueria.set_telefono(telefono)
        
        db.session.add(nueva_peluqueria)
        db.session.commit()
        
        return jsonify({
            "msg": "Peluquería creada con éxito",
            "id": nueva_peluqueria.get_id(),
            "nombre": nueva_peluqueria.get_nombre()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Error interno: {str(e)}"}), 500  