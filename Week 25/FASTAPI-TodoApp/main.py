from fastapi import FastAPI
from models import todo
from database import engine
from routers import todo as todo_router

# Create DB tables
todo.Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI()

# Include route module
app.include_router(todo_router.router)
