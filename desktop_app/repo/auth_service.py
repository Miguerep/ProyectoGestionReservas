import requests
from dotenv import load_dotenv
import os
import src.desktop_app.config as Config

class AuthService():
    _token = None
    _user_data = None

    load_dotenv()
    
    BASE_URL = f"http://{os.getenv("DB_HOST")}:{os.getenv("API_PORT")}"
    
    def login(self, email, password, rol):
            """Realiza la petición HTTP de login al backend"""
            try:
                url = f"{Config.API_URL}/login"
                payload = {
                    "email": email,
                    "password": password,
                    "rol": rol
                }
                response = requests.post(url, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    # ¡AQUÍ ESTÁ LA CLAVE! Guardamos el token automáticamente
                    AuthService.set_session(data.get("access_token"), data.get("user"))
                    return {"success": True}
                else:
                    return {"success": False, "msg": response.json().get("msg", "Error desconocido")}
                    
            except Exception as e:
                return {"success": False, "msg": f"Error de conexión: {str(e)}"}

    # --- MÉTODOS DE GESTIÓN DE SESIÓN ---
    
    @classmethod
    def set_session(cls, token, user_data):
        """Guarda el token y datos del usuario"""
        cls._token = token
        cls._user_data = user_data

    @classmethod
    def get_token(cls):
        """Recupera el token actual (para usarlo en otras peticiones)"""
        return cls._token

    @classmethod
    def get_user(cls):
        """Recupera los datos del usuario logueado"""
        return cls._user_data
        
    @classmethod
    def logout(cls):
        """Cierra sesión limpiando los datos"""
        cls._token = None
        cls._user_data = None