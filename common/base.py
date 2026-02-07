from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy.orm import validates

db = SQLAlchemy();


@dataclass
class Persona(db.Model):
    __abstract__ = True 
    
    # --- COLUMNAS PÚBLICAS (Pythonic Way) ---
    # Eliminamos el guion bajo. SQLAlchemy gestiona el acceso.
    nombre = db.Column(db.String(50), nullable=False, default="")
    apellidos = db.Column(db.String(100), nullable=True, default="")
    telefono = db.Column(db.String(20), nullable=True, default="")
    email = db.Column(db.String(120), unique=True, nullable=False, default="")
    password_hash = db.Column(db.String(255), nullable=False, default="")

    # --- VALIDACIONES AUTOMÁTICAS (SQLAlchemy) ---
    # Este decorador intercepta cualquier asignación (ej: usuario.nombre = "X")
    # y ejecuta la validación antes de guardar el valor.

    @validates('nombre')
    def validate_nombre(self, key, nombre):
        if not nombre or len(nombre.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        return nombre

    @validates('apellidos')
    def validate_apellidos(self, key, apellidos):
        if apellidos and len(apellidos.strip()) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres.")
        return apellidos

    @validates('telefono')
    def validate_telefono(self, key, telefono):
        if telefono:
            telefono_limpio = telefono.strip()
            if len(telefono_limpio) != 9 or not telefono_limpio.isdigit():
                raise ValueError("El teléfono debe tener 9 dígitos numéricos.")
        return telefono

    @validates('email')
    def validate_email(self, key, email):
        if not email or "@" not in email:
            raise ValueError("El email no es válido.")
        return email

    @validates('password_hash')
    def validate_password_hash(self, key, password_hash):
        if not password_hash or len(password_hash) < 10:
            raise ValueError("El hash de la contraseña es inseguro o inválido.")
        return password_hash
    