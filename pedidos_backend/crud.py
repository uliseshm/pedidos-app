# pedidos_backend/crud.py

from sqlalchemy.orm import Session
import models
import schemas
from typing import List

def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def create_order(db: Session, order: schemas.OrderCreate):
    order_items_data = order.items
    
    db_order = models.Order(client_id=order.client_id)
    
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    for item_data in order_items_data:
        db_item = models.OrderItem(**item_data.model_dump(), order_id=db_order.id)
        db.add(db_item)
        
    db.commit()
    db.refresh(db_order)
    
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()
    
def get_orders(db: Session):
    return db.query(models.Order).all()
    
def get_orders_by_client(db: Session, client_id: int):
    return db.query(models.Order).filter(models.Order.client_id == client_id).all()