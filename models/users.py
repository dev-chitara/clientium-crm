from sqlalchemy import Column, Integer, String
from db_setup import Base


class User(Base):
    __tablename__ =  "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(80), nullable=False)
    password = Column(String(80), unique=True,nullable=False)
    role = Column(String(80), nullable=False)    

    def __init__(self, user_id, user_name, password, role):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.role = role

    def __repr__(self):
        return f"{self.user_name} {self.role}"
