from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_session
from domain.schemas.Discipline import Discipline as schema_discipline, DisciplineList
from services import Discipline as service_discipline

router = APIRouter()

discipline_tags="Discipline"

@router.get(
    '/discipline',
    summary= 'read data from all Disciplines',
    tags = [discipline_tags],
    response_model= DisciplineList
)
def read_disciplines(db: Session = Depends(get_session)):
    return service_discipline.read_disciplines(db)

@router.get(
    '/discipline/{discipline_id}',
    summary='Search the Discipline data',
    tags=[discipline_tags],
    response_model= schema_discipline
    )
def read_discipline(discipline_id: str, db: Session = Depends(get_session)):
    return service_discipline.read_one_discipline(db, discipline_id)

@router.post(
    '/Discipline',
    summary='Add new Discipline',
    tags=[discipline_tags],
    status_code=201,
    response_model= schema_discipline
)
def add_Discipline(Discipline: schema_discipline, db: Session = Depends(get_session)):
    return service_discipline.create_discipline(db, Discipline)

@router.put(
    '/discipline/{discipline_id}/professor/{professor_id}',
    summary='Set or change the professor of a discipline',
    tags=[discipline_tags],
    status_code=201,
    response_model= schema_discipline
)
def put_professor_Discipline(discipline_id: str, professor_id: str, db: Session= Depends(get_session)):
    return service_discipline.update_discipline_professor(db, discipline_id, professor_id)

@router.get(
    '/discipline/{discipline_id}/student',
    summary='See all students enrolled in the discipline',
    tags=[discipline_tags],
    status_code= 201,
    response_model= schema_discipline
)
def get_student_discipline(discipline_id: str, db: Session = Depends(get_session)):
    return service_discipline.read_discipline_students(db, discipline_id)

@router.get(
    '/ranking/discipline',
    summary='Get a ranking of discipline grouped by the number of students matriculated',
    tags=[discipline_tags],
    status_code= 201,
    response_model= list[schema_discipline]
)
def rank_of_discipline(db: Session = Depends(get_session)):
    return service_discipline.read_rank_disciplines(db)
    

