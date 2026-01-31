from src.common import db, Peluqueria

class PeluqueriaService:
    @staticmethod
    def crear_peluqueria(data):
        nombre = data.get("nombre")
        direccion = data.get("direccion")
        telefono = data.get("telefono")
        
        if not all([nombre, direccion, telefono]):
            raise ValueError("Faltan datos obligatorios")
            
        if Peluqueria.query.filter_by(telefono=telefono).first():
            raise ValueError("Ya existe una peluquería con ese teléfono")
            
        nueva = Peluqueria(nombre=nombre, direccion=direccion, telefono=telefono)
        db.session.add(nueva)
        db.session.commit()
        return nueva