
class UserSchema:

    def __init__(self,name, mobile, role, id=None):
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


    def to_absolute_dict(self):
        fields = self.to_dict()
        return {key: fields[key] for key in fields if fields.get(key)}