from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float, ForeignKey

DATABASE_URL = "sqlite+aiosqlite:///data.db"

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    name = Column(String)
    phone = Column(String)
    role = Column(String)


class SOSRequest(Base):
    __tablename__ = "sos_requests"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    lat = Column(Float)
    lon = Column(Float)
    status = Column(String, default="new")


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
