from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from database import SessionLocal
from sqlalchemy.orm import Session
from models import Todo
from schemas import TodoBase, TodoOut, TodoIn, TodoUpdate, TodoUpdateOut

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


@router.post('/todos', response_model=TodoOut)
async def create_todo(todo_in: TodoIn, db: Session = Depends(get_db)):
    todo_out = Todo(**todo_in.model_dump())
    db.add(todo_out)
    db.commit()
    db.refresh(todo_out)
    db.close()
    return {"message": f"Задача добавлена"}


@router.get("/todos/{todo_id}", response_model=TodoBase)
async def show_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(todo_id == Todo.id).first()
    if todo is None:
        return JSONResponse(status_code=404, content={"message": f"Задача №{todo_id} не найдена"})
    return todo


@router.get("/todos/status/{todo_status}")
async def show_todos_status(todo_status: str, db: Session = Depends(get_db)):
    todos = db.query(Todo).filter(todo_status == Todo.status).all()
    if todos == []:
        return JSONResponse(status_code=404, content={"message": f"Задачи со статусом {todo_status} не найдены!"})
    return todos


@router.get("/todos/title/{todo_title}")
async def show_todos_title(todo_title: str, db: Session = Depends(get_db)):
    todos = db.query(Todo).filter(todo_title == Todo.title).order_by(Todo.create_datetime.asc()).all()
    if todos == []:
        return JSONResponse(status_code=404, content={"message": f"Задачи с заголовком {todo_title} не найдены!"})
    return todos


@router.put("/todos/{todo_id}", response_model=TodoUpdateOut)
async def update_todo(todo_id: int, todo_in: TodoUpdate, db: Session = Depends(get_db)):
    todo_query = db.query(Todo).filter(todo_id == Todo.id)
    updated_todo = todo_query.first()
    if updated_todo is None:
        return JSONResponse(status_code=404, content={"message": f"Задача №{todo_id} не найдена"})
    todo_query.update(todo_in.model_dump())
    db.commit()
    db.refresh(updated_todo)
    return {"message": f"Задача №{todo_id} обновлена", "data": updated_todo}


@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(todo_id == Todo.id).first()
    if todo is None:
        return JSONResponse(status_code=404, content={"message": f"Задача №{todo_id} не найдена"})
    db.delete(todo)
    db.commit()
    return {"message": f"Задача №{todo_id} удалена!"}
