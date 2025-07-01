from pydantic import BaseModel

class ToDoCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class ToDoOut(ToDoCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True