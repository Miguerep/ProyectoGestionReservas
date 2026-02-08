from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, get_jwt
from email_validator import validate_email, EmailNotValidError
from src.common import db, Cliente, Gerente, Estilista

class AuthService:
    
    @staticmethod
    def _validar_email(email):
        try:
            valid = validate_email(email)
            return valid.normalized
        except EmailNotValidError as e:
            raise ValueError(f"Email inválido: {str(e)}")

    @staticmethod
    def registrar_usuario(tipo, data):
        email = AuthService._validar_email(data.get("email"))
        password = data.get("password")
        nombre = data.get("nombre")
        
        if not all([email, password, nombre]):
            raise ValueError("Faltan datos obligatorios")

        # Factory logic simple para crear usuarios
        if tipo == "cliente":
            if Cliente.query.filter_by(email=email).first():
                raise ValueError("El usuario ya existe")
            nuevo_user = Cliente(nombre=nombre, email=email, password_hash=generate_password_hash(password))
            
        elif tipo == "gerente":
            if Gerente.query.filter_by(email=email).first():
                raise ValueError("El usuario ya existe")
            nuevo_user = Gerente(nombre=nombre, email=email, password_hash=generate_password_hash(password))
            
        elif tipo == "estilista":
            if Estilista.query.filter_by(email=email).first():
                raise ValueError("El usuario ya existe")
            id_peluqueria = data.get("id_peluqueria")
            if not id_peluqueria:
                raise ValueError("Se requiere id_peluqueria para un estilista")
            
            nuevo_user = Estilista(
                nombre=nombre, email=email, 
                password_hash=generate_password_hash(password),
                id_peluqueria=id_peluqueria,
                activo=True
            )
        else:
            raise ValueError("Tipo de usuario no válido")

        if data.get("apellidos"): nuevo_user.apellidos = data.get("apellidos")
        if data.get("telefono"): nuevo_user.telefono = data.get("telefono")

        db.session.add(nuevo_user)
        db.session.commit()
        return nuevo_user

    @staticmethod
    def login(data):
        email = AuthService._validar_email(data.get("email"))
        password = data.get("password")
        rol = data.get("rol", "").lower().strip()
        
        user = None
        if rol == "cliente":
            user = Cliente.query.filter_by(email=email).first()
        elif rol == "gerente":
            user = Gerente.query.filter_by(email=email).first()
        else:
            raise ValueError("Rol inválido o no especificado")
            
        if user and check_password_hash(user.password_hash, password):
            # Crear claims adicionales para ambos tokens
            additional_claims = {"rol": rol, "email": user.email}

            access_token = create_access_token(
                identity=str(user.id),
                additional_claims=additional_claims
            )

            refresh_token = create_refresh_token(
                identity=str(user.id),
                additional_claims=additional_claims
            )

            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": {"id": user.id, "nombre": user.nombre, "email": user.email, "rol": rol}
            }
        else:
            raise ValueError("Credenciales incorrectas")

    @staticmethod
    def refresh_access_token():
        """Genera un nuevo access token usando el refresh token"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        rol = claims.get("rol")
        email = claims.get("email")

        if not rol or not email:
            raise ValueError("Token de refresco inválido")

        # Crear nuevo access token con los mismos claims
        new_access_token = create_access_token(
            identity=current_user_id,
            additional_claims={"rol": rol, "email": email}
        )

        return {
            "access_token": new_access_token
        }

    @staticmethod
    def verificar_token():
        """Verifica si el token actual es válido y retorna info del usuario"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        rol = claims.get("rol")
        email = claims.get("email")

        # Buscar el usuario según el rol
        user = None
        if rol == "cliente":
            user = Cliente.query.get(current_user_id)
        elif rol == "gerente":
            user = Gerente.query.get(current_user_id)
        elif rol == "estilista":
            user = Estilista.query.get(current_user_id)

        if not user:
            raise ValueError("Usuario no encontrado")

        return {
            "user": {
                "id": user.id,
                "nombre": user.nombre,
                "email": user.email,
                "rol": rol
            }
        }