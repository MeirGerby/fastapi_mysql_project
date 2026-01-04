from pydantic import BaseModel 

class People(BaseModel):
    id: int 
    first_name: str 
    last_name: str 
    age: int 
    profession: str 
    