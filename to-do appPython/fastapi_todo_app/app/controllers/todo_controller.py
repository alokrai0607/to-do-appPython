from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.todo_service import TodoService
from app.config import SessionLocal
from pydantic import BaseModel

#This creates an API router for handling the /todos routes.
#we can register this router in our FastAPI app to group our
#routes logically.
router = APIRouter()

class TodoCreate(BaseModel):
    title: str
    description: str

class TodoPartialUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


def get_db():
    db = SessionLocal()
    try:
        yield db #Inject db session into routes
    finally:
        db.close()

@router.get("/todos")
def get_todos(db: Session = Depends(get_db)):# db is used to access the database.
    return TodoService(db).get_all_todos()

@router.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = TodoService(db).get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return TodoService(db).create_new_todo(todo.title, todo.description)

@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str, description: str, is_completed: bool, db: Session = Depends(get_db)):
    return TodoService(db).update_existing_todo(todo_id, title, description, is_completed)


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return TodoService(db).delete_todo_by_id(todo_id)


@router.patch("/todos/{todo_id}")
def patch_todo(todo_id: int, todo: TodoPartialUpdate, db: Session = Depends(get_db)):
    existing_todo = TodoService(db).get_todo_by_id(todo_id)
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.title is not None:
        existing_todo.title = todo.title
    if todo.description is not None:
        existing_todo.description = todo.description
    if todo.is_completed is not None:
        existing_todo.is_completed = todo.is_completed
    return TodoService(db).update_existing_todo(todo_id, existing_todo.title, existing_todo.description, existing_todo.is_completed)
