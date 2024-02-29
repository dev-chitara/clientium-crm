
class TaskSchema:
    
    def __init__(self, id, user_id, description, due_date, status):
        self.id = id
        self.user_id = user_id
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }
        







# id = Column(String(36), primary_key=True, default=str(uuid.uuid4))
# user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
# description = Column(String(80), nullable=False)
# due_date = Column(DateTime, default=datetime.utcnow())
# status = Column(String(80), nullable=False)