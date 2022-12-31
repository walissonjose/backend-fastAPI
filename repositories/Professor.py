from sqlalchemy.orm import Session
from domain.models.Professor import Professor

def create_Professor(db: Session, professor: Professor):
    db.add(professor)
    db.commit()
    db.refresh(professor)
    return Professor

def read_all_Professor(db: Session):
    return db.query(Professor).all()

def read_Professor(db: Session, professor_id: str):
    return db.query(Professor).filter(Professor.professor_id == professor_id).first()

def read_cpf_Professor(db: Session, cpf = str):
    return db.query(Professor).filter(Professor.cpf == cpf).first()

