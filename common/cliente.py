from base import db, Persona
from dataclasses import dataclass

@dataclass
class Cliente(db.Model, Persona):
    __tablename__ = 'clientes'    
    
    _id_cliente = db.Column("id_cliente", db.Integer, primary_key=True)
    _nombre = db.Column("nombre", db.String(50), nullable=False)
    _apellidos = db.Column("apellidos", db.String(100), nullable=True)
    _telefono = db.Column("telefono", db.String(20), nullable=True, unique=True)
    _password_hash = db.Column("password_hash", db.String(255), nullable=False)
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id_cliente
    
    def get_password_hash(self) -> str:
        return self._password_hash
    
    # --- SETTERS ---
        
    def set_password_hash(self, password_hash: str):
        self._password_hash = password_hash
    
    
    