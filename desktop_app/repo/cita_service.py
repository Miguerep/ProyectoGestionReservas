import requests
from src.desktop_app.config import Config
from src.desktop_app.utils.auth_helper import AuthHelper


class CitaService:
    def __init__(self):
        self.auth_helper = AuthHelper()

    def get_citas_por_peluqueria(self, id_peluqueria, token=None):
        """
        Obtiene las citas de una peluquería

        Args:
            id_peluqueria: ID de la peluquería
            token: (Opcional) Token manual, si no se proporciona usa AuthHelper

        Returns:
            dict: Resultado con 'success' y 'data' o 'error'
        """
        url = f"{Config.API_URL}/peluquerias/{id_peluqueria}/citas"

        # Si se proporciona token manualmente, usarlo (modo legacy)
        if token:
            headers = {"Authorization": f"Bearer {token}"}
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return {"success": True, "data": response.json()}
                return {"success": False, "error": response.json().get("msg")}
            except Exception as e:
                return {"success": False, "error": str(e)}

        # Si no hay token manual, usar AuthHelper (modo recomendado)
        return self.auth_helper.make_authenticated_request("GET", url)