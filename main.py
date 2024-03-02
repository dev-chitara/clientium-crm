from logic.users import UserService
from logic.tasks import TaskService
from logic.customers import CustomerService
from logic.leads import LeadService


data = [
    {
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

        "name": "Jane Doe",
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



lead_service = LeadService()
customer_service = CustomerService()

for record in data:
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

