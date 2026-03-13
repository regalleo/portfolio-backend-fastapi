from pydantic import BaseModel, Field, ConfigDict, field_serializer
from typing import Optional, List
from datetime import date


class Experience(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(x.split('_')))
    )
    
    id: Optional[str] = Field(None, alias="id")
    company: Optional[str] = Field(None, alias="company")
    position: Optional[str] = Field(None, alias="position")
    description: Optional[str] = Field(None, alias="description")
    startDate: Optional[date] = Field(None, alias="startDate")
    endDate: Optional[date] = Field(None, alias="endDate")
    current: bool = Field(False, alias="current")
    location: Optional[str] = Field(None, alias="location")
    achievements: Optional[List[str]] = Field(None, alias="achievements")

    @field_serializer('startDate')
    def serialize_start_date(self, value: Optional[date]) -> Optional[str]:
        return value.isoformat() if value else None

    @field_serializer('endDate')
    def serialize_end_date(self, value: Optional[date]) -> Optional[str]:
        return value.isoformat() if value else None


class ExperienceCreate(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    description: Optional[str] = None
    startDate: Optional[date] = None
    endDate: Optional[date] = None
    current: bool = False
    location: Optional[str] = None
    achievements: Optional[List[str]] = None


class ExperienceUpdate(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    description: Optional[str] = None
    startDate: Optional[date] = None
    endDate: Optional[date] = None
    current: Optional[bool] = None
    location: Optional[str] = None
    achievements: Optional[List[str]] = None
