import datetime
import os
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship, Session, sessionmaker
from sqlalchemy import ForeignKey, String, BigInteger, text, Text, func, DateTime, create_engine
from datetime import timezone
from dotenv import load_dotenv
load_dotenv()
USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

engine = create_async_engine(url=f"postgresql+asyncpg://{USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
                             echo=True)

sync_engine = create_engine(url=f"postgresql+psycopg://{USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
                             echo=True)

async_session = async_sessionmaker(engine)
sync_session = sessionmaker(sync_engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Words(Base):
    __tablename__ = 'words'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    level: Mapped[str] = mapped_column(String(5), nullable=True)
    theme: Mapped[str] = mapped_column(String(200), nullable=True)
    phonetics: Mapped[str] = mapped_column(String(50), nullable=True)
    word: Mapped[str] = mapped_column(String(200), nullable=True)
    trl: Mapped[str] = mapped_column(String(200), nullable=True)
    trt: Mapped[str] = mapped_column(String(300), nullable=True)
    past: Mapped[str] = mapped_column(String(200), nullable=True)
    past_trl: Mapped[str] = mapped_column(String(200), nullable=True)
    comm: Mapped[str] = mapped_column(String(200), nullable=True)
    comm_trl: Mapped[str] = mapped_column(String(200), nullable=True)
    comm_trt: Mapped[str] = mapped_column(String(200), nullable=True)

class Reading(Base):
    __tablename__ = 'reading'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    level: Mapped[str] = mapped_column(String(5), nullable=True)
    phonetics: Mapped[str] = mapped_column(String(50), nullable=True)
    title: Mapped[str] = mapped_column(String(300), nullable=True)
    text: Mapped[str] = mapped_column(Text, nullable=True)



async def async_main():
    async with engine.begin() as conn:
        print('async_main')
        await conn.run_sync(Base.metadata.create_all)