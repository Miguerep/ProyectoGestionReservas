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
        
        
        
def mostrar_dashboard(self, token, id_peluqueria):
        """Llamado tras el login exitoso"""
        self.dashboard_view = CutTime_dashboard()
        
        # Obtener datos de la API
        resultado = self.cita_service.get_citas_por_peluqueria(id_peluqueria, token)
        
        if resultado["success"]:
            # Enviar los datos a la vista para que los pinte
            self.dashboard_view.rellenar_tabla(resultado["data"])
        
        self.dashboard_view.show()
        
        