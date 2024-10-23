from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
from src.models.categorias import Categorias

class Productos(Base):
    __tablename__ = 'productos'
    id = Column(Integer, prymary_key=True)
    descripcion = Column(String(300), unique=True, nullable=False)
    valor_unitario = Column(Float(10,8))
    unidad_medida = Column(String(3), nullable=False)
    cantidad_stock = Column(Float(10,8))
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    def __init__(self, descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria):
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantida_stock = cantidad_stock
        self.categoria = categoria

    def obtener_productos():
        productos = session.query(productos).join(Categorias).all()
        return productos     
    
    def crear_producto():
        Producto = session.add(Producto)
        session.commit()
        return Producto