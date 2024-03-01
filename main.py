from sqlalchemy.orm import Session
from db_setup import engine, Base, Session,get_db
from models.users import User
from models.tasks import Task
from models.customers import Customer
from logic.users import UserService
from logic.tasks import TaskService
from logic.customers import CustomerService

Base.metadata.create_all(engine)

# user_service = UserService()

# print(user_service.create_users(id=1, name="Dev",mobile="12345678",role="admin"))

# print(user_service.create_users(id=2, name="Rahul", mobile="132828782", role="admin"))

# print(user_service.create_users(id=3, name="Harshit", mobile="8964198691", role="sales"))
    
# print(user_service.create_users(id=4, name="Mohit", mobile="785127192", role="admin"))

# for user in user_service.fetch_users():
#     print("user: name", user.name)

# print(user_service.fetch_user("<function uuid4 at 0x7f16c87a8b80>"))

# print(user_service.update_user(user_id="<function uuid4 at 0x7f56cff78c10>", id=4, name="Mohit", mobile="785127192", role="sales"))


# print(user_service.delete_user("<function uuid4 at 0x7f874d0a8b80>")


# task_service = TaskService()

# print(task_service.create_tasks(id=1, user_id="<function uuid4 at 0x7f16c87a8b80>", description="checking leads status", due_date="", status="pending"))

# print(task_service.create_tasks(id=2, user_id="<function uuid4 at 0x7f4bccca4c10>", description="managing new leads", due_date="", status="pending"))

# print(task_service.create_tasks(id=3, user_id="<function uuid4 at 0x7f0646aa4c10>", description="checking sales", due_date="", status="completed"))

# for task in task_service.fetch_tasks():
#     print(task)

# print(task_service.fetch_task("<function uuid4 at 0x7f17f5ea4b80>"))

# print(task_service.update_task(task_id="<function uuid4 at 0x7f17f5ea4b80>",id=4 ,user_id="<function uuid4 at 0x7f4bccca4c10>", description="managing new leads", due_date="", status="completed"))

# print(task_service.delete_task("<function uuid4 at 0x7f0a00ea0b80>"))

