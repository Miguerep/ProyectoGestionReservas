import sys
from src.desktop_app.controller.app_controller import AppController
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    controller = AppController()
    sys.exit(app.exec())