from .base import db
from dataclasses import dataclass

@dataclass
class Peluqueria(db.Model):
    __tablename__ = "peluquerias"
    
    _id_peluqueria = db.Column("id_peluqueria", db.Integer, primary_key=True)
    _nombre = db.Column("nombre", db.String(50), nullable=False)
    _direccion = db.Column("direccion", db.String(50), nullable=False)
    _telefono = db.Column("telefono", db.String(20), nullable=True, unique=True)
      
    # --- GETTERS --- 
    def get_id(self) -> int:
        return self._id_peluqueria
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_direccion(self) -> str:
        return self._direccion
    
    def get_telefono(self) -> str:
        return self._telefono
    
    # --- SETTERS ---
    
    def set_nombre(self, nombre: str):
        self._nombre = nombre
        
    def set_direccion(self, direccion: str):
        self._direccion = direccion
    
    def set_telefono(self, telefono: str):
        self._telefono = telefono
        
    
 