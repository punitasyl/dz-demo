
from typing import Annotated

from fastapi import Depends



class TaskRepository:
    def get_by_id(self, task_id: int):
        # Logic to retrieve a task by its ID
        return task_id

def get_task_repository():
    return TaskRepository()

TaskRepositoryDeps =  Annotated[TaskRepository, Depends(get_task_repository)]


