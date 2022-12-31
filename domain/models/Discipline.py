from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from .generic import GenericBase

class Discipline(GenericBase):
    __tablename__ = "discipline"
    
    discipline_id = Column(String, primary_key = True)
    name = Column(String, unique = True)
    discipline_code = Column(String, unique = True)
    description = Column(String)
    professor_id = Column(String, ForeignKey("Professor.professor_id"))
    
    professor = relationship("professor", back_populates = "discipline")
    student = relationship("student", secondary = "student_discipline", back_populates = "discipline")