from logic.users import UserService
from logic.tasks import TaskService
from logic.customers import CustomerService
from logic.leads import LeadService


data = [
    {
        "user": {
            "name": "Dev",
            "mobile": "784916818100",
            "role": "admin"
        },
        "task": {
            "description": "Task 1 for User",
            "due_date": "2024-03-15",
            "status": "pending"
        },
        "name": "John Doe",
        "lead": {
            "contact_info": "9988776655",
            "status": "new"
        },
        "customer": {
            "email": "john@mail.com",
            "phone": "9988776655"
        }       
    },
    { 
        "user": {
            "name": "Harshit",
            "mobile": "672584961869",
            "role": "sales"
        },
        "task": {
            "description": "Task 2 for User",
            "due_date": "2023-02-23",
            "status": "completed"
        },
        "name": "John Doe",
        "lead": {
            "contact_info": "8877665544",
            "status": "new"
        },
        "customer": {
            "email": "jane@mail.com",
            "phone": "8877665544"
        }
    }
]

user_service = UserService()
task_service = TaskService()
lead_service = LeadService()
customer_service = CustomerService()

for record in data:
    created_user = user_service.create_users(**record["user"])
    print(f"User name: {created_user.name}")
    print(f"User role: {created_user.role}")

    created_lead = lead_service.create_leads(
        name=record["name"], 
        **record["lead"]
    )
    print(f"Lead name: {created_lead.name}")
    print(f"Lead status: {created_lead.status}")

    created_customer = customer_service.create_customers(
        lead_id=created_lead.id, 
        name=created_lead.name, 
        **record["customer"]
    )
    print(f"Customer name: {created_customer.name}")
    print(f"Customer status: {created_customer.phone}")

    created_task = task_service.create_tasks(
        user_id=created_user.id,
        lead_id=created_lead.id,
        **record["task"]
    )
    print(f"Task name: {created_customer.name}")
    print(f"Customer status: {created_customer.phone}")