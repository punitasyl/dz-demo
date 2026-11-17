

from fastapi import APIRouter, Depends

from .schema import TaskGetResponse, TaskPath

from .service import TaskServiceDeps



router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])


@router.get("/{task_id}", response_model=TaskGetResponse, description="Get a task by its ID")
async def get_task(
    service: TaskServiceDeps,   
    path: TaskPath = Depends()
    ):

    res = service.get(path.task_id)
    return TaskGetResponse(id=res)

