from  src.desktop_app.repo.auth_service import AuthService
from  src.desktop_app.ui.cutTime_logIn_ui import Ui_LoginScreen
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal


class Login(QWidget):
    login_exitoso = Signal(dict, str)
    
    def __init__(self):
        super().__init__()
        self.auth = AuthService()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
          
        self.ui.loginButton.clicked.connect(self._login)
        
    def _login(self):
        email = self.ui.userLE.text() 
        password = self.ui.passLE.text() 
        rol = "gerente"
        
        resultado = self.auth.login(email, password, rol)
    
        if resultado.get("success"):
            user = resultado.get("user")
            user_token = resultado.get("access_token")
            self.login_exitoso.emit(user, user_token)
        
        else: 
            QMessageBox.warning(self, "Error", "Correo o contraseña incorrectos.")