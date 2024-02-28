from sqlalchemy.orm import Session
from db_setup import engine, Base, Session
from models.users import User


Base.metadata.create_all(engine)

session = Session()

# user1 = User(user_name="Dev", password="123", role="admin")
# session.add(user1)
# session.commit()

# user2 = User(user_name="Rahul", password="234", role="admin")
# session.add(user2)
# session.commit()

# user3 = User(user_name="Harshit", password="145", role="sales")
# session.add(user3)
# session.commit()
