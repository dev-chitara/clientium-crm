import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship
from db_setup import Base
from models.leads import Lead

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, default=str(uuid.uuid4))
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    phone_no = Column(Integer, nullable=False)

    lead = Relationship("Lead",  backref="leads")

    def __repr__(self):
        return f"{self.name} {self.email}"
    