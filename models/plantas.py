from config.database import Base
from sqlalchemy import Column, Integer, String


class Plantas(Base):

    __tablename__ = 'plantas'

    id = Column(Integer, primary_key=True, index=True)
    nombre_cientifico = Column(String)
    descripcion = Column(String)
    cuidados = Column(String)
