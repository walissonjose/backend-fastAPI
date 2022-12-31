from typing import Generic, List
from pydantic import BaseModel, Field 
from .generic import GenericModel 
from .Professor import Professor 

class DisciplineBase(GenericModel):
    name: str = Field(title = "Name of Discipline")
    discipline_code: str = Field(title = "Code of Discipline")
    description: str = Field(title = "Short description of Discipline")
    
    class Config: 
        orm_model = True
        schema_extra = { 
                        'example':{
                            'name' : 'material Technology',
                            'discipline_code':'TECM',
                            'description': 'Estudo da ciência dos materiais'
                        }
                    }
        
class Discipline(DisciplineBase):
    discipline_id: str = Field(title = 'ID of Discipline')
    professor: Professor | None = Field(title='Master of Discipline as Professor')
    
    class config:
        orm_model = True
        schema_extra = {
            'example': {
                'id': '11',
                'professor':{
                    'name': 'Ricardo',
                    'cpf': '134.567.987-02',
                    'title': 'PhD',
                    'id': 'str'
                }
            }
        }
        
class DisciplineList(BaseModel):
    __root__: List[Discipline]
    class Config:
        orm_model = True, 
        arbitrary_types_allowed = True, 
        schema_extra = {
            'title' : 'List of Discipline'
        }