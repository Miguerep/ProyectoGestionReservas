from .base import db, Persona
from dataclasses import dataclass

@dataclass
class Gerente(Persona):
    __tablename__ = 'gerentes'
    
    # CORRECCIÓN: Mapeamos la columna 'id_gerente' al atributo 'id'
    id: int = db.Column("id_gerente", db.Integer, primary_key=True)
    