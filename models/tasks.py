from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db_setup import Base
from models.users import User
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user_id", on_delete="CASCADE"), nullable=False, uniqe=True)
    description = Column(String(80), nullable=False)
    due_date = Column(DateTime, default=datetime.utcnow())
    status = Column(String(80), nullable=False)





# - TaskID (Primary Key)
# - UserID (Foreign Key)
# - Description
# - DueDate
# - Status