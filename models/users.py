import uuid
from sqlalchemy import UUID, Column, String
from db_setup import Base


class User(Base):
    __tablename__ =  "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = Column(String(80), nullable=False)
    mobile = Column(String(80), unique=True, nullable=False)
    role = Column(String(80), nullable=False)

    def __str__(self):
        return f"{self.name} {self.role}"
