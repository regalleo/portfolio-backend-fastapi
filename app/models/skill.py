from pydantic import BaseModel, Field
from typing import Optional


class Skill(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: Optional[str] = None
    category: Optional[str] = None
    proficiency: Optional[int] = None
    icon_url: Optional[str] = None
    years_of_experience: Optional[int] = None

    class Config:
        populate_by_name = True


class SkillCreate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    proficiency: Optional[int] = None
    icon_url: Optional[str] = None
    years_of_experience: Optional[int] = None


class SkillUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    proficiency: Optional[int] = None
    icon_url: Optional[str] = None
    years_of_experience: Optional[int] = None

