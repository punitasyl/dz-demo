from fastapi import Body, FastAPI

from projects.routes import router as project_routes
from tasks.routes import router as task_routes

app = FastAPI(
    title="Kanban Board API",
    description="API for managing projects and tasks in a Kanban board",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Projects","description": "Operations related to projects",
        },
        {
            "name": "Tasks","description": "управление задачами",
        }
    ]
)

app.include_router(project_routes)
app.include_router(task_routes)
