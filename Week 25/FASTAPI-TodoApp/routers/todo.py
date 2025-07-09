from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.todo import ToDo
from schemas.todo import ToDoCreate, ToDoOut
from database import get_db
from auth.utils import get_current_user
from models.user import User
from utils.logger import logger  

router = APIRouter(prefix="/todos", tags=["ToDos"])


@router.post("/", response_model=ToDoOut)
async def create_todo(todo: ToDoCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    logger.info(f"User {current_user.username} is creating a ToDo: {todo.title}")
    new_todo = ToDo(**todo.dict(), user_id=current_user.id)
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    logger.info(f"ToDo '{new_todo.title}' created with ID {new_todo.id} by user {current_user.username}")
    return new_todo


@router.get("/", response_model=list[ToDoOut])
async def get_todos(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    logger.info(f"Fetching ToDos for user {current_user.username}")
    result = await db.execute(select(ToDo).where(ToDo.user_id == current_user.id))
    todos = result.scalars().all()
    logger.info(f"Found {len(todos)} ToDos for user {current_user.username}")
    return todos


@router.get("/{id}", response_model=ToDoOut)
async def get_todo(id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    logger.info(f"User {current_user.username} requested ToDo with ID {id}")
    result = await db.execute(select(ToDo).where(ToDo.id == id, ToDo.user_id == current_user.id))
    todo = result.scalar_one_or_none()
    if not todo:
        logger.warning(f"ToDo with ID {id} not found for user {current_user.username}")
        raise HTTPException(status_code=404, detail="ToDo not found")
    logger.info(f"ToDo with ID {id} retrieved successfully for user {current_user.username}")
    return todo
