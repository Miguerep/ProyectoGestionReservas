from src.common import db, Cita, CitaServicio, Servicio, Peluqueria
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

class CitaService:
    @staticmethod
    def crear_cita(cliente_id, data):
        """Lógica de negocio pura para crear citas"""
        
        # 1. Validaciones
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

        # 2. Creación Transaccional
        try:
            nueva_cita = Cita(
                cliente_id=cliente_id,
                peluqueria_id=peluqueria.id, # Acceso pythonico
                servicio_id=servicio.id,
                fecha=fecha,
                estado="Solicitada"
            )
            db.session.add(nueva_cita)
            db.session.flush() # Para obtener el ID

            # Guardar precio congelado en tabla detalle
            detalle = CitaServicio(
                cita_id=nueva_cita.id,
                servicio_id=servicio.id,
                precio_aplicado=servicio.precio # Acceso pythonico
            )
            db.session.add(detalle)
            db.session.commit()
            
            return nueva_cita

        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error de base de datos: {str(e)}")

    @staticmethod
    def obtener_por_peluqueria(id_peluqueria):
        """Uso eficiente del ORM con relaciones"""
        # Ya no hacen falta joins manuales explícitos si configuramos 'joinedload' 
        # o dejamos que SQLAlchemy haga lazy loading (aunque eager es mejor para performance)
        citas = Cita.query.filter_by(peluqueria_id=id_peluqueria).all()
        
        resultado = []
        for c in citas:
            resultado.append({
                "id": c.id,
                "fecha": c.fecha.strftime("%Y-%m-%d %H:%M"), # Formateado aquí
                "cliente": c.cliente.nombre if c.cliente else "Desconocido",
                "servicio": c.servicio.nombre if c.servicio else "N/A",
                "estilista": c.estilista.nombre if c.estilista else "Por asignar",
                "estado": c.estado,
                "precio_congelado": c.precio_final # Usando la @property
            })
        return resultado