from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///crm.db")

Base = declarative_base()

Session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

def get_db():
    db = Session()
    try:
        return db
    finally:
        db.close()