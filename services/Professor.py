from fastapi import HTTPException
from sqlalchemy.orm import Session
from domain.schemas.Professor import Professor, ProfessorData as professor_schema
from domain.models.Professor import Professor as professor_models
from repositories import Professor as professor_repository

def create_professor(db: Session, professor: professor_schema):
    stmt_professor = professor_repository.read_cpf_Professor(db, professor.cpf)
    if stmt_professor:
        raise HTTPException(status_code=400, detail= "Professor already exists")
    stmt_professor = professor_models(**professor.dict())
    return create_professor(db, stmt_professor)

def read_all_professor(db: Session):
    return professor_repository.read_all_Professor(db)

def read_professor(db: Session, professor_id: str):
    stmt_professor = professor_repository.read_Professor(db, professor_id)
    if stmt_professor is None:
        raise HTTPException(status_code=404, detail="professor not found")
    return stmt_professor


