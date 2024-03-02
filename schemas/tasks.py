
class TaskSchema:
    
    def __init__(self, id, user_id, lead_id,description, due_date, status, customer_id):
        self.id = id
        self.user_id = user_id
        self.lead_id = lead_id
        self.description = description
        self.due_date = due_date
        self.status = status
        self.customer_id = customer_id
    
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
            "user_id": self.user_id,
            "lead_id": self.lead_id,
            "customer_id": self.customer_id
        }