
from fastapi.params import Depends
from typing_extensions import Annotated

from .repository import TaskRepository, TaskRepositoryDeps

    


def get_task_service(repo: TaskRepositoryDeps):
     return TaskService(repo)

class TaskService():
    def __init__(self, repo: TaskRepositoryDeps):
        self.repo = repo

    def get(self, task_id: int):
        # Logic to retrieve a task by its ID
        return self.repo.get_by_id(task_id)

TaskServiceDeps =  Annotated[TaskService, Depends(get_task_service)]
    
