import requests
from src.desktop_app.utils.token_manager import TokenManager
from src.desktop_app.repo.auth_service import AuthService


class AuthHelper:
    """
    Helper para realizar peticiones autenticadas con refresh automático de tokens
    """

    def __init__(self):
        self.token_manager = TokenManager()
        self.auth_service = AuthService()

    def make_authenticated_request(self, method, endpoint, **kwargs):
        """
        Realiza una petición HTTP autenticada con manejo automático de token refresh

        Args:
            method (str): Método HTTP ('GET', 'POST', 'PUT', 'DELETE', etc.)
            endpoint (str): URL completa del endpoint
            **kwargs: Argumentos adicionales para requests (json, params, etc.)

        Returns:
            dict: Respuesta con 'success' y 'data' o 'error'
        """
        # Obtener access token
        access_token = self.token_manager.get_access_token()

        if not access_token:
            return {"success": False, "error": "No hay sesión activa"}

        # Agregar el token al header
        if "headers" not in kwargs:
            kwargs["headers"] = {}
        kwargs["headers"]["Authorization"] = f"Bearer {access_token}"

        try:
            # Realizar la petición
            response = requests.request(method, endpoint, **kwargs)

            # Si es exitosa, retornar
            if response.status_code in [200, 201]:
                return {"success": True, "data": response.json()}

            # Si el token expiró (401), intentar refresh
            if response.status_code == 401:
                refresh_result = self._try_refresh_token()

                if refresh_result["success"]:
                    # Reintentar la petición con el nuevo token
                    kwargs["headers"]["Authorization"] = f"Bearer {refresh_result['new_token']}"
                    retry_response = requests.request(method, endpoint, **kwargs)

                    if retry_response.status_code in [200, 201]:
                        return {"success": True, "data": retry_response.json()}
                    else:
                        return {
                            "success": False,
                            "error": retry_response.json().get("msg", "Error en la petición"),
                            "status_code": retry_response.status_code
                        }
                else:
                    return {"success": False, "error": "Sesión expirada, inicie sesión nuevamente"}

            # Otros códigos de error
            return {
                "success": False,
                "error": response.json().get("msg", "Error en la petición"),
                "status_code": response.status_code
            }

        except Exception as e:
            return {"success": False, "error": f"Error de conexión: {str(e)}"}

    def _try_refresh_token(self):
        """
        Intenta refrescar el access token usando el refresh token

        Returns:
            dict: {'success': bool, 'new_token': str} o {'success': False}
        """
        refresh_token = self.token_manager.get_refresh_token()

        if not refresh_token:
            return {"success": False}

        refresh_result = self.auth_service.refresh_token(refresh_token)

        if refresh_result.get("success"):
            new_access_token = refresh_result["access_token"]
            self.token_manager.update_access_token(new_access_token)
            return {"success": True, "new_token": new_access_token}

        # Si el refresh falló, limpiar tokens
        self.token_manager.clear_tokens()
        return {"success": False}

    def get_current_token(self):
        """Obtiene el token actual, refrescándolo si es necesario"""
        access_token = self.token_manager.get_access_token()

        if not access_token:
            return None

        # Verificar si el token es válido
        verify_result = self.auth_service.verify_token(access_token)

        if verify_result.get("success"):
            return access_token

        # Si expiró, intentar refresh
        refresh_result = self._try_refresh_token()
        if refresh_result["success"]:
            return refresh_result["new_token"]

        return None

    def logout(self):
        """Cierra la sesión y limpia todos los tokens"""
        self.token_manager.clear_tokens()
