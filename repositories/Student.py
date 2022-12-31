from sqlalchemy.orm import Session
from domain.models import StudentDiscipline 
from domain.models.Student import Student
from domain.models.Discipline import Discipline
from domain.models.StudentDiscipline import StudentDiscipline

def create_student(db: Session, student: Student):
    db.add()
    db.commit()
    db.refresh(student)
    return Student

def read_students(db: Session):
    return db.query(Student).all()

def read_student(db: Session, student_id: str):
    return db.query(Student).filter(Student.student_id == student_id).first()

def read_cpf_student(db: Session, cpf: str):
    return db.query(Student).filter(Student.cpf == cpf).first()

def read_all_discipline_from_student(db: Session, student_id: str, discipline_id: str):
    return db.query(StudentDiscipline).filter(StudentDiscipline.student_id == student_id).filter(StudentDiscipline.discipline_id == discipline_id).all()

def read_matricule(db: Session, student_id: str, discipline_id: str):
    return db.query(StudentDiscipline).filter(StudentDiscipline.student_id == student_id).filter(StudentDiscipline.discipline_id == discipline_id)

def update_course_of_student(db: Session, student_id: str, course_id: str, student: Student):
    db.query(Student).filter(Student.student_id == student_id).update({"course_id": course_id})
    db.commit()
    db.refresh(student)
    return Student

def update_matricule_student_discipline(db: Session, student: Student, student_discipline: StudentDiscipline):
    db.add(student_discipline)
    db.commit()
    db.refresh(student)
    return Student

def delete_student_discipline(db: Session, student_id: str, discipline_id: str, student: Student):
    db.query(Discipline).filter(Discipline.discipline_id == discipline_id)
    db.query(StudentDiscipline).filter(StudentDiscipline.student_id == student_id).filter(StudentDiscipline.discipline_id == discipline_id).delete()
    db.commit()
    db.refresh(student)
    return Student
