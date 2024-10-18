from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base


class Productos(Base):
    __tablename__ = 'productos'
    id = Column(Integer, prymary_key=True)
    descripcion_cliente = Column(String(300), unique=True, nullable=False)
    codigo_cliente = Column(Float(10,8))
    valor_unitario = Column(String(3), nullable=False)
    cantida = Column(Float(10,8))
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    def __init__(self, descripcion, valor_unitario, unidad_medida, cantida_stock, categoria):
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantida_stock = cantida_stock
        self.categoria = categoria