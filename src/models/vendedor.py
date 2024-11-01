from sqlalchemy import Column, Integer, String, Float, DateTime
from src.models import Session, Base


class Vendedor(Base):
    __tablename__ = 'Vendedor'
    id = Column(Integer, primary_key=True)
    nombre_completo = Column(String(300), nullable=False)
    email = Column(String(400))
    telefono = Column(Float(10), nullable=False)
    direccion = Column(String(100))
    fecha_ingreso = Column(DateTime, nullable=False)
    contraseña = Column(String(30), nullable=False)
    rol = Column(String(20), nullable=False)

    def __init__(self, nombre_completo, email, telefono, direccion, fecha_ingreso, contraseña, rol):
        self.nombre_completo = nombre_completo
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_ingreso = fecha_ingreso
        self.fecha_ingreso = contraseña
        self.fecha_ingreso = rol

    def obtener_vendedor():
        vendedor = session.query(Vendedor).all()
        return vendedor