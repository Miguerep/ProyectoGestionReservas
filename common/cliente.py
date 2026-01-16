from .base import db, Persona
from dataclasses import dataclass

@dataclass
class Cliente(Persona):
    __tablename__ = 'clientes'    
    
    _id_cliente: int = db.Column("id_cliente", db.Integer, primary_key=True)  
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id_cliente


    
    
    