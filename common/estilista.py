from .base import db, Persona
from dataclasses import dataclass

@dataclass
class Estilista(Persona):
    __tablename__ = 'estilistas'
    
    _id_estilista = db.Column("id_estilista", db.Integer, primary_key=True)
    _activo: bool = db.Column("activo", db.Boolean, default=True)
    _id_peluqueria: int = db.Column("id_peluqueria", db.Integer, 
                                db.ForeignKey('peluquerias.id_peluqueria'), nullable=True)
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id_estilista
    
    def is_activo(self) -> bool:
        return self._activo
    
    # --- SETTERS ---   
    def set_activo(self, estado: bool):
        self._activo = estado