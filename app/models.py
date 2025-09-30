
from pydantic import BaseModel
from typing import Optional

class TodoModel(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class UpdateTodoModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]
