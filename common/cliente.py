from .base import db, Persona
from dataclasses import dataclass

@dataclass
class Cliente(Persona):
    __tablename__ = 'clientes'    
    
    id: int = db.Column("id_cliente", db.Integer, primary_key=True)

    citas = db.relationship("Cita", back_populates="cliente", cascade="all, delete-orphan")

   