from sqlalchemy import Column, Integer, String
from db_setup import Base


class User(Base):
    __tablename__ =  "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(80), nullable=False)
    password = Column(String(80), unique=True,nullable=False)
    role = Column(String(80), nullable=False)