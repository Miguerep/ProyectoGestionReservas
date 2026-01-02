from cutTime_dashboard_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QDate

class cutTime_dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lblFullDate.setText(QDate.currentDate().toString("dd/MM/yyyy"))
        self.ui.dateEdit.setDate(QDate.currentDate())
        

        
       

        
        