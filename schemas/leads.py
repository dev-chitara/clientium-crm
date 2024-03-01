
class LeadSchema:
    def __init__(self, id, customer_id, contact_info, source, status):
        self.id = id
        self.customer_id = customer_id
        self.contact_info = contact_info
        self.source = source
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "contact_info": self.contact_info,
            "source": self.source,
            "status": self.status
        }        
