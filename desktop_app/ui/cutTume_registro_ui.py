# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cutTume_registro.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_RegistroForm(object):
    def setupUi(self, RegistroForm):
        if not RegistroForm.objectName():
            RegistroForm.setObjectName(u"RegistroForm")
        RegistroForm.resize(600, 550)
        self.verticalLayout = QVBoxLayout(RegistroForm)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(80, 40, 80, 40)
        self.label_titulo = QLabel(RegistroForm)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_titulo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(15)
        self.label_nombre = QLabel(RegistroForm)
        self.label_nombre.setObjectName(u"label_nombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_nombre)

        self.input_nombre = QLineEdit(RegistroForm)
        self.input_nombre.setObjectName(u"input_nombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_nombre)

        self.label_apellidos = QLabel(RegistroForm)
        self.label_apellidos.setObjectName(u"label_apellidos")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_apellidos)

        self.input_apellidos = QLineEdit(RegistroForm)
        self.input_apellidos.setObjectName(u"input_apellidos")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_apellidos)

        self.label_telefono = QLabel(RegistroForm)
        self.label_telefono.setObjectName(u"label_telefono")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_telefono)

        self.input_telefono = QLineEdit(RegistroForm)
        self.input_telefono.setObjectName(u"input_telefono")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_telefono)

        self.label_email = QLabel(RegistroForm)
        self.label_email.setObjectName(u"label_email")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_email)

        self.input_email = QLineEdit(RegistroForm)
        self.input_email.setObjectName(u"input_email")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.input_email)

        self.label_pass = QLabel(RegistroForm)
        self.label_pass.setObjectName(u"label_pass")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_pass)

        self.input_password = QLineEdit(RegistroForm)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.input_password)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_buttons = QVBoxLayout()
        self.verticalLayout_buttons.setSpacing(15)
        self.verticalLayout_buttons.setObjectName(u"verticalLayout_buttons")
        self.btn_registrar = QPushButton(RegistroForm)
        self.btn_registrar.setObjectName(u"btn_registrar")
        self.btn_registrar.setMinimumSize(QSize(0, 45))
        self.btn_registrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_buttons.addWidget(self.btn_registrar)

        self.btn_cancelar = QPushButton(RegistroForm)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setMinimumSize(QSize(0, 45))
        self.btn_cancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_buttons.addWidget(self.btn_cancelar)


        self.verticalLayout.addLayout(self.verticalLayout_buttons)


        self.retranslateUi(RegistroForm)

        QMetaObject.connectSlotsByName(RegistroForm)
    # setupUi

    def retranslateUi(self, RegistroForm):
        RegistroForm.setWindowTitle(QCoreApplication.translate("RegistroForm", u"Registro de Usuario", None))
        self.label_titulo.setText(QCoreApplication.translate("RegistroForm", u"Crear Cuenta", None))
        self.label_nombre.setText(QCoreApplication.translate("RegistroForm", u"Nombre", None))
        self.input_nombre.setPlaceholderText(QCoreApplication.translate("RegistroForm", u"Tu nombre", None))
        self.label_apellidos.setText(QCoreApplication.translate("RegistroForm", u"Apellidos", None))
        self.input_apellidos.setPlaceholderText(QCoreApplication.translate("RegistroForm", u"Tus apellidos", None))
        self.label_telefono.setText(QCoreApplication.translate("RegistroForm", u"Tel\u00e9fono", None))
        self.input_telefono.setPlaceholderText(QCoreApplication.translate("RegistroForm", u"+34 600 000 000", None))
        self.label_email.setText(QCoreApplication.translate("RegistroForm", u"Email", None))
        self.input_email.setPlaceholderText(QCoreApplication.translate("RegistroForm", u"ejemplo@correo.com", None))
        self.label_pass.setText(QCoreApplication.translate("RegistroForm", u"Contrase\u00f1a", None))
        self.input_password.setPlaceholderText(QCoreApplication.translate("RegistroForm", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.btn_registrar.setText(QCoreApplication.translate("RegistroForm", u"Registrar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("RegistroForm", u"Cancelar", None))
    # retranslateUi

