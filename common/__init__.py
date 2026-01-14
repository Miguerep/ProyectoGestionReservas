# Importamos el objeto db y la clase base Persona para que estén accesibles
from .base import db, Persona

# Importamos todos los modelos de los archivos que hemos creado
from .cliente import Cliente
from .cita import Cita
from .servicio import Servicio
from .peluqueria import Peluqueria
from .estilista import Estilista
from .citaServicio import CitaServicio
from .peluqueriaServicio import PeluqueriaServicio

#  __all__ para facilitar las importaciones masivas y el control de visibilidad
__all__ = [
    'db',
    'Cliente',
    'Cita',
    'Servicio',
    'Peluqueria',
    'Estilista',
    'CitaServicio',
    'PeluqueriaServicio',
]