# pedidos_backend_final/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine, Base
import crud
import models
import schemas

# Crea las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para gestionar la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "¡API de gestión de pedidos funcionando!"}

@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.create_client(db=db, client=client)
    return db_client

@app.get("/clients/", response_model=List[schemas.Client])
def get_all_clients(db: Session = Depends(get_db)):
    clients = db.query(models.Client).all()
    return clients

@app.get("/clients/{client_id}", response_model=schemas.Client)
def get_client_by_id(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# Endpoints para pedidos
@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = crud.create_order(db=db, order=order)
    return db_order

@app.get("/orders/", response_model=List[schemas.Order])
def get_all_orders(db: Session = Depends(get_db)):
    orders = crud.get_orders(db)
    return orders

@app.get("/orders/{order_id}", response_model=schemas.Order)
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_order(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
    
@app.get("/clients/{client_id}/orders", response_model=List[schemas.Order])
def get_orders_for_client(client_id: int, db: Session = Depends(get_db)):
    orders = crud.get_orders_by_client(db, client_id)
    if not orders:
        raise HTTPException(status_code=404, detail="Orders not found for this client")
    return orders