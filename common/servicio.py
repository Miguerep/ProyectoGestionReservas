from .base import db
from dataclasses import dataclass

@dataclass
class Servicio(db.Model):
    __tablename__ = 'servicios'

    # CORRECCIÓN: Mapeo de id_servicio -> id
    id = db.Column("id_servicio", db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    duracion = db.Column("duracion", db.Integer, nullable=False) # Minutos

    # RELACIONES
    peluquerias = db.relationship(
        "Peluqueria",
        secondary="peluquerias_servicios",
        back_populates="servicios"
    )

   