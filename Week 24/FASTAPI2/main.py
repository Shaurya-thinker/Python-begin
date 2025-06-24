from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

 
 
""" from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# In-memory storage
todos = []
id_counter = 1

# ToDo item schema
class ToDo(BaseModel):
    title: str
    description: Optional[str] = None

# POST /todos: Add a new task
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

# GET /todos/{id}: Get a specific task by ID
@app.get("/todos/{id}")
def get_todo_by_id(id: int):
    for todo in todos:
        if todo["id"] == id:
            return todo
    raise HTTPException(status_code=404, detail="Task not found")
 """



""" from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# In-memory storage
todos = []
id_counter = 1

# Pydantic model for creating a task (input)
class ToDoCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Pydantic model for returning a task (output)
class ToDoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

# POST /todos: Add a new task
@app.post("/todos", response_model=ToDoResponse)
def create_todo(todo: ToDoCreate):
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
@app.get("/todos", response_model=List[ToDoResponse])
def get_all_todos():
    return todos

# GET /todos/{id}: Get a specific task by ID
@app.get("/todos/{id}", response_model=ToDoResponse)
def get_todo_by_id(id: int):
    for todo in todos:
        if todo["id"] == id:
            return todo
    raise HTTPException(status_code=404, detail="Task not found") """
