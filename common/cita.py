from .base import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cita(db.Model):
    __tablename__ = "citas"
    
    id: int = db.Column("id_cita", db.Integer, primary_key=True)
    fecha: datetime = db.Column("fecha", db.DateTime, nullable=False)
    estado: str = db.Column("estado", db.String(50), nullable=False)
    
    # Claves Foráneas
    cliente_id: int = db.Column("id_cliente", db.Integer, db.ForeignKey("clientes.id_cliente"), nullable=False)
    peluqueria_id: int = db.Column("id_peluqueria", db.Integer, db.ForeignKey('peluquerias.id_peluqueria'))
    servicio_id: int = db.Column("id_servicio", db.Integer, db.ForeignKey('servicios.id_servicio'))
    estilista_id: int = db.Column("id_estilista", db.Integer, db.ForeignKey('estilistas.id_estilista'), nullable=True)
    
    # RELACIONES (La magia del ORM)
    cliente = db.relationship("Cliente", back_populates="citas")
    servicio = db.relationship("Servicio") # Acceso directo a self.servicio.nombre
    peluqueria = db.relationship("Peluqueria")
    estilista = db.relationship("Estilista")
    
    # Relación con el detalle (precio)
    detalle_servicio = db.relationship("CitaServicio", back_populates="cita", uselist=False, cascade="all, delete-orphan")

    @property
    def precio_final(self):
        """Propiedad calculada: Fuente única de la verdad"""
        return self.detalle_servicio.precio_aplicado if self.detalle_servicio else 0.0