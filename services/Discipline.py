from fastapi import HTTPException
from sqlalchemy.orm import Session
from domain.models.Discipline import Discipline
from domain.schemas.Discipline import DisciplineBase
from repositories import Discipline as repository_Discipline
from services import Professor as service_professor


def create_discipline(db: Session, discipline):
    stmt_discipline = repository_Discipline.read_discipline_by_name(db, discipline.name)
    if stmt_discipline:
        raise HTTPException(status_code= 400, detail="Class already exists")
    stmt_discipline = Discipline(**discipline.dict())
    return repository_Discipline.create_discipline(db, stmt_discipline)

def read_disciplines(db: Session):
    return repository_Discipline.read_all_disciplines(db)

def read_one_discipline(db: Session, discipline_id: str):
    stmt_discipline = repository_Discipline.read_one_discipline(db, discipline_id)
    if stmt_discipline is None:
        raise HTTPException(status_code=404, detail="Discipline not founded")
    return stmt_discipline

def read_discipline_students(db: Session, discipline_id: str):
    stmt_discipline = repository_Discipline.read_one_discipline(db, discipline_id)
    if stmt_discipline is None:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return repository_Discipline.read_students_discipline(db, discipline_id)

def read_rank_disciplines(db: Session):
    return repository_Discipline.read_rank(db)

def update_discipline_professor(db: Session, professor_id: str, discipline_id: str):
    discipline = read_one_discipline(db, discipline_id)
    professor = service_professor.read_professor(db, professor_id)
    if (professor or discipline) is None:
        raise HTTPException(status_code=404, detail= "Professor or discipline not found")
    return repository_Discipline.update_discipline_add_professor(db, discipline_id, professor_id, discipline)
