import asyncio
from database import engine
from models.user import Base  # or wherever Base is defined

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)  # Drop all tables
        await conn.run_sync(Base.metadata.create_all)  # Recreate them

if __name__ == "__main__":
    asyncio.run(init_models())
