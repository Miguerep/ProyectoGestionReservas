import requests
from dotenv import load_dotenv
import os


class AuthService():

    load_dotenv()

    BASE_URL = f"http://{os.getenv("DB_HOST")}:{os.getenv("API_PORT")}"

    def login(self, email, password, rol):
        """Realiza el login y retorna los tokens"""
        endpoint = f"{self.BASE_URL}/login"
        payload = {
            "email": email,
            "password": password,
            "rol": rol
        }

        try:
            response = requests.post(endpoint, json=payload)

            if response.status_code == 200:
                data = response.json()

                return {
                    "success": True,
                    "user": data.get("user"),
                    "access_token": data.get("access_token"),
                    "refresh_token": data.get("refresh_token")
                }
            else:
                return {
                    "code": response.status_code,
                    "success": False,
                    "error": response.json().get("msg")
                }
        except Exception as e:
            return {"success": False, "error": f"Error de conexión: {str(e)}"}

    def refresh_token(self, refresh_token):
        """Refresca el access token usando el refresh token"""
        endpoint = f"{self.BASE_URL}/refresh"
        headers = {
            "Authorization": f"Bearer {refresh_token}"
        }

        try:
            response = requests.post(endpoint, headers=headers)

            if response.status_code == 200:
                data = response.json()
                return {
                    "success": True,
                    "access_token": data.get("access_token")
                }
            else:
                return {
                    "success": False,
                    "error": response.json().get("msg", "Error al refrescar token")
                }
        except Exception as e:
            return {"success": False, "error": f"Error de conexión: {str(e)}"}

    def verify_token(self, access_token):
        """Verifica si el access token es válido"""
        endpoint = f"{self.BASE_URL}/verify"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        try:
            response = requests.get(endpoint, headers=headers)

            if response.status_code == 200:
                data = response.json()
                return {
                    "success": True,
                    "user": data.get("user")
                }
            else:
                return {
                    "success": False,
                    "error": response.json().get("msg", "Token inválido")
                }
        except Exception as e:
            return {"success": False, "error": f"Error de conexión: {str(e)}"}
            