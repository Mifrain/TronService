import pytest
import asyncio
from app.config import settings
from app.database import Base, engine, async_session_maker
from httpx import AsyncClient, ASGITransport
from app.main import app as fastapi_app

# Исправим фикстуру для asyncio event loop
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


# Фикстура для подготовки базы данных
@pytest.fixture(scope='session', autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    # Создаем все таблицы в тестовой базе данных
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# Фикстура для AsyncClient
@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url="http://test") as ac:
        yield ac
