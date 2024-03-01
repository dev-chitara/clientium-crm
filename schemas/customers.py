
class CustomerSchema:

    def __init__(self, id, name, email, phone_no):
        self.id = id
        self.name = name
        self.email = email
        self.phone_no = phone_no

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone_no": self.phone_no
        }