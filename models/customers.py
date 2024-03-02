import uuid
from sqlalchemy import Column, Integer, UUID, String, ForeignKey
from sqlalchemy.orm import Relationship
from db_setup import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    phone = Column(Integer, nullable=False)
    lead_id = Column(UUID, ForeignKey("leads.id", ondelete="CASCADE"))


    def __str__(self):
        return f"{self.name} {self.email}"
    