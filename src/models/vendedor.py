from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from src.models import session, Base


class vendedor(Base):
    __tablename__ = 'vendedor'
    id = Column(Integer, prymary_key=True)
    nombre_completo = Column(String(300), unique=True, nullable=False)
    email = Column(String(400))
    telefono = Column(Float(10), nullable=False)
    direccion = Column(String(100))
    fecha_ingreso = Column(DateTime, nullable=False)

    def __init__(self, nombre_completo, email, telefono, direccion, fecha_ingreso):
        self.nombre_completo = nombre_completo
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_ingreso = fecha_ingreso

        #continuacion 