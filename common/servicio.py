from .base import db
from dataclasses import dataclass

@dataclass
class Servicio(db.Model):
    __tablename__ = "servicios"
    
    _id_servicio = db.Column("id_servicio", db.Integer, primary_key=True)
    _nombre = db.Column("nombre", db.String(50), nullable=False)
    _duracion = db.Column("duracion", db.Integer, nullable=False)
    _precio = db.Column("precio", db.Float(20), nullable=True, unique=True)
      
    # --- GETTERS --- 
    def get_id(self) -> int:
        return self._id_servicio
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_duracion(self) -> int:
        return self._duracion
    
    def get_precio(self) -> float:
        return self._precio
    
    # --- SETTERS ---
    
    def set_nombre(self, nombre: str):
        self._nombre = nombre
        
    def set_duracion(self, duracion: int):
        self._duracion = duracion
    
    def set_precio(self, precio: float):
        self._precio = precio
  