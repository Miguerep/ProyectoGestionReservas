from base import db
from dataclasses import dataclass

@dataclass
class Cita(db.Model):
    __tablename__ = "citasz"