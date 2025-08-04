from fastapi import FastAPI
from database import engine, Base
import models

# Crea las tablas en la BD, solo para desarrollo
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Conexion exitosa con FasAPI"}