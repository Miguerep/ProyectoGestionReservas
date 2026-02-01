import requests
from dotenv import load_dotenv
import os
class AuthService():

    load_dotenv()
    
    BASE_URL = f"http://{os.getenv("DB_HOST")}:{os.getenv("API_PORT")}"
    
    def login(self, email, password, rol):
        endpoint = f"{self.BASE_URL}/login"
        payload = {
            "email": email,
            "password": password,
            "rol": rol
        }
        
        try:
            response = requests.post(endpoint, json=payload)
            
            if response.status_code == 200:
                data=response.json()
                
                
                return {
                    "success": True,
                    "user": data.get("user"),
                    "access_token": data.get("access_token")
                    
                }
            else:
                return {
                    "Code": response.status_code,
                    "Success": False,
                    "error": response.json().get("msg")
                }
        except Exception as e:
            return {"success": False, "error": f"Error de conexión: {str(e)}"}
            