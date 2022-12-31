from pydantic import BaseModel

def snake_to_camel(snake_str: str | None = None):
    if snake_str is None:
        return None
    splitted = snake_str.split('_')
    return splitted[0] + ''.join(s.title() for s in splitted[1:])

class GenericModel(BaseModel):
    class Config:
        alias_generator = snake_to_camel
        allow_population_by_field_name = True
        #arbitrary_types_allowed = True
