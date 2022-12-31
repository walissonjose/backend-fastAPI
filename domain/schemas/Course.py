from domain.schemas.Professor import Professor
from pydantic import BaseModel, Field
from .generic import GenericModel
from typing import List
from datetime import date

class  CourseData(GenericModel):
    name: str = Field(title = 'Name of Course')
    creation_date: date = Field(default=None, title = 'Creation date of Course')
    location: str = Field(title='Where is located this Course?')
    class config:
        orm_model = True
        schema_extra = {
                "example": 
                        {
                            "name": "Engenharia Civil",
                            "creation_date": "1955-03-01",
                            "location": "CTEC"
                        }
            }

class Course(CourseData):
    course_id: str = Field(title='ID of Course')
    coordinator: Professor | None = Field(title='Coordinator of Course')
    
    class Config:
        schema_extra = {
            "example": {
                
                "course_id": "ecac7712-08e4-4bfb-a697-9018a74429fa",
                "coordinator": 
                    {
                        "professor_id": "6f04bb79-750c-4d98-8bde-86d697b0f04e",
                        "cpf": "000.000.000-00",
                        "name": "Ricardo",
                        "title": "PhD"
                    }
            }
        }  


class CourseList(BaseModel):
    __root__: List[Course]
    class Config:
        orm_model = True
        arbitrary_types_allowed = True
        schema_extra = {
            "title": 'List of courses'
        }