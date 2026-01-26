import sys
from src.desktop_app.utils import JsonHandler
from src.desktop_app.controller.login import Login
class AppController:
    def __init__(self):
        
        self.app_state = JsonHandler.load_json("app_state.json")
        self.login_view = Login()
        self.mainWindow = None
    
        
        