import requests
from src.desktop_app.config import Config # Importamos config

class CitaService:
    def get_citas_por_peluqueria(self, id_peluqueria, token):
        headers = {"Authorization": f"Bearer {token}"}
        try:
            # Usamos la URL de configuración
            url = f"{Config.API_URL}/peluquerias/{id_peluqueria}/citas"
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                return {"success": True, "data": response.json()}
            return {"success": False, "error": response.json().get("msg")}
        except Exception as e:
            return {"success": False, "error": str(e)}