from PySide6.QtCore import QSettings
import json


class TokenManager:
    """
    Gestor seguro de tokens usando QSettings.
    QSettings almacena datos de forma cifrada en el registro de Windows
    o archivos de configuración según el sistema operativo.
    """

    def __init__(self):
        # Configurar QSettings con nombre de organización y aplicación
        self.settings = QSettings("CutTime", "ReservationApp")

    def save_tokens(self, access_token, refresh_token, user_data):
        """
        Guarda los tokens y datos del usuario de forma segura

        Args:
            access_token (str): Token de acceso JWT
            refresh_token (str): Token de refresco JWT
            user_data (dict): Datos del usuario (id, nombre, email, rol)
        """
        self.settings.setValue("auth/access_token", access_token)
        self.settings.setValue("auth/refresh_token", refresh_token)
        self.settings.setValue("auth/user_data", json.dumps(user_data))
        self.settings.sync()  # Forzar guardado inmediato

    def get_access_token(self):
        """Obtiene el access token guardado"""
        return self.settings.value("auth/access_token", None)

    def get_refresh_token(self):
        """Obtiene el refresh token guardado"""
        return self.settings.value("auth/refresh_token", None)

    def get_user_data(self):
        """Obtiene los datos del usuario guardado"""
        user_json = self.settings.value("auth/user_data", None)
        if user_json:
            try:
                return json.loads(user_json)
            except json.JSONDecodeError:
                return None
        return None

    def update_access_token(self, new_access_token):
        """Actualiza solo el access token (usado después de refresh)"""
        self.settings.setValue("auth/access_token", new_access_token)
        self.settings.sync()

    def clear_tokens(self):
        """Elimina todos los tokens y datos del usuario (logout)"""
        self.settings.remove("auth/access_token")
        self.settings.remove("auth/refresh_token")
        self.settings.remove("auth/user_data")
        self.settings.sync()

    def has_saved_session(self):
        """Verifica si hay una sesión guardada"""
        return (
            self.get_access_token() is not None
            and self.get_refresh_token() is not None
            and self.get_user_data() is not None
        )

    def get_saved_session(self):
        """
        Obtiene la sesión completa guardada

        Returns:
            dict: Diccionario con access_token, refresh_token y user_data
                  o None si no hay sesión guardada
        """
        if not self.has_saved_session():
            return None

        return {
            "access_token": self.get_access_token(),
            "refresh_token": self.get_refresh_token(),
            "user_data": self.get_user_data()
        }
