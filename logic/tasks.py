from db_setup import get_db, Session
from models.tasks import Task
from schemas.tasks import TaskSchema

class TaskService:
    def __init__(self):
        self.db = get_db()

    def fetch_tasks(self):
        task_objects = self.db.query(Task).all()
        return task_objects
    
    def create_tasks(self, **kwargs):
        create_task_data = TaskSchema(**kwargs).to_dict()
        task_id = create_task_data.pop("id")
        task_due_date = create_task_data.pop("due_date")

        task_object = Task(**create_task_data)
        self.db.add(task_object)
        self.db.commit()
        return task_object
    
    def fetch_task(self, id):
        task_object = self.db.query(Task).filter(Task.id == id).first()
        return task_object
    
    def update_task(self,task_id, **kwargs):
        update_task_data = TaskSchema(**kwargs).to_dict()
        update_task_data.pop("id")
        update_task_data.pop("due_date")

        task_query = self.db.query(Task).filter(Task.id == task_id)
        task_object = task_query.first()
        task_query.update(update_task_data, synchronize_session=False)

        self.db.commit()
        self.db.refresh(task_object)
        return task_object
    
    def delete_task(self, task_id):
        task_object = self.db.query(Task).filter(Task.id == task_id).first()
        self.db.delete(task_object)
        self.db.commit()
        return f"{task_object} deleted successfully"

        