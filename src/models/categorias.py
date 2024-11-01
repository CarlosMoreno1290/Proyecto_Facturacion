from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Categorias(Base):
    __tablename__ = "Categorias"    
    id = Column(Integer, primary_key=True)
    categoria = Column(String(300), unique=True, nullable=False)

    def __init__(self, Categoria):
        self.categoria = Categoria

    def obtener_categorias():
        Categorias = session.query(Categorias).all()
        return Categorias 
    