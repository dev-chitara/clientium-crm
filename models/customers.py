from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship
from db_setup import Base
from models.leads import Lead

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(80), nullable=False)
    email = Column(String(80), uniqe=True, nullable=False)
    phone_no = Column(Integer, unique=True, nullable=False)

    lead = Relationship("Lead", back_populates="customer")

