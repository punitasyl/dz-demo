from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException


class ProjectPath(BaseModel):
    project_id: int = Field(
        ..., gt=0, description="Project ID must be a positive integer"
    )


class ProjectGetResponse(BaseModel):
    id: int


class ProjectUpdateRequest(BaseModel):
    name: str | None = None
    description: str | None = None


class ProjectUpdateResponse(BaseModel):
    id: int
    key: str
    name: str | None = None
    description: str | None = None


class ProjectCreateRequest(BaseModel):
    key: str
    name: str
    description: str | None = None

    model_config = {
        "extra": "forbid",
    }

    @field_validator("key")
    @classmethod
    def key_not_empty(cls, v):
        if not v.strip():
            raise HTTPException(status_code=400, detail="Key must be valid string")
        return v


class ProjectCreateResponse(BaseModel):
    id: int
    name: str
