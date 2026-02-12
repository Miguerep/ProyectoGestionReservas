import sys
from src.desktop_app.controller.app_controller import AppController
from PySide6.QtWidgets import QApplication
from src.desktop_app.utils.theme_helper import ThemeHelper

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    controller = AppController(app)
    sys.exit(app.exec())