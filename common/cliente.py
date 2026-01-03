from base import db, Persona
from dataclasses import dataclass


@dataclass
class Cliente(Persona):
    __tablename__ = 'Cliente'
    
    _id_cliente: str
    _password_hash: str
    
    _id_cliente = db.Column(db.Integer, primary_key=True)
    _nombre = db.Column(db.String(50), nullable=False)
    _apellidos = db.Column(db.String(100), nullable=True)
    _telefono = db.Column(db.String(20), nullable=True, unique=True)
    _password_hash = db.Column(db.String(100), nullable=False)
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self.id_cliente
    
    def get_password_hash(self) -> str:
        return self._password_hash
    
    # --- SETTERS ---
        
    def set_password_hash(self, password_hash: str):
        self._password_hash = password_hash
    
    
    