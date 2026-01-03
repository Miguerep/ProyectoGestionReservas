from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy();


@dataclass
class Persona:
    _nombre: str
    _apellidos: str
    _telefono: str
    
    # --- GETTERS ---
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_apellidos(self) -> str:  
        return self._apellidos
    
    def get_telefono(self) -> str:
        return self._telefono
    
        # --- SETTERS ---
    def set_nombre(self, nombre: str):
        if not nombre or len(nombre.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = nombre
    
    def set_apellidos(self, apellidos: str):
        if not apellidos or len(apellidos.strip()) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres.")
        self._apellidos = apellidos
    
    def set_telefono(self, telefono: str):    
        if not telefono or len(telefono.strip()) != 9 or not telefono.isdigit():
            raise ValueError("El telefono no cumple los requisitos")
        self._telefono = telefono