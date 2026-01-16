from .base import db, Persona
from dataclasses import dataclass

@dataclass
class Gerente(Persona):
    __tablename__ = 'gerentes'
    
    _id_gerente = db.Column("id_gerente", db.Integer, primary_key=True) 
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id_gerente