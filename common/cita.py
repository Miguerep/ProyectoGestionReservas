from .base import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cita(db.Model):
    __tablename__ = "citas"
    
    _id_cita = db.Column("id_cita", db.Integer, primary_key=True)
    _fecha = db.Column("fecha", db.DateTime, nullable=False)
    _estado = db.Column("estado", db.String(50), nullable=False)
    
    #Claves Foráneas
    _id_cliente = db.Column("id_cliente", db.Integer, 
                            db.ForeignKey("clientes.id_cliente"), nullable=False)
    _id_peluqueria = db.Column("id_peluqueria", db.Integer, 
                               db.ForeignKey('peluquerias.id_peluqueria'))
    _id_servicio = db.Column("id_servicio", db.Integer, 
                             db.ForeignKey('servicios.id_servicio'))
    
    # --- GETTERS --- 
    def get_id(self) -> int:
        return self._id_cita
    
    def get_fecha(self) -> datetime:
        return self._fecha
    
    def get_estado(self) -> str:
        return self._estado
    
    def get_cliente(self) -> int:
        return self._id_cliente
    
    # --- SETTERS ---
    
    def set_fecha(self, fecha: datetime):
        self._fecha = fecha
        
    def set_estado(self, estado: str):
        self._estado = estado
    
    def set_cliente(self, cliente: int):
        self._id_cliente = cliente
    
    def set_peluqueria(self, peluqueria: int):
        self._id_peluqueria = peluqueria
        
    def set_servicio(self, servicio: int):
        self._id_servicio = servicio
    
    
        