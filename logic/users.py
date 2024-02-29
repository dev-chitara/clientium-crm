from db_setup import get_db, Session
from models.users import User
from schemas.users import UserSchema


class UserService:

    def __init__(self):
        self.db = get_db()


    def fetch_users(self):
        user_objects = self.db.query(User).all()
        return user_objects


    def create_users(self, **kwargs):
        create_user_data = UserSchema(**kwargs).to_dict()
        user_id = create_user_data.pop("id")

        user_object = User(**create_user_data)
        self.db.add(user_object)
        self.db.commit()
        return user_object


    def fetch_user(self, id):
        user_object = self.db.query(User).filter(User.id == id).first()
        return user_object


    def update_user(self,user_id, **kwargs):
        update_user_data = UserSchema(**kwargs).to_dict()
        update_user_data.pop("id")

        user_query = self.db.query(User).filter(User.id == user_id)
        user_object = user_query.first()
        user_query.update(update_user_data, synchronize_session=False)

        self.db.commit()
        self.db.refresh(user_object)
        return user_object


    def delete_user(self, id):
        user_object =self.db.query(User).filter(User.id == id).first()
        self.db.delete(user_object)
        self.db.commit()
        return f"{user_object} deleted succesfully"