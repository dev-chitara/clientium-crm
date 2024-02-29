import uuid
from datetime import datetime
from sqlalchemy import Column, UUID, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Relationship
# from models.users import User
from db_setup import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4))
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
    description = Column(String(80), nullable=False)
    due_date = Column(DateTime, default=datetime.utcnow())
    status = Column(String(80), nullable=False)

    users = Relationship("User", backref="users")

    def __repr__(self):
        return f"{self.description} {self.due_date} {self.status}"
