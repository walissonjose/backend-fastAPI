from sqlalchemy.orm import Session 
from domain.models.Course import Course
from domain.models.Student import Student

def create_course(db: Session, course: Course):
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def read_courses(db: Session):
    return db.query(Course).all()

def read_course(db: Session, course_id: str):
    return db.query(Course).filter(Course.course_id == course_id).first()

def read_course_by_name(db: Session, name: str):
    return db.query(Course).filter(Course.name == name).first()

def read_student_course(db: Session, course_id: str):
    print(db.query(Student).filter(Student.course_id == course_id).all())
    return db.query(Student).filter(Student.course_id == course_id).all()


def update_coordinator(db: Session, course_id: str, coordinator_id: str, course: Course):
    db.query(Course).filter(Course.course_id == course_id).updated({"coordinator_id": coordinator_id})
    db.commit()
    db.refresh(course)
    return course


    