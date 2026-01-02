from PySide6.QtWidgets import QApplication
from cutTime_dashboard import cutTime_dashboard
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = cutTime_dashboard()
    ventana.show()
    sys.exit(app.exec())

