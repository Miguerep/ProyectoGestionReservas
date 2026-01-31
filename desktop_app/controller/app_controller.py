import sys
from src.desktop_app.utils.json_handler import JsonHandler
from src.desktop_app.controller.login import Login
from src.desktop_app.controller.cutTime_dashboard import CutTime_dashboard
from src.desktop_app.repo.cita_service import CitaService

class AppController:
    def __init__(self):
        
        self.app_state = JsonHandler.load_json("app_state.json")
        self.login_view = Login()
        self.mainWindow = None
        self.cita_service = CitaService()
        self.login_view.login_exitoso.connect(self.mostrar_dashboard)
        self.login_view.show()
        
        
        
    def mostrar_dashboard(self, user_data, token):
        print(f"¡Señal recibida! Usuario: {user_data['nombre']}")
        print(f"Token guardado: {token}")
        self.mainWindow = CutTime_dashboard()
        
        self.login_view.close()
        
        id_pelu = 1 # Esto deberías obtenerlo de los datos del gerente logueado
        resultado = self.cita_service.get_citas_por_peluqueria(id_pelu, token)

        if resultado["success"]:
            # 3. LE PASAMOS LOS DATOS A LA VISTA
            self.dashboard.actualizar_tabla(resultado["data"])
        else:
            print(f"Error al cargar citas: {resultado['error']}")
        self.mainWindow.show()
        
        