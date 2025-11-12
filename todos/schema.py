from pydantic import BaseModel, Field


class Todo(BaseModel):
    todo: str
    completed: bool = Field(False)
