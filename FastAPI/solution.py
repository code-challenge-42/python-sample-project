from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from copy import deepcopy

# Configuración de la base de datos
DATABASE_URL = "sqlite:///./libros.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo en la base de datos
class LibroDB(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor = Column(String)

Base.metadata.create_all(bind=engine)

# Pydantic para validación
class Libro(BaseModel):
    titulo: str
    autor: str

app = FastAPI()

@app.post("/libro/")
def crear_libro(libro: Libro):
    try:
        db = SessionLocal()
        nuevo_libro = LibroDB(titulo=libro.titulo, autor=libro.autor)
        db.add(nuevo_libro)
        db.commit()
        db.refresh(nuevo_libro)
        return {"mensaje": "Libro creado", "id": nuevo_libro.id}
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.get("/libro/{libro_id}")
def obtener_libro(libro_id: int):
    try:
        db = SessionLocal()
        libro = db.query(LibroDB).filter(LibroDB.id == libro_id).first()
        if not libro:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        libro_dict = deepcopy({"titulo": libro.titulo, "autor": libro.autor})
        return libro_dict
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
