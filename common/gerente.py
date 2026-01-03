from base import db, Persona
from dataclasses import dataclass

@dataclass
class Gerente(Persona):
    __tablename__ = 'ente'
    
    id_cliente: str
    password_hash: str
    
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)