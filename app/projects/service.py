
from fastapi.params import Depends
from typing_extensions import Annotated

from .repository import ProjectRepository, ProjectRepositoryDeps

    


def get_project_service(repo: ProjectRepositoryDeps):
     return ProjectService(repo)

class ProjectService():
    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    def get_project(self, project_id: int):
        # Logic to retrieve a project by its ID
        return self.repo.get_by_id(project_id)

ProjectServiceDeps =  Annotated[ProjectService, Depends(get_project_service)]
    
