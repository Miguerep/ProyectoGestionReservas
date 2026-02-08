from .base import db
from dataclasses import dataclass

@dataclass
class Peluqueria(db.Model):
    __tablename__ = 'peluquerias'
    
    id = db.Column("id_peluqueria", db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False, unique=True)

    # Relación con Servicios (Muchos-a-Muchos)
    servicios = db.relationship(
        "Servicio",
        secondary="peluquerias_servicios",
        back_populates="peluquerias"
    )
    
    # Relación con Estilistas (Uno-a-Muchos)
    estilistas = db.relationship("Estilista", backref="peluqueria_ref", lazy=True)