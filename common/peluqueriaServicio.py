from .base import db
from dataclasses import dataclass

@dataclass
class PeluqueriaServicio(db.Model):
    """
    Tabla intermedia para la relación Muchos-a-Muchos entre Peluquería y Servicio.
    Indica qué servicios ofrece cada local.
    """
    __tablename__ = 'peluquerias_servicios'
    
    # Claves foráneas apuntando a las tablas reales
    id_peluqueria = db.Column(db.Integer, db.ForeignKey('peluquerias.id_peluqueria'), primary_key=True)
    id_servicio = db.Column(db.Integer, db.ForeignKey('servicios.id_servicio'), primary_key=True)
    