from base import db
from dataclasses import dataclass

@dataclass
class PeluqueriaServicio(db.Model):
    __tablename__ = "peluquerias_servicios"
    
    _id_peluqueriaServicio = db.Column("id_peluqueriaServicio", db.Integer, primary_key=True)
    _precioEspecial = db.Column("precioEspecial", db.Float, nullable=False)
 
    
    #Claves Foráneas
    _id_peluqueria = db.Column("id_peluqueria", db.Integer, 
                            db.ForeignKey("peluquerias.id_peluqueria"), nullable=False)
    _id_servicio = db.Column("id_servicio", db.Integer, 
                            db.ForeignKey("servicios.id_servicio"), nullable=False)
    
    # --- GETTERS --- 

    def get_id(self) -> int:
        return self._id_peluqueriaServicio

    def get_precioEspecial(self) -> float:
        return self._precioEspecial

    def get_servicio(self) -> int:
        return self._id_servicio
    
    def get_peluqueria(self) -> int:
        return self._id_peluqueria
    
    # --- SETTERS ---
    
    def set_precioEspecial(self, precioEspecial: float):
        self._precioEspecial = precioEspecial
    
    def set_servicio(self, servicio: int):
        self._id_servicio = servicio
    
    def set_peluqueria(self, peluqueria: int):
        self._id_peluqueria = peluqueria