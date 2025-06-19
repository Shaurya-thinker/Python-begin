from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List

from database import SessionLocal, engine
from models import ToDo as DBToDo
import models

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Schemas
class ToDoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class ToDoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]

    class Config:
        orm_mode = True

# POST /todos
@app.post("/todos", response_model=ToDoResponse)
def create_todo(todo: ToDoCreate, db: Session = Depends(get_db)):
    db_todo = DBToDo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# GET /todos
@app.get("/todos", response_model=List[ToDoResponse])
def get_all_todos(db: Session = Depends(get_db)):
    return db.query(DBToDo).all()

# GET /todos/{id}
@app.get("/todos/{id}", response_model=ToDoResponse)
def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    todo = db.query(DBToDo).filter(DBToDo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    return todo
