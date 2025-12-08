from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    id: int
    title: str
    desc: str
    status: str
    create_datetime: datetime
    update_datetime: datetime


class TodoOut(BaseModel):
    message: str


class TodoIn(BaseModel):
    title: str
    desc: str
