from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .generic import GenericBase
from .Professor import *

class Course(GenericBase):
    __tablename__ = 'course'
    course_id = Column(String, primary_key = True)
    name = Column(String)
    init_date = Column(String)
    location = Column(String)
    professor_id = Column(String, ForeignKey(Professor.professor_id))
    
    coordinator = relationship("professor", back_populates = "course")
    students = relationship("student", back_populates = "course")