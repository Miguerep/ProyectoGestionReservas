import requests
from src.desktop_app.config import Config

class AuthService:
    # Variables de clase para mantener la sesión (Singleton)
    _token = None
    _user = None

    def login(self, email, password, rol):
        try:
            url = f"{Config.API_URL}/login"
            payload = {"email": email, "password": password, "rol": rol}
            
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                # GUARDAMOS LA SESIÓN AQUÍ AUTOMÁTICAMENTE
                AuthService.set_session(data.get("access_token"), data.get("user"))
                return {"success": True, "data": data}
            else:
                return {"success": False, "msg": response.json().get("msg", "Error desconocido")}
        except Exception as e:
            return {"success": False, "msg": f"Error de conexión: {str(e)}"}

    # --- MÉTODOS DE GESTIÓN DE SESIÓN ---
    @classmethod
    def set_session(cls, token, user):
        cls._token = token
        cls._user = user

    @classmethod
    def get_token(cls):
        """Recupera el token actual"""
        return cls._token

    @classmethod
    def get_user(cls):
        return cls._user