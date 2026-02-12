from PySide6.QtWidgets import QApplication
from pathlib import Path

class ThemeHelper:
    def __init__(self):

        self.base_path = Path(__file__).parent.parent / "Styles"
        
        self.available_themes = {
            "light": "light.qss",
            "dark": "dark.qss",
            "warm": "warm.qss",
            "cold": "cold.qss"
        }
    
    def apply_theme(self, app: QApplication, theme_name: str):
        """Método principal para cambiar el tema"""
        if theme_name not in self.available_themes:
            print(f" Error: El tema '{theme_name}' no está definido en available_themes.")
            return

        file_name = self.available_themes[theme_name]
        style_path = self.base_path / file_name

        self._load_stylesheet(app, style_path)

    def _load_stylesheet(self, app: QApplication, path: Path):
        """Método interno para leer el archivo y aplicarlo"""
        if not path.exists():
            print(f" Error: No se encontró el archivo de estilo: {path}")
            return
            
        try:
            with open(path, "r", encoding="utf-8") as f:
                stylesheet = f.read()
                app.setStyleSheet(stylesheet)
                print(f" Tema aplicado: {path.name}")
        except Exception as e:
            print(f" Error al leer el archivo de estilos: {e}")