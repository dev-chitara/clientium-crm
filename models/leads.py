from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from db_setup import Base
from models.customers import Customer

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customer_id", ondelete="CASCADE"), nullable=False, index=True, unique=True)
    contact_info = Column(String(80), nullable=False)
    source = Column(String(80), nullable=False)
    status = Column(String(80), nullable=False)

    customer = Relationship("Customer", backref="lead")