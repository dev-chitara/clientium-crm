
class LeadSchema:

    def __init__(self, name, contact_info, status, id=None):
        self.id = id
        self.name = name
        self.contact_info = contact_info
        self.status = status


    def to_dict(self):
        return {
            "id": self.id,      
            "name": self.name,    
            "contact_info": self.contact_info,
            "status": self.status
        }
    

    def to_absolute_dict(self):
        fields = self.to_dict()
        return {key: fields[key] for key in fields if fields.get(key)}