from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from db_setup import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False, index=True, unique=True)
    contact_info = Column(String(80), nullable=False)
    source = Column(String(80), nullable=False)
    status = Column(String(80), nullable=False)

    customer = Relationship("Customer", backref="customers")

    def __repr__(self):
        return f"{self.source} {self.status}"