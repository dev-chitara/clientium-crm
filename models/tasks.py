import uuid
from sqlalchemy import Column, UUID, String, ForeignKey, Date
from sqlalchemy.orm import Relationship
from db_setup import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    description = Column(String(80), nullable=False)
    due_date = Column(Date)
    status = Column(String(80), nullable=False)
    user_id = Column(UUID, ForeignKey("users.id", ondelete="CASCADE"))
    lead_id = Column(UUID, ForeignKey("leads.id",ondelete="CASCADE"))

    user = Relationship("User", backref="users")
    lead = Relationship("Lead", backref="leads")

    def __str__(self):
        return f"{self.description} {self.due_date} {self.status}"
