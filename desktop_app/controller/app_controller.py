
from src.desktop_app.utils.json_handler import JsonHandler
from src.desktop_app.controller.login import Login
from src.desktop_app.controller.cutTime_dashboard import CutTime_dashboard
from src.desktop_app.repo.cita_service import CitaService
from src.desktop_app.repo.auth_service import AuthService
from src.desktop_app.utils.token_manager import TokenManager


class AppController:
    def __init__(self):
        self.app_state = JsonHandler.load_json("app_state.json")
        self.login_view = Login()
        self.mainWindow = None
        self.cita_service = CitaService()
        self.auth_service = AuthService()
        self.token_manager = TokenManager()

        self.login_view.login_exitoso.connect(self.mostrar_dashboard)

        # Intentar auto-login con tokens guardados
        if not self.intentar_auto_login():
            # Si no hay sesión guardada o falló, mostrar login
            self.login_view.show()

    def intentar_auto_login(self):
        """
        Intenta realizar auto-login usando tokens guardados

        Returns:
            bool: True si el auto-login fue exitoso, False en caso contrario
        """
        # Verificar si hay una sesión guardada
        if not self.token_manager.has_saved_session():
            return False

        session = self.token_manager.get_saved_session()
        access_token = session["access_token"]
        refresh_token = session["refresh_token"]
        user_data = session["user_data"]

        # Primero, intentar verificar el access token actual
        verify_result = self.auth_service.verify_token(access_token)

        if verify_result.get("success"):
            # El access token es válido, usar directamente
            print(f"Auto-login exitoso para {user_data['nombre']}")
            self.mostrar_dashboard(user_data, access_token)
            return True

        # Si el access token expiró, intentar refrescarlo
        print("Access token expirado, intentando refrescar...")
        refresh_result = self.auth_service.refresh_token(refresh_token)

        if refresh_result.get("success"):
            # Refresh exitoso, actualizar el access token
            new_access_token = refresh_result["access_token"]
            self.token_manager.update_access_token(new_access_token)

            print(f"Token refrescado exitosamente para {user_data['nombre']}")
            self.mostrar_dashboard(user_data, new_access_token)
            return True

        # Si ambos tokens fallaron, limpiar la sesión y mostrar login
        print("Sesión expirada, se requiere nuevo login")
        self.token_manager.clear_tokens()
        return False
        
    def mostrar_dashboard(self, user_data, token):
        print(f"¡Señal recibida! Usuario: {user_data["nombre"]}")
        print(f"Token guardado: {token}")
        self.mainWindow = CutTime_dashboard()
        
        self.login_view.close()
        
        # 3. Llamar al servicio
        id_pelu = user_data["id"]
        resultado = self.cita_service.get_citas_por_peluqueria(id_pelu, token)

        if resultado["success"]:
            
            self.mainWindow.actualizar_tabla(resultado["data"])
        else:
            print(f"Error al cargar citas: {resultado['error']}")
        
        # 5. Mostrar la ventana
        self.mainWindow.show()