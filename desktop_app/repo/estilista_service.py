import requests
from src.desktop_app.config import Config
from src.desktop_app.utils.auth_helper import AuthHelper


class EstilistaService:
    def __init__(self):
        self.auth_helper = AuthHelper()

    def get_estilistas_por_peluqueria(self, id_peluqueria, token=None, incluir_inactivos=False):
        """
        Obtiene los estilistas de una peluquería

        Args:
            id_peluqueria: ID de la peluquería
            token: (Opcional) Token manual, si no se proporciona usa AuthHelper
            incluir_inactivos: Si True, incluye estilistas inactivos

        Returns:
            dict: Resultado con 'success' y 'data' o 'error'
        """
        url = f"{Config.API_URL}/peluquerias/{id_peluqueria}/estilistas"
        params = {"incluir_inactivos": "true" if incluir_inactivos else "false"}

        # Si se proporciona token manualmente, usarlo
        if token:
            headers = {"Authorization": f"Bearer {token}"}
            try:
                response = requests.get(url, headers=headers, params=params)
                if response.status_code == 200:
                    return {"success": True, "data": response.json()}
                return {"success": False, "error": response.json().get("msg")}
            except Exception as e:
                return {"success": False, "error": str(e)}

        # Si no hay token manual, usar AuthHelper
        return self.auth_helper.make_authenticated_request("GET", url, params=params)

    def crear_estilista(self, id_peluqueria, data, token=None):
        """
        Crea un nuevo estilista

        Args:
            id_peluqueria: ID de la peluquería
            data: Diccionario con nombre, apellidos, telefono, email, password
            token: (Opcional) Token manual

        Returns:
            dict: Resultado con 'success' y 'data' o 'error'
        """
        url = f"{Config.API_URL}/peluquerias/{id_peluqueria}/estilistas"

        # Si se proporciona token manualmente, usarlo
        if token:
            headers = {"Authorization": f"Bearer {token}"}
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 201:
                    return {"success": True, "data": response.json()}
                return {"success": False, "error": response.json().get("msg")}
            except Exception as e:
                return {"success": False, "error": str(e)}

        # Si no hay token manual, usar AuthHelper
        return self.auth_helper.make_authenticated_request("POST", url, json=data)

    def actualizar_estilista(self, id_estilista, data, token=None):
        """
        Actualiza los datos de un estilista

        Args:
            id_estilista: ID del estilista
            data: Diccionario con los campos a actualizar
            token: (Opcional) Token manual

        Returns:
            dict: Resultado con 'success' y 'data' o 'error'
        """
        url = f"{Config.API_URL}/estilistas/{id_estilista}"

        # Si se proporciona token manualmente, usarlo
        if token:
            headers = {"Authorization": f"Bearer {token}"}
            try:
                response = requests.put(url, headers=headers, json=data)
                if response.status_code == 200:
                    return {"success": True, "data": response.json()}
                return {"success": False, "error": response.json().get("msg")}
            except Exception as e:
                return {"success": False, "error": str(e)}

        # Si no hay token manual, usar AuthHelper
        return self.auth_helper.make_authenticated_request("PUT", url, json=data)

    def desactivar_estilista(self, id_estilista, token=None):
        """
        Desactiva un estilista (borrado lógico)

        Args:
            id_estilista: ID del estilista
            token: (Opcional) Token manual

        Returns:
            dict: Resultado con 'success' y 'data' o 'error'
        """
        url = f"{Config.API_URL}/estilistas/{id_estilista}"

        # Si se proporciona token manualmente, usarlo
        if token:
            headers = {"Authorization": f"Bearer {token}"}
            try:
                response = requests.delete(url, headers=headers)
                if response.status_code == 200:
                    return {"success": True, "data": response.json()}
                return {"success": False, "error": response.json().get("msg")}
            except Exception as e:
                return {"success": False, "error": str(e)}

        # Si no hay token manual, usar AuthHelper
        return self.auth_helper.make_authenticated_request("DELETE", url)
