# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cutTime_dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1161, 778)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #f5f7fb;\n"
"}\n"
"QWidget {\n"
"	font-family: \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif;\n"
"	color: #333333;\n"
"}\n"
"QLineEdit {\n"
"	background-color: white;\n"
"	border: 1px solid #e0e0e0;\n"
"	border-radius: 8px;\n"
"	padding: 10px;\n"
"	color: #333;\n"
"}\n"
"QComboBox {\n"
"	background-color: white;\n"
"	border: 1px solid #e0e0e0;\n"
"	border-radius: 8px;\n"
"	padding: 8px 15px;\n"
"	color: #555;\n"
"}\n"
"QDateEdit {\n"
"	background-color: white;\n"
"	border: 1px solid #e0e0e0;\n"
"	border-radius: 8px;\n"
"	padding: 8px 15px;\n"
"	color: #555;\n"
"}\n"
"QComboBox::drop-down {\n"
"	border: none;\n"
"}\n"
"QTableWidget {\n"
"	background-color: white;\n"
"	border: 1px solid #e0e0e0;\n"
"	border-radius: 12px;\n"
"	gridline-color: transparent;\n"
"	outline: none;\n"
"}\n"
"QHeaderView::section {\n"
"	background-color: white;\n"
"	padding: 10px;\n"
"	border: none;\n"
"	border-bottom: 2px solid #f0f0f0;\n"
"	font-weight: bold;\n"
"	color: #555;\n"
"}\n"
"QTableW"
                        "idget::item {\n"
"	padding: 10px;\n"
"	border-bottom: 1px solid #f5f7fb;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_Main = QVBoxLayout(self.centralwidget)
        self.verticalLayout_Main.setSpacing(20)
        self.verticalLayout_Main.setObjectName(u"verticalLayout_Main")
        self.verticalLayout_Main.setContentsMargins(30, 20, 30, 30)
        self.headerContainer = QWidget(self.centralwidget)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_Header = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_Header.setObjectName(u"horizontalLayout_Header")
        self.horizontalLayout_Header.setContentsMargins(0, 0, 0, 10)
        self.logo = QLabel(self.headerContainer)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(40, 40))
        self.logo.setMaximumSize(QSize(40, 40))
        self.logo.setStyleSheet(u"background-color: #d438d4; border-radius: 8px; color: white; font-size: 20px; font-weight: bold;")
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_Header.addWidget(self.logo)

        self.titleWidget = QWidget(self.headerContainer)
        self.titleWidget.setObjectName(u"titleWidget")
        self.verticalLayout_Title = QVBoxLayout(self.titleWidget)
        self.verticalLayout_Title.setSpacing(0)
        self.verticalLayout_Title.setObjectName(u"verticalLayout_Title")
        self.verticalLayout_Title.setContentsMargins(10, 0, 0, 0)
        self.lblAppName = QLabel(self.titleWidget)
        self.lblAppName.setObjectName(u"lblAppName")
        self.lblAppName.setStyleSheet(u"font-size: 20px; font-weight: bold;")

        self.verticalLayout_Title.addWidget(self.lblAppName)

        self.lblAppSub = QLabel(self.titleWidget)
        self.lblAppSub.setObjectName(u"lblAppSub")
        self.lblAppSub.setStyleSheet(u"color: #888; font-size: 13px;")

        self.verticalLayout_Title.addWidget(self.lblAppSub)


        self.horizontalLayout_Header.addWidget(self.titleWidget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Header.addItem(self.horizontalSpacer)

        self.dateWidget = QWidget(self.headerContainer)
        self.dateWidget.setObjectName(u"dateWidget")
        self.verticalLayout_Date = QVBoxLayout(self.dateWidget)
        self.verticalLayout_Date.setSpacing(2)
        self.verticalLayout_Date.setObjectName(u"verticalLayout_Date")
        self.lblToday = QLabel(self.dateWidget)
        self.lblToday.setObjectName(u"lblToday")
        self.lblToday.setStyleSheet(u"color: #888;")
        self.lblToday.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_Date.addWidget(self.lblToday)

        self.lblFullDate = QLabel(self.dateWidget)
        self.lblFullDate.setObjectName(u"lblFullDate")
        self.lblFullDate.setStyleSheet(u"font-weight: bold;")
        self.lblFullDate.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_Date.addWidget(self.lblFullDate)


        self.horizontalLayout_Header.addWidget(self.dateWidget)


        self.verticalLayout_Main.addWidget(self.headerContainer)

        self.cardsContainer = QWidget(self.centralwidget)
        self.cardsContainer.setObjectName(u"cardsContainer")
        self.horizontalLayout_Cards = QHBoxLayout(self.cardsContainer)
        self.horizontalLayout_Cards.setSpacing(20)
        self.horizontalLayout_Cards.setObjectName(u"horizontalLayout_Cards")
        self.horizontalLayout_Cards.setContentsMargins(0, 0, 0, 0)
        self.card1 = QFrame(self.cardsContainer)
        self.card1.setObjectName(u"card1")
        self.card1.setStyleSheet(u"background-color: white; border-radius: 12px; border: 1px solid #e0e0e0;")
        self.card1.setFrameShape(QFrame.Shape.StyledPanel)
        self.card1.setFrameShadow(QFrame.Shadow.Raised)
        self.vl_c1 = QVBoxLayout(self.card1)
        self.vl_c1.setObjectName(u"vl_c1")
        self.lblTitleAppointments = QLabel(self.card1)
        self.lblTitleAppointments.setObjectName(u"lblTitleAppointments")
        self.lblTitleAppointments.setStyleSheet(u"color: #888;")

        self.vl_c1.addWidget(self.lblTitleAppointments)

        self.lblValAppointments = QLabel(self.card1)
        self.lblValAppointments.setObjectName(u"lblValAppointments")
        self.lblValAppointments.setStyleSheet(u"font-size: 24px; font-weight: bold;")

        self.vl_c1.addWidget(self.lblValAppointments)


        self.horizontalLayout_Cards.addWidget(self.card1)

        self.card2 = QFrame(self.cardsContainer)
        self.card2.setObjectName(u"card2")
        self.card2.setStyleSheet(u"background-color: white; border-radius: 12px; border: 1px solid #e0e0e0;")
        self.card2.setFrameShape(QFrame.Shape.StyledPanel)
        self.vl_c2 = QVBoxLayout(self.card2)
        self.vl_c2.setObjectName(u"vl_c2")
        self.lblTitle2 = QLabel(self.card2)
        self.lblTitle2.setObjectName(u"lblTitle2")
        self.lblTitle2.setStyleSheet(u"color: #888;")

        self.vl_c2.addWidget(self.lblTitle2)

        self.lblVal2 = QLabel(self.card2)
        self.lblVal2.setObjectName(u"lblVal2")
        self.lblVal2.setStyleSheet(u"font-size: 24px; font-weight: bold;")

        self.vl_c2.addWidget(self.lblVal2)


        self.horizontalLayout_Cards.addWidget(self.card2)

        self.card3 = QFrame(self.cardsContainer)
        self.card3.setObjectName(u"card3")
        self.card3.setStyleSheet(u"background-color: white; border-radius: 12px; border: 1px solid #e0e0e0;")
        self.card3.setFrameShape(QFrame.Shape.StyledPanel)
        self.vl_c3 = QVBoxLayout(self.card3)
        self.vl_c3.setObjectName(u"vl_c3")
        self.lblTitleEarnings = QLabel(self.card3)
        self.lblTitleEarnings.setObjectName(u"lblTitleEarnings")
        self.lblTitleEarnings.setStyleSheet(u"color: #888;")

        self.vl_c3.addWidget(self.lblTitleEarnings)

        self.lblValEarnings = QLabel(self.card3)
        self.lblValEarnings.setObjectName(u"lblValEarnings")
        self.lblValEarnings.setStyleSheet(u"font-size: 24px; font-weight: bold;")

        self.vl_c3.addWidget(self.lblValEarnings)


        self.horizontalLayout_Cards.addWidget(self.card3)

        self.card4 = QFrame(self.cardsContainer)
        self.card4.setObjectName(u"card4")
        self.card4.setStyleSheet(u"background-color: white; border-radius: 12px; border: 1px solid #e0e0e0;")
        self.card4.setFrameShape(QFrame.Shape.StyledPanel)
        self.vl_c4 = QVBoxLayout(self.card4)
        self.vl_c4.setObjectName(u"vl_c4")
        self.lblTitlePending = QLabel(self.card4)
        self.lblTitlePending.setObjectName(u"lblTitlePending")
        self.lblTitlePending.setStyleSheet(u"color: #888;")

        self.vl_c4.addWidget(self.lblTitlePending)

        self.lblValPending = QLabel(self.card4)
        self.lblValPending.setObjectName(u"lblValPending")
        self.lblValPending.setStyleSheet(u"font-size: 24px; font-weight: bold;")

        self.vl_c4.addWidget(self.lblValPending)


        self.horizontalLayout_Cards.addWidget(self.card4)


        self.verticalLayout_Main.addWidget(self.cardsContainer)

        self.filterFrame = QFrame(self.centralwidget)
        self.filterFrame.setObjectName(u"filterFrame")
        self.filterFrame.setStyleSheet(u"QFrame#filterFrame { background-color: white; border-radius: 12px; border: 1px solid #e0e0e0; }")
        self.filterFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.filterFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_Filters = QHBoxLayout(self.filterFrame)
        self.horizontalLayout_Filters.setObjectName(u"horizontalLayout_Filters")
        self.horizontalLayout_Filters.setContentsMargins(15, 10, 15, 10)
        self.searchEdit = QLineEdit(self.filterFrame)
        self.searchEdit.setObjectName(u"searchEdit")

        self.horizontalLayout_Filters.addWidget(self.searchEdit)

        self.comboStatus = QComboBox(self.filterFrame)
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.setObjectName(u"comboStatus")
        self.comboStatus.setMinimumSize(QSize(143, 36))
        self.comboStatus.setMouseTracking(False)

        self.horizontalLayout_Filters.addWidget(self.comboStatus)

        self.dateEdit = QDateEdit(self.filterFrame)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMinimumSize(QSize(130, 36))
        self.dateEdit.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.horizontalLayout_Filters.addWidget(self.dateEdit)


        self.verticalLayout_Main.addWidget(self.filterFrame)

        self.tableAppointments = QTableWidget(self.centralwidget)
        if (self.tableAppointments.columnCount() < 7):
            self.tableAppointments.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableAppointments.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableAppointments.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableAppointments.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableAppointments.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableAppointments.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableAppointments.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableAppointments.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableAppointments.setObjectName(u"tableAppointments")
        self.tableAppointments.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tableAppointments.setShowGrid(False)
        self.tableAppointments.setSortingEnabled(True)
        self.tableAppointments.horizontalHeader().setStretchLastSection(True)
        self.tableAppointments.verticalHeader().setVisible(False)

        self.verticalLayout_Main.addWidget(self.tableAppointments)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CutTime Dashboard", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"\u2702", None))
        self.lblAppName.setText(QCoreApplication.translate("MainWindow", u"CutTime", None))
        self.lblAppSub.setText(QCoreApplication.translate("MainWindow", u"Panel de gesti\u00f3n de citas", None))
        self.lblToday.setText(QCoreApplication.translate("MainWindow", u"Hoy", None))
        self.lblFullDate.setText(QCoreApplication.translate("MainWindow", u"FECHA", None))
        self.lblTitleAppointments.setText(QCoreApplication.translate("MainWindow", u"Citas hoy", None))
        self.lblValAppointments.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblTitle2.setText(QCoreApplication.translate("MainWindow", u"Total citas", None))
        self.lblVal2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.lblTitleEarnings.setText(QCoreApplication.translate("MainWindow", u"Ingresos", None))
        self.lblValEarnings.setText(QCoreApplication.translate("MainWindow", u"0\u20ac", None))
        self.lblTitlePending.setText(QCoreApplication.translate("MainWindow", u"Pendientes", None))
        self.lblValPending.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Buscar por nombre, tel\u00e9fono o servicio...", None))
        self.comboStatus.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos los estados", None))
        self.comboStatus.setItemText(1, QCoreApplication.translate("MainWindow", u"Confirmada", None))
        self.comboStatus.setItemText(2, QCoreApplication.translate("MainWindow", u"Pendiente", None))

        ___qtablewidgetitem = self.tableAppointments.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem1 = self.tableAppointments.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Servicio", None));
        ___qtablewidgetitem2 = self.tableAppointments.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem3 = self.tableAppointments.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem4 = self.tableAppointments.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem5 = self.tableAppointments.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem6 = self.tableAppointments.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Acciones", None));
    # retranslateUi

