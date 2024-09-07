#raw SQL queries.
from sqlalchemy import Column, Integer, String, Boolean
#importing the Base class from config module
from app.config import Base

class TodoItem(Base):
    __tablename__ = 'todo_items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    is_completed = Column(Boolean, default=False)
