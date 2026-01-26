from  src.desktop_app.repo.auth_service import AuthService
from  src.desktop_app.ui.cutTime_logIn_ui import Ui_LoginScreen
from PySide6.QtWidgets import QWidget, QMessageBox

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.auth = AuthService()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        
        self.ui.userLE.textChanged.connect(self._login)  
        self.ui.passLE.textChanged.connect(self._login)  
        self.ui.loginButton.clicked.connect(self._login)
        
    def _login(self):
        email = self.ui.userLE.text() 
        password = self.ui.passLE.text() 
        rol = "gerente"
        
        resultado = self.auth.login(email, password, rol)
        
        if resultado["success"]:
            print ("login correcto")
        
        else: 
            QMessageBox.warning(self, "Error", "Correo o contraseña incorrectos.")