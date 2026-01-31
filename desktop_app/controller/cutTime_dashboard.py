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
        
def rellenar_tabla(self, lista_citas):
        """Limpia y llena el tableWidget con los datos de la API"""
        self.ui.tableWidget.setRowCount(0)
        for row, cita in enumerate(lista_citas):
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(cita["fecha"]))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(cita["cliente"]))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(cita["servicio"]))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(cita["estado"]))
                   
        

        
       

        
        