from pydantic import BaseModel, Field
from domain.schemas.Course import Course

from domain.schemas.Discipline import DisciplineList
from .generic import GenericModel
from datetime import date
from typing import List

class StudentBase(GenericModel):
    
    cpf: str = Field( title = 'CPF of Student')
    name: str = Field(title='Name of Student')
    birth_date: date | None = Field(default=None, title = 'Birth date of Student')
    rg: str = Field(title='Indentify number of Student RG')
    agency: str = Field(title = 'Agency who expedit Student RG')
    uf: str = Field(title = 'State who expedits RG of Student')
    
    class Config:
        orm_model = True
        schema_extra = {
            "example": {
                "name": "Walisson Araujo",
                "birth_date": "2001-05-02",
                "cpf": "000.000.000-00",
                "rg": "00000000",
                "agency": "SSP",
                "uf": "AL"
                }
            }
        

class Student(StudentBase):
    
    student_id: str = Field(title = 'ID of Student')
    course: Course | None = Field(title = 'Course of the Student')
    discipline: DisciplineList | None = Field(title = 'Classes of the Student')
    
    class Config:
        orm_model = True
        schema_extra = {
            "example": {
                "id": "ecac7712-08e4-4bfb-a697-9018a74429fa",
                "course": {
                    "id": "3eefcead-1be7-476c-a7b4-4778c3f738de",
                    "name": "Engenharia Civil",
                    "init_date": "1955-03-01",
                    "building_name": "CTEC",
                    "coordinator":{
                        'name':'Bob',
                        'cpf':'168.169.967-90',
                        'titration':'PhD',
                        'id':'f3a9f393-3d58-4082-a8b8-cd89a63465fe'
                    }
                    
                },
                "discipline": [
                    {
                        "name": "Cálculo 1",
                        "code": "MAT-01",
                        "description": "Limites, derivadas, integrais, etc",
                        "id": "f3a9f393-3d58-4082-a8b8-cd89a63465fe",
                        "professor":{
                            'name': 'Beleza',
                            'cpf': '666.616.626-69',
                            'title': "PhD"
                        }
                    },
                    {
                        "name": "Mecânica dos Sólidos",
                        "code": "ECIV-51",
                        "description": "Elasticidade, tração, flexão, etc",
                        "id": "c97aa5a6-6284-4613-83b1-27d97d45e6e7",
                        "professor":{
                            'name': 'Luciano',
                            'cpf': '416.567.876.87',
                            'title': "PhD"
                        }
                    }
                ]
            }
        }
         
class StudentList(BaseModel):
    __root__: List[Student]
    class Config:
        orm_model = True
        arbitrary_types_allowed = True
        schema_extra = {
            "title": 'List of students'
        }