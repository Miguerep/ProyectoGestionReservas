# Importamos el objeto db y la clase base Persona para que estén accesibles
from base import db, Persona

# Importamos todos los modelos de los archivos que hemos creado
from .cliente import Cliente
from .gerente import Gerente
from .estilista import Estilista
from .servicio import Servicio
from .cita import Cita, CitaServicio

# Definimos __all__ para facilitar las importaciones masivas y el control de visibilidad
__all__ = [
    'db',
    'Persona',
    'Cliente',
    'Estilista',
    'Servicio',
    'Cita',
    'CitaServicio'
]