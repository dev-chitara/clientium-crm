import uuid
from sqlalchemy import Column, Integer, UUID, String, ForeignKey, DateTime
from sqlalchemy.orm import Relationship
from db_setup import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    description = Column(String(80), nullable=False)
    due_date = Column(DateTime)
    status = Column(String(80), nullable=False)
    user_id = Column(UUID, ForeignKey("users.id", ondelete="CASCADE"))
    lead_id = Column(UUID, ForeignKey("leads.id",ondelete="CASCADE"))

    lead = Relationship("Lead", backref="tasks")


    def __repr__(self):
        return f"{self.description} {self.due_date} {self.status}"
