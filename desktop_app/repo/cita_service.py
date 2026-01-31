import requests

class CitaService:
    BASE_URL = "http://127.0.0.1:5000"

    def get_citas_por_peluqueria(self, id_peluqueria, token):
        headers = {"Authorization": f"Bearer {token}"}
        try:
            response = requests.get(f"{self.BASE_URL}/peluquerias/{id_peluqueria}/citas", headers=headers)
            if response.status_code == 200:
                return {"success": True, "data": response.json()}
            return {"success": False, "error": response.json().get("msg")}
        except Exception as e:
            return {"success": False, "error": str(e)}