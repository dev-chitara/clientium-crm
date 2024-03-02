
class TaskSchema:
    
    def __init__(self, description, due_date, status, user_id, lead_id, id=None):
        self.id = id
        self.description = description
        self.due_date = due_date
        self.status = status
        self.user_id = user_id
        self.lead_id = lead_id
    

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
            "user_id": self.user_id,
            "lead_id": self.lead_id
        }
    

    def to_absolute_dict(self):
        fields = self.to_dict()
        return {key: fields[key] for key in fields if fields.get(key)}