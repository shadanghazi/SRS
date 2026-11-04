from pydantic import BaseModel, Field

class StudentBase(BaseModel):
    name: str= Field(min_length=3, max_length=50)
    age:int= Field(ge=5,le=34)

class StudentCreate(StudentBase):
    pass
class StudentUpdate(StudentBase):
    pass
class StudentOut(StudentBase):
    id : int 