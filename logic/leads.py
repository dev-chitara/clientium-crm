from db_setup import get_db, Session
from models.leads import Lead
from schemas.leads import LeadSchema


class LeadService:

    def __init__(self):
        self.db = get_db()


    def fetch_leads(self):
        lead_object = self.db.query(Lead).all()
        return lead_object
    

    def create_leads(self, **kwargs):
        create_lead_data = LeadSchema(**kwargs).to_absolute_dict()
        lead_object = Lead(**create_lead_data)
    
        self.db.add(lead_object)
        self.db.commit()
        return lead_object
    

    def fetch_lead(self, lead_id):
        lead_object = self.db.query(Lead).filter(Lead.id == lead_id).first()
        return lead_object
    

    def update_lead(self, lead_id, **kwargs):
        update_lead_data = LeadSchema(**kwargs).to_dict()
        update_lead_data.pop("id")

        lead_query = self.db.query(Lead).filter(Lead.id == lead_id)
        lead_object = lead_query.first()
        lead_query.update(update_lead_data, synchronize_session=False)

        self.db.commit()
        self.db.refresh(lead_object)
        return lead_object
    

    def delete_lead(self, lead_id):
        lead_object = self.db.query(Lead).filter(Lead.id == lead_id).first()
        self.db.delete(lead_object)
        self.db.commit()
        return f"{lead_object} deleted succesfully"