from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from config.database import get_session
from domain.schemas.Professor import Professor, ProfessorData, ProfessorList
from services import Professor as professor_service

router = APIRouter()

professor_tag = 'Professor'

@router.get(
    '/professor',
    summary='Search the data of all professors',
    tags=[professor_tag],
    response_model=ProfessorList
)
def read_professor(db: Session = Depends(get_session)):
    return professor_service.read_all_professor(db)

@router.get(
    '/professor/{professor_id}',
    summary='Search one professor data',
    tags=[professor_tag],
    response_model=Professor
)
def read_professor(professor_id: UUID, db: Session = Depends(get_session)):
    return professor_service.get_professor(professor_id, db)

@router.post(
    '/professor',
    summary='Add new professor',
    tags=[professor_tag],
    status_code=201,
    response_model=Professor
)
def add_professor(professor: ProfessorData, db: Session = Depends(get_session)):
    return professor_service.create_professor(professor, db)

