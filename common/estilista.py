from .base import db, Persona
from dataclasses import dataclass

@dataclass
class Estilista(Persona):
    __tablename__ = 'estilistas'
    
    # CORRECCIÓN: Mapeamos 'id_estilista' a 'id'
    id = db.Column("id_estilista", db.Integer, primary_key=True)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    id_peluqueria = db.Column(db.Integer, db.ForeignKey('peluquerias.id_peluqueria'), nullable=False)
    