import sys
from src.desktop_app.controller.app_controller import AppController
from PySide6.QtWidgets import QApplication
from src.desktop_app.utils.theme_helper import ThemeHelper

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    theme_helper = ThemeHelper()
    theme_helper.apply_theme(app, "light")
    controller = AppController()
    sys.exit(app.exec())