from .base import db
from dataclasses import dataclass

@dataclass
class CitaServicio(db.Model):
    __tablename__ = "citas_servicios"
    
    _id_citaServicio = db.Column("id_citaServicio", db.Integer, primary_key=True)
    _precioAplicado = db.Column("precioAplicado", db.Float, nullable=False)
 
    
    #Claves Foráneas
    _id_cita = db.Column("id_cita", db.Integer, 
                            db.ForeignKey("citas.id_cita"), nullable=False)
    _id_servicio = db.Column("id_servicio", db.Integer, 
                            db.ForeignKey("servicios.id_servicio"), nullable=False)
    
    # --- GETTERS --- 

    def get_id(self) -> int:
        return self._id_citaServicio

    def get_precioAplicado(self) -> float:
        return self._precioAplicado

    def get_servicio(self) -> int:
        return self._id_servicio
    
    def get_cita(self) -> int:
        return self._id_cita
    
    # --- SETTERS ---
    
    def set_precioAplicado(self, precioAplicado: float):
        self._precioAplicado = precioAplicado
    
    def set_servicio(self, servicio: int):
        self._id_servicio = servicio
    
    def set_cita(self, cita: int):
        self._id_cita = cita