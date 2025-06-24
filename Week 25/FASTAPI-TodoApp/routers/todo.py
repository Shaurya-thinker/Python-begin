from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from models.todo import ToDo as DBToDo
from schemas.todo import ToDoCreate, ToDoResponse

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /todos
@router.post("/todos", response_model=ToDoResponse)
def create_todo(todo: ToDoCreate, db: Session = Depends(get_db)):
    db_todo = DBToDo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# GET /todos
@router.get("/todos", response_model=List[ToDoResponse])
def get_all_todos(db: Session = Depends(get_db)):
    return db.query(DBToDo).all()

# GET /todos/{id}
@router.get("/todos/{id}", response_model=ToDoResponse)
def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    todo = db.query(DBToDo).filter(DBToDo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    return todo
