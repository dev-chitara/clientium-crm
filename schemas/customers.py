
class CustomerSchema:

    def __init__(self, name, email, phone, lead_id, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.lead_id = lead_id


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "lead_id": self.lead_id
        }
    

    def to_absolute_dict(self):
        fields = self.to_dict()
        return {key: fields[key] for key in fields if fields.get(key)}