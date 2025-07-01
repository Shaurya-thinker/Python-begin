from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.todo import ToDo
from schemas.todo import ToDoCreate, ToDoOut
from database import get_db
from auth.utils import get_current_user
from models.user import User

router = APIRouter(prefix="/todos", tags=["ToDos"])

@router.post("/", response_model=ToDoOut)
async def create_todo(todo: ToDoCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_todo = ToDo(**todo.dict(), user_id=current_user.id)
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo

@router.get("/", response_model=list[ToDoOut])
async def get_todos(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(ToDo).where(ToDo.user_id == current_user.id))
    return result.scalars().all()

@router.get("/{id}", response_model=ToDoOut)
async def get_todo(id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(ToDo).where(ToDo.id == id, ToDo.user_id == current_user.id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo