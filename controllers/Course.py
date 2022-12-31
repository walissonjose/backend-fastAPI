from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_session
from domain.schemas.Course import Course, CourseData, CourseList
from services import Course as course_service

router = APIRouter()

course_tag = 'Course'

@router.get(
    '/course',
    summary='Search all course information',
    tags = [course_tag],
    response_model= CourseList
)
def read_courses(db: Session = Depends(get_session)):
    return course_service.read_all_courses(db)

@router.get(
    '/course/{course_id}',
    summary='Search course data',
    tags=[course_tag],
    response_model=Course
)
def read_course(course_id: str, db: Session = Depends(get_session)):
    return course_service.read_course_by_id(db, course_id)

@router.get(
    '/course/{course_id}/student',
    summary='View all students in course',
    tags=[course_tag],
    response_model=list
)
def read_student_course(course_id: str, db: Session = Depends(get_session)):
    return course_service.read_course_student(db, course_id)


@router.post(
    '/course',
    summary='Add a new course',
    tags=[course_tag],
    status_code=201,
    response_model=Course
)
def add_course(course: CourseData, db: Session = Depends(get_session)):
    return course_service.create_course(db, course)

@router.put(
    '/course/{course_id}/coordinator/{professor_id}',
    summary='Add or change the course coordinator',
    tags=[course_tag],
    status_code=201,
    response_model=Course
)
def put_coordinator_course(course_id: str, professor_id: int, db: Session = Depends(get_session)):
    return course_service.update_course_coordinator(db, course_id, professor_id)


