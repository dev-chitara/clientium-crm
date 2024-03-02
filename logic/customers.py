from db_setup import get_db, Session
from models.customers import Customer
from schemas.customers import CustomerSchema
from models.leads import Lead

class CustomerService:

    def __init__(self):
        self.db = get_db()

    
    def fetch_customers(self):
        customer_object = self.db.query(Customer).all()
        return customer_object
    

    def create_customers(self, **kwargs):
        create_customer = CustomerSchema(**kwargs)
        create_customer_data = create_customer.to_absolute_dict()

        customer_object = Customer(**create_customer_data)

        lead_object = self.db.query(Lead).filter(Lead.id == customer_object.lead_id).first()
    
        lead_object.status = "qualified"
        lead_object.customer = customer_object

        self.db.add(customer_object)
        self.db.commit()
        return customer_object
    
    
    def fetch_customer(self, id):
        customer_object = self.db.query(Customer.id == id).first()
        return customer_object
    
    
    def fetch_customer_associated_tasks(self, customer_id):
        customer_object = self.db.query(Customer).get(customer_id)
        customer_tasks = customer_object.tasks
        return customer_tasks
         
    
    def update_customer(self, id, **kwargs):
        update_customer = CustomerSchema(**kwargs)
        update_customer_data = update_customer.to_absolute_dict()

        customer_query = self.db.query(Customer).filter(Customer.id == id)
        customer_object = customer_query.first()
        customer_query.update(update_customer_data, synchronize_session=False)

        self.db.commit()
        self.db.refresh(customer_object)
        return customer_object
    
    
    def delete_customer(self, id):
        customer_object = self.db.query(Customer).filter(Customer.id == id).first()
        self.db.delete(customer_object)
        self.db.commit()
        return True