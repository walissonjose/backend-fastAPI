from pydantic import BaseModel, Field
from .generic import GenericModel
from typing import List

#corpo do objeto professor
class ProfessorData(GenericModel):
    cpf: str = Field(title='CPF of Professor')
    name: str = Field(title = 'Name of Professor')
    title: str = Field(title = 'Informate the Professor degree')
    
    class Config:
        orm_model = True 
        schema_extra = {
                "example": 
                    {
                        "name": "Ricardo",
                        "cpf": "000.000.000-00",
                        "title": "PhD"
                    }
            }
        
#corpo do objeto professor COM id
class Professor(ProfessorData):
    professor_id: str = Field(title='ID of Professor')
    class Config:
        orm_model = True
        schema_extra = {
            "example": 
                {
                    "professor_id": "6f04bb79-750c-4d98-8bde-86d697b0f04e",
                    "name": "Ricardo",
                    "cpf": "000.000.000-00",
                    "title": "PhD"
                }
        }
         
class ProfessorList(BaseModel):
    __root__: List[Professor]
    class Config:
        orm_model = True
        schema_extra = {
            "title": 'List of professor'
        }