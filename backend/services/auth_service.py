from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
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
        """Maneja el registro de Cliente, Gerente o Estilista"""
        email = AuthService._validar_email(data.get("email"))
        password = data.get("password")
        nombre = data.get("nombre")
        
        if not all([email, password, nombre]):
            raise ValueError("Faltan datos obligatorios")

        # Selección del modelo según el tipo
        if tipo == "cliente":
            if Cliente.query.filter_by(email=email).first(): # Usando atributo público 'email'
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
                peluqueria_id=id_peluqueria,
                activo=True
            )
        else:
            raise ValueError("Tipo de usuario no válido")

        # Campos opcionales comunes
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
            access_token = create_access_token(
                identity=str(user.id),
                additional_claims={"rol": rol}
            )
            return {
                "access_token": access_token,
                "user": {"id": user.id, "nombre": user.nombre, "email": user.email, "rol": rol}
            }
        else:
            raise ValueError("Credenciales incorrectas")