from sqlalchemy.orm import Session
from domain.models import Student, StudentDiscipline
from domain.models.Discipline import Discipline
from sqlalchemy import desc

def create_discipline(db: Session, discipline: Discipline):
    db.add(discipline)
    db.commit()
    db.refresh(Discipline)
    return discipline

def read_all_disciplines(db: Session):
    return db.query(Discipline).all()

def read_one_discipline(db: Session, discipline_id: str):
    return db.query(Discipline).filter(Discipline.discipline_id == discipline_id).first()

def read_discipline_by_name(db: Session, discipline_name: str):
    return db.query(Discipline).filter(Discipline.name == discipline_name).first()

def read_students_discipline(db: Session, discipline_id: str):
    return db.query(Student).join(StudentDiscipline).filter(StudentDiscipline.discipline_id == discipline_id).all()

def read_discipline_studentdiscipline(db: Session, discipline_id: str):
    return len(db.query(StudentDiscipline).filter(StudentDiscipline.discipline_id == discipline_id).all())
    
def read_rank(db: Session):
    return db.query(Discipline).order_by(desc()).all()

def update_discipline_add_professor(db: Session, discipline_id: str, professor_id: str, discipline: Discipline):
    db.query(Discipline).filter(Discipline.discipline_id == discipline_id).update({"professor_id": professor_id})
    db.commit()
    db.refresh(discipline)
    return discipline

