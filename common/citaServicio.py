from .base import db
from dataclasses import dataclass

@dataclass
class CitaServicio(db.Model):
    __tablename__ = "citas_servicios"
    
    cita_id: int = db.Column("id_cita", db.Integer, db.ForeignKey("citas.id_cita"), primary_key=True)
    servicio_id: int = db.Column("id_servicio", db.Integer, db.ForeignKey("servicios.id_servicio"), primary_key=True)
    precio_aplicado: float = db.Column("precioAplicado", db.Float, nullable=False)

    cita = db.relationship("Cita", back_populates="detalle_servicio")