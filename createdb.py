from config.database import engine
from domain.models.generic import GenericBase

from domain.models import (
    Professor,
    Course,
    Discipline,
    Student,
    StudentDiscipline
)

GenericBase.metadata.create_all(bind=engine)
