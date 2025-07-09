from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from schemas.user import UserCreate, Token
from models.user import User
from auth.utils import hash_password, verify_password, create_access_token
from database import get_db
from utils.logger import logger  

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"Attempting registration for username: {user.username}")

    result = await db.execute(select(User).where(User.username == user.username))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        logger.warning(f"Registration failed: Username '{user.username}' is already taken.")
        raise HTTPException(status_code=400, detail="Username taken")

    new_user = User(username=user.username, password=hash_password(user.password))
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    logger.info(f"User '{user.username}' registered successfully.")
    return {"message": "User created"}


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    logger.info(f"Login attempt for username: {form_data.username}")

    result = await db.execute(select(User).where(User.username == form_data.username))
    db_user = result.scalar_one_or_none()
    if not db_user or not verify_password(form_data.password, db_user.password):
        logger.warning(f"Login failed for username: {form_data.username}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.username})
    logger.info(f"User '{form_data.username}' logged in successfully.")
    return {"access_token": token, "token_type": "bearer"}
