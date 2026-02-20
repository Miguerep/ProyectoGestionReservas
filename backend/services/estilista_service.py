from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash
from src.common import db, Estilista

class EstilistaService:

    @staticmethod
    def crear_estilista(id_peluqueria, data):
        """
        Crea un nuevo estilista asociado a una peluquería

        Args:
            id_peluqueria: ID de la peluquería
            data: Diccionario con nombre, apellidos, telefono, email, password

        Returns:
            Estilista: El estilista creado

        Raises:
            ValueError: Si faltan datos requeridos o el email ya existe
            Exception: Si hay error de base de datos
        """
        # Validaciones
        required_fields = ["nombre", "email", "password"]
        for field in required_fields:
            if not data.get(field):
                raise ValueError(f"El campo '{field}' es requerido")

        # Verificar que el email no exista
        if Estilista.query.filter_by(email=data["email"]).first():
            raise ValueError("El email ya está registrado")

        try:
            nuevo_estilista = Estilista(
                nombre=data["nombre"],
                apellidos=data.get("apellidos", ""),
                telefono=data.get("telefono", ""),
                email=data["email"],
                password_hash=generate_password_hash(data["password"]),
                id_peluqueria=id_peluqueria,
                activo=True
            )

            db.session.add(nuevo_estilista)
            db.session.commit()
            return nuevo_estilista

        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error de base de datos: {str(e)}")

    @staticmethod
    def obtener_por_peluqueria(id_peluqueria, incluir_inactivos=False):
        """
        Obtiene todos los estilistas de una peluquería

        Args:
            id_peluqueria: ID de la peluquería
            incluir_inactivos: Si True, incluye estilistas inactivos

        Returns:
            list: Lista de estilistas formateados como diccionarios
        """
        query = Estilista.query.filter_by(id_peluqueria=id_peluqueria)

        if not incluir_inactivos:
            query = query.filter_by(activo=True)

        estilistas = query.all()

        resultado = []
        for e in estilistas:
            resultado.append({
                "id": e.id,
                "nombre": e.nombre,
                "apellidos": e.apellidos,
                "telefono": e.telefono,
                "email": e.email,
                "activo": e.activo
            })

        return resultado

    @staticmethod
    def obtener_por_id(id_estilista):
        """
        Obtiene un estilista por su ID

        Args:
            id_estilista: ID del estilista

        Returns:
            Estilista: El estilista encontrado o None
        """
        return Estilista.query.get(id_estilista)

    @staticmethod
    def actualizar_estilista(id_estilista, data):
        """
        Actualiza los datos de un estilista

        Args:
            id_estilista: ID del estilista
            data: Diccionario con los campos a actualizar

        Returns:
            Estilista: El estilista actualizado

        Raises:
            ValueError: Si el estilista no existe o el email ya está en uso
            Exception: Si hay error de base de datos
        """
        estilista = Estilista.query.get(id_estilista)
        if not estilista:
            raise ValueError("El estilista no existe")

        try:
            # Actualizar campos permitidos
            if "nombre" in data:
                estilista.nombre = data["nombre"]
            if "apellidos" in data:
                estilista.apellidos = data["apellidos"]
            if "telefono" in data:
                estilista.telefono = data["telefono"]
            if "email" in data and data["email"] != estilista.email:
                # Verificar que el nuevo email no exista
                if Estilista.query.filter_by(email=data["email"]).first():
                    raise ValueError("El email ya está registrado")
                estilista.email = data["email"]
            if "password" in data and data["password"]:
                estilista.password_hash = generate_password_hash(data["password"])
            if "activo" in data:
                estilista.activo = data["activo"]

            db.session.commit()
            return estilista

        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error de base de datos: {str(e)}")

    @staticmethod
    def desactivar_estilista(id_estilista):
        """
        Desactiva un estilista (borrado lógico)

        Args:
            id_estilista: ID del estilista

        Returns:
            Estilista: El estilista desactivado

        Raises:
            ValueError: Si el estilista no existe
            Exception: Si hay error de base de datos
        """
        estilista = Estilista.query.get(id_estilista)
        if not estilista:
            raise ValueError("El estilista no existe")

        try:
            estilista.activo = False
            db.session.commit()
            return estilista

        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error de base de datos: {str(e)}")
