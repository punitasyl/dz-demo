

from pydantic import BaseModel, Field


class TaskPath(BaseModel):
    task_id: int = Field(
        ..., gt=0, description="Task ID must be a positive integer"
    )

class TaskGetResponse(BaseModel):
    id: int
   