from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt, QDateTime, QDate, QLocale
from src.desktop_app.ui.cutTime_dashboard_ui import Ui_MainWindow

class CutTime_dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Configuraciones visuales solamente
        self._configurar_tabla()
        self._configurar_fecha_hoy()

    def _configurar_fecha_hoy(self):
        """Establece la fecha actual en los headers y widgets"""
        hoy = QDate.currentDate()
        self.ui.lblFullDate.setText(QLocale().toString(hoy, "dddd, d 'de' MMMM 'de' yyyy"))
        self.ui.dateEdit.setDate(hoy)

    def _configurar_tabla(self):
        """Configuración estética y funcional de la tabla"""
        tabla = self.ui.tableAppointments
        header = tabla.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        tabla.setShowGrid(False)
        tabla.setAlternatingRowColors(True)

    def actualizar_tabla(self, lista_citas):
        
        """
        Recibe la lista de citas (JSON) desde el AppController y la pinta.
        """
        tabla = self.ui.tableAppointments
        tabla.setRowCount(0)

        for row_index, cita_raw in enumerate(lista_citas):
            # Procesamos datos (DTO simple interno)
            datos = self._procesar_datos_fila(cita_raw)
            
            tabla.insertRow(row_index)
            tabla.setItem(row_index, 0, QTableWidgetItem(datos['cliente']))
            tabla.setItem(row_index, 1, QTableWidgetItem(datos['servicio']))
            tabla.setItem(row_index, 2, QTableWidgetItem(datos['fecha']))
            tabla.setItem(row_index, 3, QTableWidgetItem(datos['hora']))
            tabla.setItem(row_index, 4, QTableWidgetItem(datos['precio']))
            tabla.setItem(row_index, 5, QTableWidgetItem(datos['estado']))
            
            # Alineación derecha para precio
            tabla.item(row_index, 4).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

    def _procesar_datos_fila(self, cita):
        """Ayudante para formatear los datos antes de pintarlos"""
        # Fecha
        fecha_str = cita.get("fecha", "")
        qdt = QDateTime.fromString(fecha_str, "yyyy-MM-dd HH:mm")
        fecha_fmt = qdt.toString("dd/MM/yyyy") if qdt.isValid() else fecha_str
        hora_fmt = qdt.toString("HH:mm") if qdt.isValid() else "--:--"
        
        # Precio
        precio = float(cita.get("precio_congelado", 0.0))
        
        return {
            "cliente": str(cita.get("cliente", "N/A")),
            "servicio": str(cita.get("servicio", "N/A")),
            "fecha": fecha_fmt,
            "hora": hora_fmt,
            "precio": f"{precio:.2f} €",
            "estado": str(cita.get("estado", ""))
        }
    
    def _actualizar_targetas(self, lista_citas):
        
        self.ui.card1