# GETT Query rnd_from and rnd_to, return random int between them


from fastapi import APIRouter, Depends, HTTPException, Request
import random

from .repository import ProjectRepositoryDeps

from .service import ProjectServiceDeps

from .schema import (
    ProjectCreateRequest,
    ProjectCreateResponse,
    ProjectGetResponse,
    ProjectPath,
    ProjectUpdateRequest,
    ProjectUpdateResponse,
)


router = APIRouter(prefix="/v1/projects", tags=["Projects"])
router2 = APIRouter(prefix="/v2/projects", tags=["Projects"])


@router.get("/{project_id}", response_model=ProjectGetResponse, description="Get a project by its ID")
async def get_project(
    service: ProjectServiceDeps,
    path: ProjectPath = Depends()
    ):
    res = service.get_project(path.project_id)
    return ProjectGetResponse(id=res)


@router.post("/", response_model=ProjectCreateResponse, status_code=201, description="Create a new project with the given details")
async def create_post(data: ProjectCreateRequest):
    print(data)
    return ProjectCreateResponse(id=random.randint(1, 100), name=data.name)


@router.patch("/{project_id}", response_model=ProjectUpdateResponse, description="Update a project with the given details")
async def update_project(data: ProjectUpdateRequest, path: ProjectPath = Depends()):

    return ProjectUpdateResponse(
        id=path.project_id,
        key="random_key",
        name=data.name,
        description=data.description,
    )
