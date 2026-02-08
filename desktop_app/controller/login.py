from src.desktop_app.repo.auth_service import AuthService
from src.desktop_app.ui.cutTime_logIn_ui import Ui_LoginScreen
from src.desktop_app.utils.token_manager import TokenManager
from PySide6.QtWidgets import QWidget, QMessageBox, QCheckBox
from PySide6.QtCore import Signal


class Login(QWidget):
    login_exitoso = Signal(dict, str)

    def __init__(self):
        super().__init__()
        self.auth = AuthService()
        self.token_manager = TokenManager()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self._login)

        # Agregar checkbox "Recordarme" si no existe en el UI
        # (Esto es opcional, puedes siempre guardar los tokens)
        self.remember_me = True  # Por defecto siempre recordar

    def _login(self):
        email = self.ui.userLE.text()
        password = self.ui.passLE.text()
        rol = "gerente"

        resultado = self.auth.login(email, password, rol)

        if resultado.get("success"):
            user = resultado.get("user")
            access_token = resultado.get("access_token")
            refresh_token = resultado.get("refresh_token")

            # Guardar tokens y datos del usuario de forma segura
            if self.remember_me:
                self.token_manager.save_tokens(access_token, refresh_token, user)

            self.login_exitoso.emit(user, access_token)

        else:
            QMessageBox.warning(self, "Error", "Correo o contraseña incorrectos.")