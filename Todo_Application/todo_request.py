from pydantic import BaseModel, Field


class TodoRequest(BaseModel):
    todo_id: int
    todo_is_complete: bool
    todo_title: str = Field(min_length=7)
    todo_description: str = Field(min_length=10, max_length=200)
    todo_priority: int = Field(gt=0, lt=6)
