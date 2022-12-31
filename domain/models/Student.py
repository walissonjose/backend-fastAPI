from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .generic import GenericBase

class Student(GenericBase):
    __tablename__ = "student"
    
    student_id = Column(String, primary_key = True)
    cpf = Column(String, unique = True)
    name = Column(String)
    birth_date = Column(String)
    rg = Column(String)
    agency = Column(String)
    uf = Column(String)
    course_id = Column(String, ForeignKey("Courses.course_id"))
    
    __table_args__ = (UniqueConstraint("rg", "agency", "uf"),)
    
    course = relationship("course", back_populates = "")
    discipline = relationship("discipline", secondary = "student_discipline", back_populates = "student")