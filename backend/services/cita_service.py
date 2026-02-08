from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from src.common import db, Cita, CitaServicio, Servicio, Peluqueria

class CitaService:
    # Definición del flujo de estados permitidos
    ESTADOS_VALIDOS = ["Pendiente", "Confirmada", "Completada", "Cancelada"]
    TRANSICIONES_PERMITIDAS = {
        "Pendiente": ["Confirmada", "Cancelada"],
        "Confirmada": ["Completada", "Cancelada"],
        "Completada": [],  # Estado final, no permite cambios
        "Cancelada": []    # Estado final, no permite cambios
    }

    @staticmethod
    def crear_cita(cliente_id, data):
        # 1. Validaciones de Negocio
        servicio = Servicio.query.get(data.get("id_servicio"))
        if not servicio:
            raise ValueError("El servicio especificado no existe.")
            
        peluqueria = Peluqueria.query.get(data.get("id_peluqueria"))
        if not peluqueria:
            raise ValueError("La peluquería especificada no existe.")
            
        try:
            fecha = datetime.strptime(data.get("fecha"), "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD HH:MM")

        # 2. Transacción Atómica
        try:
            # Creamos la cabecera de la cita
            nueva_cita = Cita(
                cliente_id=cliente_id,
                peluqueria_id=peluqueria.id,
                servicio_id=servicio.id,
                fecha=fecha,
                estado="Pendiente"
            )
            db.session.add(nueva_cita)
            db.session.flush() # Genera el ID sin commitear aún

            # Guardamos el precio histórico (Snapshot)
            detalle = CitaServicio(
                cita_id=nueva_cita.id,
                servicio_id=servicio.id,
                precio_aplicado=servicio.precio
            )
            db.session.add(detalle)
            
            db.session.commit() # Confirmamos todo el bloque
            return nueva_cita

        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error de base de datos: {str(e)}")

    @staticmethod
    def obtener_por_peluqueria(id_peluqueria):
        # Usamos la potencia de las relaciones definidas en los modelos
        citas = Cita.query.filter_by(peluqueria_id=id_peluqueria).all()
        
        resultado = []
        for c in citas:
            resultado.append({
                "id": c.id,
                "fecha": c.fecha.strftime("%Y-%m-%d %H:%M"),
                "cliente": c.cliente.nombre if c.cliente else "Desconocido",
                "servicio": c.servicio.nombre if c.servicio else "N/A",
                "estilista": c.estilista.nombre if c.estilista else "Por asignar",
                "estado": c.estado,
                "precio_congelado": c.detalle_servicio.precio_aplicado if c.detalle_servicio else 0.0
            })
        return resultado

    @staticmethod
    def actualizar_estado(id_cita, nuevo_estado):
        """
        Actualiza el estado de una cita validando las transiciones permitidas.

        Flujo de estados:
        - Pendiente → Confirmada → Completada
        - Cualquier estado → Cancelada (excepto Completada)
        """
        # Validar que el nuevo estado es válido
        if nuevo_estado not in CitaService.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(CitaService.ESTADOS_VALIDOS)}")

        # Buscar la cita
        cita = Cita.query.get(id_cita)
        if not cita:
            raise ValueError("La cita no existe")

        estado_actual = cita.estado

        # Validar transición permitida
        if nuevo_estado not in CitaService.TRANSICIONES_PERMITIDAS.get(estado_actual, []):
            raise ValueError(
                f"No se puede cambiar de '{estado_actual}' a '{nuevo_estado}'. "
                f"Transiciones permitidas: {', '.join(CitaService.TRANSICIONES_PERMITIDAS.get(estado_actual, []))}"
            )

        # Actualizar estado
        try:
            cita.estado = nuevo_estado
            db.session.commit()
            return cita
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error al actualizar el estado: {str(e)}")