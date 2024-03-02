import uuid
from sqlalchemy import Column, Integer, UUID, String, ForeignKey
from sqlalchemy.orm import Relationship
from db_setup import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = Column(String(80), nullable=False)
    contact_info = Column(String(80), nullable=False)
    status = Column(String(80), nullable=False)

    customer = Relationship("Customer", backref="customers", uselist=False)


    def __str__(self):
        return f"{self.name} {self.contact_info}"