# pedidos_backend/schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional, List

class ClientBase(BaseModel):
    name: str
    phone_number: str
    address: str
    points: Optional[int] = 0
    municipality: str
    route: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        from_attributes = True

class OrderItemBase(BaseModel):
    name: str
    price: float
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    order_id: int

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    client_id: int

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class Order(OrderBase):
    id: int
    items: List[OrderItem] = []

    class Config:
        from_attributes = True