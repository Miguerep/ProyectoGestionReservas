from src.desktop_app.ui.cutTime_dashboard_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtCore import QDate

class CutTime_dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lblFullDate.setText(QDate.currentDate().toString("dd/MM/yyyy"))
        self.ui.dateEdit.setDate(QDate.currentDate())
        
    def actualizar_tabla(self, lista_citas):
        """Este método se encarga exclusivamente de la UI"""
        tabla = self.ui.tableAppointments 
        tabla.setRowCount(0)  # Limpiamos datos viejos

        for row_index, cita in enumerate(lista_citas):
            tabla.insertRow(row_index)
            
            # Insertamos cada celda (ajusta las claves si tu API devuelve otras)
            tabla.setItem(row_index, 0, QTableWidgetItem(str(cita.get("cliente"))))
            tabla.setItem(row_index, 1, QTableWidgetItem(str(cita.get("servicio"))))
            tabla.setItem(row_index, 2, QTableWidgetItem(str(cita.get("estilista"))))
            tabla.setItem(row_index, 3, QTableWidgetItem(str(cita.get("estilista"))))
            tabla.setItem(row_index, 4, QTableWidgetItem(str(cita.get("estado"))))