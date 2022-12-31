import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

load_dotenv()

database_url = os.getenv('DATABASE_URL') or 'sqlite:///./fastapi_sql_prograd.db'

engine = create_engine(
    database_url, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
