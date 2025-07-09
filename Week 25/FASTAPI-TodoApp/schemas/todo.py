from pydantic import BaseModel

class ToDoCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class ToDoOut(ToDoCreate):
    id: int
    title: str
    description: str = ""

    class Config:
        from_attributes = True