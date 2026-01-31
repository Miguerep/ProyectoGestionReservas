from .base import db, Persona
from dataclasses import dataclass

@dataclass
class Cliente(Persona):
    __tablename__ = 'clientes'    
    
    # Mapeamos la columna 'id_cliente' al atributo 'id'
    id: int = db.Column("id_cliente", db.Integer, primary_key=True)
    
    # RELACIÓN: Un cliente tiene muchas citas
    citas = db.relationship("Cita", back_populates="cliente", cascade="all, delete-orphan")

   