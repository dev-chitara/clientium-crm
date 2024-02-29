import uuid
from sqlalchemy import UUID, Column, Integer, String
from sqlalchemy.orm import Relationship
from db_setup import Base
from models.tasks import Task


class User(Base):
    __tablename__ =  "users"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4))
    name = Column(String(80), nullable=False)
    mobile = Column(String(80), unique=True, nullable=False)
    role = Column(String(80), nullable=False)

    tasks = Relationship("Task", backref="tasks", passive_deletes=True)

    def __repr__(self):
        return f"{self.name} {self.role}"
