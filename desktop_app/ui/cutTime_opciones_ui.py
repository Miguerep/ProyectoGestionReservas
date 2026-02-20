# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cutTime_opciones.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(842, 667)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 821, 641))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTituloOpciones = QLabel(self.verticalLayoutWidget)
        self.lblTituloOpciones.setObjectName(u"lblTituloOpciones")
        self.lblTituloOpciones.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTituloOpciones)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.estilistaList = QListWidget(self.verticalLayoutWidget)
        self.estilistaList.setObjectName(u"estilistaList")
        self.estilistaList.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.estilistaList)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.crearEstilistaPB = QPushButton(self.verticalLayoutWidget)
        self.crearEstilistaPB.setObjectName(u"crearEstilistaPB")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crearEstilistaPB.sizePolicy().hasHeightForWidth())
        self.crearEstilistaPB.setSizePolicy(sizePolicy)
        self.crearEstilistaPB.setMinimumSize(QSize(150, 35))

        self.horizontalLayout.addWidget(self.crearEstilistaPB)

        self.editarEstilistaPB = QPushButton(self.verticalLayoutWidget)
        self.editarEstilistaPB.setObjectName(u"editarEstilistaPB")
        self.editarEstilistaPB.setEnabled(False)
        sizePolicy.setHeightForWidth(self.editarEstilistaPB.sizePolicy().hasHeightForWidth())
        self.editarEstilistaPB.setSizePolicy(sizePolicy)
        self.editarEstilistaPB.setMinimumSize(QSize(150, 35))

        self.horizontalLayout.addWidget(self.editarEstilistaPB)

        self.eliminarEstilistaPB = QPushButton(self.verticalLayoutWidget)
        self.eliminarEstilistaPB.setObjectName(u"eliminarEstilistaPB")
        self.eliminarEstilistaPB.setEnabled(False)
        sizePolicy.setHeightForWidth(self.eliminarEstilistaPB.sizePolicy().hasHeightForWidth())
        self.eliminarEstilistaPB.setSizePolicy(sizePolicy)
        self.eliminarEstilistaPB.setMinimumSize(QSize(150, 35))

        self.horizontalLayout.addWidget(self.eliminarEstilistaPB)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblTituloOpciones.setText(QCoreApplication.translate("Form", u"Opciones Peluquer\u00eda", None))
        self.crearEstilistaPB.setText(QCoreApplication.translate("Form", u"Crear Estilista", None))
        self.editarEstilistaPB.setText(QCoreApplication.translate("Form", u"Editar Estilista", None))
        self.eliminarEstilistaPB.setText(QCoreApplication.translate("Form", u"Eliminar Estilista", None))
    # retranslateUi

