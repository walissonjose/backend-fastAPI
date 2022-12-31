from fastapi import HTTPException
from sqlalchemy.orm import Session
from domain.models.Course import Course
from domain.schemas.Course import CourseData
from repositories import Course as repository_course
from services import Professor as service_professor



def create_course(db: Session, course: CourseData):
    stmt_course = repository_course.read_course_by_name(db, course.name)
    if stmt_course:
        raise HTTPException(status_code= 400, detail="Course already exists")
    stmt_course = Course(**course.dict())
    return create_course(db, stmt_course)

def read_all_courses(db: Session):
    return repository_course.read_courses(db)

def read_course_by_id(db: Session, course_id: str):
    stmt_course = repository_course.read_course(db, course_id)
    if stmt_course is None:
        raise HTTPException(status_code= 404, detail= "Course not founded")
    return stmt_course

def read_course_student(db: Session, course_id: str):
    stmt_course = repository_course.read_course(db, course_id)
    if stmt_course is None:
        raise HTTPException(status_code= 404, detail= "Course not foundedd")
    return repository_course.read_student_course(db, course_id)

def update_course_coordinator(db: Session, course_id: str, coordinator_id: str):
    course = read_course_by_id(db, course_id)
    professor = service_professor.read_professor(db, coordinator_id)
    if (professor or course) is None:
        raise HTTPException(status_code=404, detail= "Professor or course not found")
    return repository_course.update_coordinator(db, course_id, coordinator_id, course)

