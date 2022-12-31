from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .generic import GenericBase

class Professor(GenericBase):
    __tablename__ = "professor"
    professor_id = Column(String, primary_key=True)
    name = Column(String)
    cpf = Column(String, unique = True)
    title = Column(String)
    
    discipline = relationship("discipline", back_populates = "professor")
    courses = relationship("course", back_populates = "coordinator")