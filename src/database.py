from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from datetime import datetime

engine = create_engine("sqlite:///clima.db")
Base = declarative_base()

class RegistroClima(Base):
    __tablename__ = "registros"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ciudad = Column(String)
    temperatura = Column(Float)
    descripcion = Column(String)
    fecha = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)

def guardar_registro(ciudad: str, temperatura: float, descripcion: str)-> None:
    with Session(engine) as session:
        registro = RegistroClima(
            ciudad=ciudad,
            temperatura=temperatura,
            descripcion=descripcion
        )
        session.add(registro)
        session.commit()

def obtener_registros()-> list:
    with Session(engine) as session:
        return session.query(RegistroClima).all()

def obtener_por_ciudad(ciurad: str) -> list:
    with Session(engine) as session:
        return session.query(RegistroClima).filter(
            RegistroClima.ciudad == ciudad
        ).all()