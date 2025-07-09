from fastapi import FastAPI
from auth.routes import router as auth_router
from routers.todo import router as todo_router
from database import engine, Base
from utils.logger import logger 

app = FastAPI(debug=True)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables created.")

app.include_router(auth_router)
app.include_router(todo_router)
