from sqlalchemy.orm import Session
from app.repositories.todo_repository import TodoRepository
from app.models.todo import TodoItem

class TodoService:
    def __init__(self, db: Session):
        self.repository = TodoRepository(db)

    def get_all_todos(self):
        return self.repository.get_todos()

    def get_todo_by_id(self, todo_id: int):
        return self.repository.get_todo_by_id(todo_id)

    def create_new_todo(self, title: str, description: str):
        new_todo = TodoItem(title=title, description=description)
        return self.repository.create_todo(new_todo)

    def update_existing_todo(self, todo_id: int, title: str, description: str, is_completed: bool):
        return self.repository.update_todo(todo_id, title, description, is_completed)

    def delete_todo_by_id(self, todo_id: int):
        return self.repository.delete_todo(todo_id)
