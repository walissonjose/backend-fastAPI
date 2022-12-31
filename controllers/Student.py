from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from config.database import get_session
from domain.schemas.Student import Student, StudentList as schema_studentList
from services import Student as service_student

router = APIRouter()
student_tag = 'Students'

@router.get(
    '/students',
    summary='Fetch all students data',
    tags=[student_tag],
    response_model= schema_studentList
)
def read_all_student(db: Session = Depends(get_session)):
    return service_student.read_students(db)

@router.get(
    '/students/{student_id}',
    summary='Fetch one students data',
    tags=[student_tag],
    response_model= Student
)
def read_one_student(student_id: str, db: Session = Depends(get_session)):
    return service_student.read_student(db, student_id)

@router.post(
    '/students',
    summary='Add a new student',
    tags=[student_tag],
    status_code=201,
    response_model= Student
)
def create_student(student: Student, db: Session = Depends(get_session)):
    return service_student.create_student(db, student)


@router.put(
    '/student/{student_id}/course/{course_id}',
    summary='Set or change student course',
    tags=[student_tag],
    status_code=201,
    response_model= Student
)
def update_student_course(student_id: str, course_id: str, db: Session = Depends(get_session)):
    return service_student.update_student_course(db, student_id, course_id)

@router.post(
    '/stutend/{student_id}/discipline/{discipline_id}',
    summary='Add the student to a discipline',
    tags=[student_tag],
    status_code=201,
    response_model= Student
)
def update_matricule(student_id: str, discipline_id: str, db: Session = Depends(get_session)):
    return service_student.update_matriculate_student_discipline(db, student_id, discipline_id)

@router.delete(
    '/student/{student_id}/discipline/{discipline_id}',
    summary='Dematricule a student from a discipline',
    tags=[student_tag],
    status_code=200,
    response_model= Student
)
def delete_student_matricule(student_id: str, discipline_id: str, db: Session = Depends(get_session)):
    return service_student.delete_matricule(db, student_id, discipline_id)

