from sqlalchemy import Column, ForeignKey, UniqueConstraint, Integer
from .generic import GenericBase
from .Discipline import *

class StudentDiscipline(GenericBase):
    __tablename__ = 'student_siscipline'
    
    matricule_id = Column(Integer, primary_key = True, autoincrement = True)
    student_id = Column(String, ForeignKey("Students.student_id"))
    discipline_id = Column(String, ForeignKey("Discipline.discipline_id"))
    
    __table_args__ = (UniqueConstraint("student_id", "discipline_id"),)