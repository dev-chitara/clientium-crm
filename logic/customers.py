from db_setup import get_db, Session
from models.customers import Customer
from schemas.customers import CustomerSchema

class CustomerService:

    def __init__(self):
        self.db = get_db()

    def fetch_customers(self):
        customer_object = self.db.query(Customer).all()
        return customer_object
    
    def create_customers(self, **kwargs):
        create_customer_data = CustomerSchema(**kwargs).to_dict()
        create_customer_data.pop("id")

        customer_object = Customer(**create_customer_data)
        self.db.add(customer_object)
        self.db.commit()
        return customer_object
    
    def fetch_customer(self, customer_id):
        customer_object = self.db.query(Customer).filter(Customer.id == customer_id).first()
        return customer_object
    
    def update_customer(self, customer_id, **kwargs):
        update_customer_data = CustomerSchema(**kwargs).to_dict()
        update_customer_data.pop("id")

        customer_query = self.db.query(Customer).filter(Customer.id == customer_id)
        customer_object = customer_query.first()
        customer_query.update(update_customer_data, synchronize_session=False)

        self.db.commit()
        self.db.refresh(customer_object)
        return customer_object
    
    def delete_customer(self, customer_id):
        customer_object = self.db.query(Customer).filter(Customer.id == customer_id).first()
        self.db.delete(customer_object)
        self.db.commit()
        return f"{customer_object} deleted successfully"

        
        