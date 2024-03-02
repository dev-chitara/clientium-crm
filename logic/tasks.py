from db_setup import get_db, Session
from models.tasks import Task
from schemas.tasks import TaskSchema
from models.users import User


class TaskService:

    def __init__(self):
        self.db = get_db()


    def fetch_tasks(self):
        task_objects = self.db.query(Task).all()
        return task_objects
    

    def create_tasks(self, **kwargs):
        create_task_data = TaskSchema(**kwargs).to_absolute_dict()

        task_object = Task(**create_task_data)
        self.db.add(task_object)
        self.db.commit()
        return task_object

    
    def fetch_task_associated_user(self, task_id):
        task_object = self.db.query(Task).get(task_id)
        task_users= task_object.users
        return task_users
    

    def update_task(self, id, **kwargs):
        update_task = TaskSchema(**kwargs)
        update_task_data = update_task.to_absolute_dict()     

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
