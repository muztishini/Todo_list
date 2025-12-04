from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import desc
from models import Todo

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/todos")
async def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos


@router.post('/todos')
async def create_todo(data=Body(), db: Session = Depends(get_db)):
    todo_out = Todo(title=data['title'], desc=data['desc'])
    db.add(todo_out)
    db.commit()
    db.refresh(todo_out)
    db.close()
    return {"message": f"Задача добавлена"}


@router.get("/todos/{todo_id}")
async def show_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(todo_id == Todo.id).first()
    if todo is None:
        return JSONResponse(status_code=404, content={"message": f"Задача №{todo_id} не найдена"})
    return todo
