from db_setup import engine, Base
from models import users, leads, customers, tasks

Base.metadata.create_all(engine)
