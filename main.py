from db_setup import engine, Base
from models.users import User


Base.metadata.create_all(engine)