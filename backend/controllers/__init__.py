from flask import Blueprint

# Create main API blueprint
api = Blueprint("api", __name__)

# Import all controllers to register routes
from src.backend.controllers import auth_controller
from src.backend.controllers import cita_controller
from src.backend.controllers import peluqueria_controller
from src.backend.controllers import servicio_controller
from src.backend.controllers import estilista_controller
