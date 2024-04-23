from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings


class Base(DeclarativeBase):
    pass


URL = settings.POSTGRES_URL

Engine = create_async_engine(
    url=URL,
    echo=True,
)
Session = async_sessionmaker(
    bind=Engine,
    expire_on_commit=False,
    autoflush=True
)
