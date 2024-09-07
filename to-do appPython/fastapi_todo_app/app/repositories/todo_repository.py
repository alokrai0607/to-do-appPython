from sqlalchemy.orm import Session
from app.models.todo import TodoItem

class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_todos(self):
        return self.db.query(TodoItem).all()

    def get_todo_by_id(self, todo_id: int):
        return self.db.query(TodoItem).filter(TodoItem.id == todo_id).first()

    def create_todo(self, todo: TodoItem):
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def update_todo(self, todo_id: int, title: str, description: str, is_completed: bool):
        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.title = title
            todo.description = description
            todo.is_completed = is_completed
            self.db.commit()
            self.db.refresh(todo)
        return todo

    def delete_todo(self, todo_id: int):
        todo = self.get_todo_by_id(todo_id)
        if todo:
            self.db.delete(todo)
            self.db.commit()
        return todo
