from pydantic import BaseModel, Field, ConfigDict, field_serializer
from typing import Optional, List
from datetime import date


class Project(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(x.split('_')))
    )
    
    id: Optional[str] = Field(None, alias="id")
    title: str
    description: Optional[str] = None
    imageUrl: Optional[str] = Field(None, alias="imageUrl")
    githubLink: Optional[str] = Field(None, alias="githubLink")
    liveLink: Optional[str] = Field(None, alias="liveLink")
    technologies: Optional[List[str]] = Field(None, alias="technologies")
    category: Optional[str] = Field(None, alias="category")
    completedDate: Optional[date] = Field(None, alias="completedDate")
    featured: bool = Field(False, alias="featured")

    @field_serializer('imageUrl')
    def serialize_image_url(self, value: Optional[str]) -> Optional[str]:
        return value

    @field_serializer('githubLink')
    def serialize_github_link(self, value: Optional[str]) -> Optional[str]:
        return value

    @field_serializer('liveLink')
    def serialize_live_link(self, value: Optional[str]) -> Optional[str]:
        return value

    @field_serializer('completedDate')
    def serialize_completed_date(self, value: Optional[date]) -> Optional[str]:
        return value.isoformat() if value else None


class ProjectCreate(BaseModel):
    title: str
    description: Optional[str] = None
    imageUrl: Optional[str] = None
    githubLink: Optional[str] = None
    liveLink: Optional[str] = None
    technologies: Optional[List[str]] = None
    category: Optional[str] = None
    completedDate: Optional[date] = None
    featured: bool = False


class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    imageUrl: Optional[str] = None
    githubLink: Optional[str] = None
    liveLink: Optional[str] = None
    technologies: Optional[List[str]] = None
    category: Optional[str] = None
    completedDate: Optional[date] = None
    featured: Optional[bool] = None
