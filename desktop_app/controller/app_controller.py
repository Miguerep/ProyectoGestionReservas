import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from utils import JsonHandler
class AppController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        self.app_state = JsonHandler.load_json("app_state.json")
        