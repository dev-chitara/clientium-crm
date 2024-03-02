from db_setup import get_db, Session
from models.tasks import Task
from schemas.tasks import TaskSchema


class TaskService:

    def __init__(self):
        self.db = get_db()


    def fetch_tasks(self):
        task_objects = self.db.query(Task).all()
        return task_objects
# id, description, due_date, status, user_id, lead_id, customer_id

    def create_tasks(self, lead_id, user_id, **kwargs):
        new_task_data = TaskSchema(id="", lead_id=lead_id, user_id=user_id, **kwargs).to_dict()
        new_task_data.pop("id")
        new_task_data.pop("user_id")
        new_task_data.pop("lead_id")

        new_task = Task(**new_task_data)
        self.db.add(new_task)
        self.db.commit()
        return new_task

    
    def fetch_task(self, user_id):
        assigned_tasks = self.db.query(Task).filter_by(user_id=user_id).all()

        tasks = [f"Description: {task.description}, Due Date: {task.due_date}, Status: {task.status}" for task in assigned_tasks]
        return tasks

    def update_task(self, id, **kwargs):
        update_task_data = TaskSchema(**kwargs).to_dict()
        update_task_data.pop("id")
        update_task_data.pop("due_date")

        task_query = self.db.query(Task).filter(Task.id == id)
        task_object = task_query.first()
        task_query.update(update_task_data, synchronize_session=False)

        self.db.commit()
        self.db.refresh(task_object)
        return task_object


    def delete_task(self, id):
        task_object = self.db.query(Task).filter(Task.id == id).first()
        self.db.delete(task_object)
        self.db.commit()
        return task_object
