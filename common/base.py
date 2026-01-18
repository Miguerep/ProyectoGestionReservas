from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy();


@dataclass
class Persona(db.Model):
    __abstract__ = True 
    
    # --- COLUMNAS COMUNES HEREDADAS ---
    _nombre: str = db.Column("nombre", db.String(50), nullable=False, default="")
    _apellidos: str = db.Column("apellidos", db.String(100), nullable=True, default="")
    _telefono:str = db.Column("telefono", db.String(20), nullable=True, default="")
    _email:str = db.Column("email", db.String(120), unique=True, nullable=False, default="")
    _password_hash: str = db.Column("password_hash", db.String(255), nullable=False, default="")
    
    def __post_init__(self):
        """
        FUNCION PROPIA DE DATACLASS
        SE EJECUTA AUTOMÁTICAMENTE AL CREAR EL OBJETO.
        Llama a los setters para forzar que pasen por las valida validaciones.
        """
        if isinstance(self._nombre, str) and self._nombre:
            self.set_nombre(self._nombre)
            
        # 2. Validar Apellidos
        if isinstance(self._apellidos, str) and self._apellidos:
            self.set_apellidos(self._apellidos)
            
        # 3. Validar Teléfono
        if isinstance(self._telefono, str) and self._telefono:
            self.set_telefono(self._telefono)
            
        # 4. Validar Email
        if isinstance(self._email, str) and self._email:
            self.set_email(self._email)
            
        # 5. Validar Hash
        if isinstance(self._password_hash, str) and self._password_hash:
            self.set_password_hash(self._password_hash)
    
    # --- GETTERS ---
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_apellidos(self) -> str:  
        return self._apellidos
    
    def get_telefono(self) -> str:
        return self._telefono
    
    def get_email(self) -> str:
        return self._email
    
    def get_password_hash(self)-> str:
        return self._password_hash

    # --- SETTERS ---
    def set_nombre(self, nombre: str):
        if not nombre or len(nombre.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = nombre
    
    def set_apellidos(self, apellidos: str):
        if not apellidos or len(apellidos.strip()) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres.")
        self._apellidos = apellidos
    
    def set_telefono(self, telefono: str):    
        if not telefono or len(telefono.strip()) != 9 or not telefono.isdigit():
            raise ValueError("El telefono no cumple los requisitos")
        self._telefono = telefono
    
    def set_email(self, email: str):
        if not email or "@" not in email: 
            raise ValueError("El email no es válido.")
        self._email = email
        
    def set_password_hash(self, password_hash: str):
        if not password_hash or len(password_hash) < 10: 
            raise ValueError("El hash de la contraseña no es válido.")
        self._password_hash = password_hash