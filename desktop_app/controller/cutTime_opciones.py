from PySide6.QtWidgets import QWidget, QListWidgetItem, QMessageBox, QInputDialog, QDialog, QVBoxLayout, QFormLayout, QLineEdit, QDialogButtonBox
from PySide6.QtCore import Qt
from src.desktop_app.ui.cutTime_opciones_ui import Ui_Form
from src.desktop_app.repo.estilista_service import EstilistaService


class CutTime_Opciones(QWidget):
    def __init__(self, id_peluqueria, token):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.id_peluqueria = id_peluqueria
        self.token = token
        self.estilista_service = EstilistaService()
        self.estilistas_data = []

        # Conectar señales
        self.ui.crearEstilistaPB.clicked.connect(self.crear_estilista)
        self.ui.editarEstilistaPB.clicked.connect(self.editar_estilista)
        self.ui.eliminarEstilistaPB.clicked.connect(self.eliminar_estilista)
        self.ui.estilistaList.itemSelectionChanged.connect(self.on_selection_changed)

        # Cargar estilistas
        self.cargar_estilistas()

    def cargar_estilistas(self):
        """Carga la lista de estilistas desde el backend"""
        resultado = self.estilista_service.get_estilistas_por_peluqueria(
            self.id_peluqueria,
            self.token
        )

        if resultado["success"]:
            self.estilistas_data = resultado["data"]
            self.actualizar_lista()
        else:
            QMessageBox.warning(
                self,
                "Error",
                f"No se pudieron cargar los estilistas: {resultado['error']}"
            )

    def actualizar_lista(self):
        """Actualiza la lista visual de estilistas"""
        self.ui.estilistaList.clear()

        for estilista in self.estilistas_data:
            nombre_completo = f"{estilista['nombre']} {estilista['apellidos']}".strip()
            email = estilista['email']
            telefono = estilista.get('telefono', 'Sin teléfono')
            activo = "✓ Activo" if estilista['activo'] else "✗ Inactivo"

            texto = f"{nombre_completo} - {email} - {telefono} - {activo}"

            item = QListWidgetItem(texto)
            item.setData(Qt.ItemDataRole.UserRole, estilista['id'])
            self.ui.estilistaList.addItem(item)

    def on_selection_changed(self):
        """Habilita/deshabilita botones según la selección"""
        hay_seleccion = len(self.ui.estilistaList.selectedItems()) > 0
        self.ui.editarEstilistaPB.setEnabled(hay_seleccion)
        self.ui.eliminarEstilistaPB.setEnabled(hay_seleccion)

    def crear_estilista(self):
        """Abre un diálogo para crear un nuevo estilista"""
        dialog = EstilistaDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()

            resultado = self.estilista_service.crear_estilista(
                self.id_peluqueria,
                data,
                self.token
            )

            if resultado["success"]:
                QMessageBox.information(
                    self,
                    "Éxito",
                    "Estilista creado exitosamente"
                )
                self.cargar_estilistas()
            else:
                QMessageBox.warning(
                    self,
                    "Error",
                    f"No se pudo crear el estilista: {resultado['error']}"
                )

    def editar_estilista(self):
        """Abre un diálogo para editar el estilista seleccionado"""
        item_seleccionado = self.ui.estilistaList.currentItem()
        if not item_seleccionado:
            return

        id_estilista = item_seleccionado.data(Qt.ItemDataRole.UserRole)

        # Buscar los datos del estilista
        estilista = next((e for e in self.estilistas_data if e['id'] == id_estilista), None)
        if not estilista:
            return

        dialog = EstilistaDialog(self, estilista)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()

            resultado = self.estilista_service.actualizar_estilista(
                id_estilista,
                data,
                self.token
            )

            if resultado["success"]:
                QMessageBox.information(
                    self,
                    "Éxito",
                    "Estilista actualizado exitosamente"
                )
                self.cargar_estilistas()
            else:
                QMessageBox.warning(
                    self,
                    "Error",
                    f"No se pudo actualizar el estilista: {resultado['error']}"
                )

    def eliminar_estilista(self):
        """Desactiva el estilista seleccionado"""
        item_seleccionado = self.ui.estilistaList.currentItem()
        if not item_seleccionado:
            return

        id_estilista = item_seleccionado.data(Qt.ItemDataRole.UserRole)

        # Buscar los datos del estilista
        estilista = next((e for e in self.estilistas_data if e['id'] == id_estilista), None)
        if not estilista:
            return

        nombre = f"{estilista['nombre']} {estilista['apellidos']}".strip()

        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro de que desea desactivar a {nombre}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            resultado = self.estilista_service.desactivar_estilista(
                id_estilista,
                self.token
            )

            if resultado["success"]:
                QMessageBox.information(
                    self,
                    "Éxito",
                    "Estilista desactivado exitosamente"
                )
                self.cargar_estilistas()
            else:
                QMessageBox.warning(
                    self,
                    "Error",
                    f"No se pudo desactivar el estilista: {resultado['error']}"
                )


class EstilistaDialog(QDialog):
    """Diálogo para crear/editar estilistas"""

    def __init__(self, parent=None, estilista_data=None):
        super().__init__(parent)
        self.estilista_data = estilista_data
        self.is_edit = estilista_data is not None

        self.setWindowTitle("Editar Estilista" if self.is_edit else "Crear Estilista")
        self.setMinimumWidth(400)

        self.setup_ui()

        if self.is_edit:
            self.load_data()

    def setup_ui(self):
        """Configura la interfaz del diálogo"""
        layout = QVBoxLayout()

        # Formulario
        form_layout = QFormLayout()

        self.nombre_input = QLineEdit()
        self.apellidos_input = QLineEdit()
        self.telefono_input = QLineEdit()
        self.email_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        form_layout.addRow("Nombre*:", self.nombre_input)
        form_layout.addRow("Apellidos:", self.apellidos_input)
        form_layout.addRow("Teléfono:", self.telefono_input)
        form_layout.addRow("Email*:", self.email_input)

        if self.is_edit:
            form_layout.addRow("Nueva Contraseña:", self.password_input)
            self.password_input.setPlaceholderText("Dejar vacío para no cambiar")
        else:
            form_layout.addRow("Contraseña*:", self.password_input)

        layout.addLayout(form_layout)

        # Botones
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def load_data(self):
        """Carga los datos del estilista en el formulario"""
        if self.estilista_data:
            self.nombre_input.setText(self.estilista_data.get('nombre', ''))
            self.apellidos_input.setText(self.estilista_data.get('apellidos', ''))
            self.telefono_input.setText(self.estilista_data.get('telefono', ''))
            self.email_input.setText(self.estilista_data.get('email', ''))

    def get_data(self):
        """Obtiene los datos del formulario"""
        data = {
            "nombre": self.nombre_input.text().strip(),
            "apellidos": self.apellidos_input.text().strip(),
            "telefono": self.telefono_input.text().strip(),
            "email": self.email_input.text().strip(),
        }

        # Solo agregar password si no está vacío
        password = self.password_input.text().strip()
        if password:
            data["password"] = password
        elif not self.is_edit:
            # Para crear, la contraseña es obligatoria
            data["password"] = ""

        return data
