

from fastapi import APIRouter, Depends

from app.core.settings import SettingsDeps

from .schema import TaskGetResponse, TaskPath

from .service import TaskServiceDeps



router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])


@router.get("/{task_id}", response_model=TaskGetResponse, description="Get a task by its ID")
async def get_task(
    service: TaskServiceDeps, 
    settings: SettingsDeps,  
    path: TaskPath = Depends()
    ):

    res = service.get(path.task_id)
    print(settings.db.url)
    return TaskGetResponse(id=res)

