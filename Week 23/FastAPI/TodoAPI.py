from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# In-memory storage
todos = []
id_counter = 1

# Request model
class ToDo(BaseModel):
    title: str
    description: Optional[str] = None

# POST /todos: Add new task
@app.post("/todos")
def create_todo(todo: ToDo):
    global id_counter
    todo_item = {
        "id": id_counter,
        "title": todo.title,
        "description": todo.description
    }
    todos.append(todo_item)
    id_counter += 1
    return todo_item

# GET /todos: Get all tasks
@app.get("/todos")
def get_all_todos():
    return todos

# GET /todos/{id}: Get task by ID
@app.get("/todos/{id}")
def get_todo_by_id(id: int):
    for todo in todos:
        if todo["id"] == id:
            return todo
    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/check")
def check():
    return {"status": "This is TodoAPI!"}

