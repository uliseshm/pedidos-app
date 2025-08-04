from sqlalchemy import Column, Integer, String, Float
from database import Base

class Client(Base):
    __tablename__ = "Clientes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, index=True)
    address = Column(String)
    points = Column(Integer, default=0)
    municipality = Column(String, index=True)
    route = Column(String, index=True)

    latitude = Column(Float)
    longitude = Column(Float)