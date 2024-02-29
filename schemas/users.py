
class UserSchema:

    def __init__(self, id, name, mobile, role):
        self.id = id
        self.name = name
        self.mobile = mobile
        self.role = role


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "mobile": self.mobile,
            "role": self.role
        }
