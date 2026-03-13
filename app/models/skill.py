from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class Skill(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(x.split('_')))
    )
    
    id: Optional[str] = Field(None, alias="id")
    name: Optional[str] = Field(None, alias="name")
    category: Optional[str] = Field(None, alias="category")
    proficiency: Optional[int] = Field(None, alias="proficiency")
    iconUrl: Optional[str] = Field(None, alias="iconUrl")
    yearsOfExperience: Optional[int] = Field(None, alias="yearsOfExperience")


class SkillCreate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    proficiency: Optional[int] = None
    iconUrl: Optional[str] = None
    yearsOfExperience: Optional[int] = None


class SkillUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    proficiency: Optional[int] = None
    iconUrl: Optional[str] = None
    yearsOfExperience: Optional[int] = None
