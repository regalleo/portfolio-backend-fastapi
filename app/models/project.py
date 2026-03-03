from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class Project(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    github_link: Optional[str] = None
    live_link: Optional[str] = None
    technologies: Optional[List[str]] = None
    category: Optional[str] = None
    completed_date: Optional[date] = None
    featured: bool = False

    class Config:
        populate_by_name = True
        json_encoders = {date: lambda v: v.isoformat() if v else None}


class ProjectCreate(BaseModel):
    title: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    github_link: Optional[str] = None
    live_link: Optional[str] = None
    technologies: Optional[List[str]] = None
    category: Optional[str] = None
    completed_date: Optional[date] = None
    featured: bool = False


class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    github_link: Optional[str] = None
    live_link: Optional[str] = None
    technologies: Optional[List[str]] = None
    category: Optional[str] = None
    completed_date: Optional[date] = None
    featured: bool = False

