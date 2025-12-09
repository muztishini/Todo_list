from sqlalchemy import Column, Integer, String, DateTime, Text, Enum
from database import Base, engine
from datetime import datetime
from enum import Enum as PyEnum


class TodoStatus(PyEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    COMPLETED = "completed"
    IN_WORK = "in_work"


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    desc = Column(Text, nullable=False)
    status = Column(Enum(TodoStatus), default="ACTIVE")
    create_datetime = Column(DateTime, default=datetime.now)
    update_datetime = Column(DateTime, default=datetime.now, onupdate=datetime.now)


Base.metadata.create_all(engine)
