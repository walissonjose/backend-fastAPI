from wsgiref.simple_server import server_version
from fastapi import HTTPException
from sqlalchemy.orm import Session

from domain.models import StudentDiscipline
from domain.models.Student import Student
from domain.schemas.Student import StudentBase

from repositories import Student as repository_Student
from repositories import Discipline as repository_Discipline
from repositories import Course as repository_Course

from services import Course as service_course
from services import Discipline as service_discipline

def create_student(db: Session, student: StudentBase):
    stmt_student = repository_Student.read_cpf_student(db, student.cpf)
    if stmt_student:
        raise HTTPException(status_code= 400, detail="Student already exists")
    stmt_student = Student(**student.dict())
    return repository_Student.create_student(db, stmt_student)

def read_students(db: Session):
    return repository_Student.read_students(db)

def read_student(db: Session, student_id: str):
    stmt_student = repository_Student.read_student(db, student_id)
    if stmt_student:
        raise HTTPException(status_code= 404, detail="Student not exists")
    return stmt_student

def update_student_course(db: Session, student_id: str, course_id: str):
    student = read_student(db, student_id)
    course = service_course.read_course_by_id(db, course_id)
    if(student or course) == None:
        raise HTTPException(status_code=404, detail="Student or course not exists")
    return repository_Student.update_course_of_student(db, student_id, course_id, student)

#def update_matriculate_student_discipline(db: Session, student_id: str, discipline_id: str):
#    student = read_student(db, student_id)
#    discipline = service_discipline.read_one_discipline(db, discipline)
#    if (student or discipline) is None:
#        raise HTTPException(status_code=404, detail="Student or class not exists")
#    matricule = repository_Student.read_matricule(db, student_id, discipline_id)
#    if len(matricule) != 0:
#        raise HTTPException(status_code=400, detail="The student already matriculated")
#    student_matricule = StudentDiscipline(student_id = student_id, discipline_id = discipline_id)
#    return repository_Student.update_matricule_student_discipline(db, student, student_matricule)

#def delete_matricule(db: Session, student_id: str, discipline_id: str):
#    student = read_student(student_id)
#    discipline = service_discipline.read_one_discipline(discipline_id)
#    if (student or discipline) is None:
#        raise HTTPException(status_code=404, detail = "Student or discipline not found")
#    student_discipline = repository_Student.read_all_discipline_from_student(db, student_id, discipline_id)
#    if(len(student_discipline)) == 0:
#        raise HTTPException(status_code= 404, detail="Student is not matriculated in this class")
#    return repository_Student.delete_student_discipline(db, student_id, discipline_id, student)