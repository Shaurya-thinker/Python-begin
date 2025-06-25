from fastapi import FastAPI
from database import engine
from models import todo, user
from routers import todo as todo_router, auth as auth_router

todo.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router.router)
app.include_router(auth_router.router)
