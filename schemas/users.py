from models.users import User
from db_setup import Session

user1 = User(user_name = "Dev", password = "1234", role = "admin")
Session.add(user1)
Session.commit()

user2 = User(user_name = "Rahul", password = "2345", role = "sales")
Session.add(user2)
Session.commit()

user3 = User(user_name = "Mohit", password = "3456", role = "admin")
Session.add(user3)
Session.commit()

user4 = User(user_name = "Harshit", password = "4567", role = "admin")
Session.add(user4)
Session.commit()

user5 = User(user_name = "Sachin", password = "7647", role = "sales")
Session.add(user5)
Session.commit()

user6 = User(user_name = "Yash", password = "7242", role = "admin")
Session.add(user6)
Session.commit()

user7 = User(user_name = "Sumit", password = "8937", role = "admin")
Session.add(user7)
Session.commit()

user8 = User(user_name = "Kailash", password = "4657", role = "admin")
Session.add(user8)
Session.commit()

