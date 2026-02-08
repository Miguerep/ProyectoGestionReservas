from src.common import db, Servicio

class ServicioService:
    @staticmethod
    def crear_servicio(data):
        """Crea un nuevo servicio"""
        nombre = data.get("nombre")
        precio = data.get("precio")
        duracion = data.get("duracion")

        if not all([nombre, precio, duracion]):
            raise ValueError("Faltan datos obligatorios: nombre, precio y duracion son requeridos")

        # Validación de tipos y valores
        try:
            precio = float(precio)
            duracion = int(duracion)
        except (ValueError, TypeError):
            raise ValueError("Precio debe ser un número y duración debe ser un entero")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0 minutos")

        # Verificar si ya existe un servicio con el mismo nombre
        if Servicio.query.filter_by(nombre=nombre).first():
            raise ValueError("Ya existe un servicio con ese nombre")

        nuevo_servicio = Servicio(
            nombre=nombre,
            precio=precio,
            duracion=duracion
        )

        db.session.add(nuevo_servicio)
        db.session.commit()
        return nuevo_servicio

    @staticmethod
    def obtener_todos():
        """Obtiene todos los servicios"""
        return Servicio.query.all()

    @staticmethod
    def obtener_por_id(id_servicio):
        """Obtiene un servicio por su ID"""
        servicio = Servicio.query.get(id_servicio)
        if not servicio:
            raise ValueError("Servicio no encontrado")
        return servicio

    @staticmethod
    def actualizar_servicio(id_servicio, data):
        """Actualiza un servicio existente"""
        servicio = Servicio.query.get(id_servicio)
        if not servicio:
            raise ValueError("Servicio no encontrado")

        # Actualizar campos si están presentes en data
        if "nombre" in data:
            nombre = data.get("nombre")
            if not nombre:
                raise ValueError("El nombre no puede estar vacío")

            # Verificar si el nuevo nombre ya existe en otro servicio
            servicio_existente = Servicio.query.filter_by(nombre=nombre).first()
            if servicio_existente and servicio_existente.id != id_servicio:
                raise ValueError("Ya existe otro servicio con ese nombre")

            servicio.nombre = nombre

        if "precio" in data:
            try:
                precio = float(data.get("precio"))
                if precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
                servicio.precio = precio
            except (ValueError, TypeError):
                raise ValueError("El precio debe ser un número válido")

        if "duracion" in data:
            try:
                duracion = int(data.get("duracion"))
                if duracion <= 0:
                    raise ValueError("La duración debe ser mayor a 0 minutos")
                servicio.duracion = duracion
            except (ValueError, TypeError):
                raise ValueError("La duración debe ser un número entero válido")

        db.session.commit()
        return servicio

    @staticmethod
    def eliminar_servicio(id_servicio):
        """Elimina un servicio"""
        servicio = Servicio.query.get(id_servicio)
        if not servicio:
            raise ValueError("Servicio no encontrado")

        # Verificar si el servicio está asociado a alguna peluquería
        if servicio.peluquerias:
            raise ValueError("No se puede eliminar el servicio porque está asociado a una o más peluquerías")

        db.session.delete(servicio)
        db.session.commit()
        return True
