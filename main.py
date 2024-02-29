from sqlalchemy.orm import Session
from db_setup import engine, Base, Session
from models.users import User
from logic.users import UserService


Base.metadata.create_all(engine)

user_service = UserService()
# for user in user_service.fetch_users():
#     print("user: name", user.name)
# print(user_service.create_users(id=1, name="Dev",mobile="12345678",role="admin"))

# print(user_service.create_users(id=2, name="Rahul", mobile="132828782", role="admin"))

# print(user_service.create_users(id=3, name="Harshit", mobile="8964198691", role="sales"))
    
# print(user_service.create_users(id=4, name="Mohit", mobile="785127192", role="admin"))

# print(user_service.fetch_user("<function uuid4 at 0x7f16c87a8b80>"))

# print(user_service.update_user(user_id="<function uuid4 at 0x7f56cff78c10>", id=4, name="Mohit", mobile="785127192", role="sales"))


# print(user_service.delete_user("<function uuid4 at 0x7f874d0a8b80>"))

