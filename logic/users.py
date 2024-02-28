from main import session
from models.users import User

class AllUsers(User):
    
    def all_users():
        return session.query(User).all()


s = AllUsers().all_users()
for i in s:
    print(i)