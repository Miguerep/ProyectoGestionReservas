# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cutTime_logIn.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(800, 600)
        self.verticalLayout_2 = QVBoxLayout(LoginScreen)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_top)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_left)

        self.cardFrame = QFrame(LoginScreen)
        self.cardFrame.setObjectName(u"cardFrame")
        self.cardFrame.setMinimumSize(QSize(400, 450))
        self.cardFrame.setMaximumSize(QSize(400, 500))
        self.cardFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.cardFrame)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 40, 40, 40)
        self.iconPlaceholder = QLabel(self.cardFrame)
        self.iconPlaceholder.setObjectName(u"iconPlaceholder")
        self.iconPlaceholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.iconPlaceholder)

        self.titleLabel = QLabel(self.cardFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.subtitleLabel = QLabel(self.cardFrame)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        self.subtitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.subtitleLabel)

        self.verticalSpacer_form = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_form)

        self.userLE = QLineEdit(self.cardFrame)
        self.userLE.setObjectName(u"userLE")

        self.verticalLayout.addWidget(self.userLE)

        self.passLE = QLineEdit(self.cardFrame)
        self.passLE.setObjectName(u"passLE")
        self.passLE.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.passLE)

        self.loginButton = QPushButton(self.cardFrame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.loginButton)


        self.horizontalLayout.addWidget(self.cardFrame)

        self.horizontalSpacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_right)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_bottom)


        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"CutTime - Iniciar Sesi\u00f3n", None))
        self.iconPlaceholder.setStyleSheet(QCoreApplication.translate("LoginScreen", u"font-size: 40px; border: none; background: transparent;", None))
        self.iconPlaceholder.setText(QCoreApplication.translate("LoginScreen", u"\u2702\ufe0f", None))
        self.titleLabel.setText(QCoreApplication.translate("LoginScreen", u"CutTime", None))
        self.subtitleLabel.setText(QCoreApplication.translate("LoginScreen", u"Bienvenido de nuevo", None))
        self.userLE.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Correo", None))
        self.passLE.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Contrase\u00f1a", None))
        self.loginButton.setText(QCoreApplication.translate("LoginScreen", u"Iniciar Sesi\u00f3n", None))
    # retranslateUi

