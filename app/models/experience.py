from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class Experience(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    company: Optional[str] = None
    position: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    current: bool = False
    location: Optional[str] = None
    achievements: Optional[List[str]] = None

    class Config:
        populate_by_name = True
        json_encoders = {date: lambda v: v.isoformat() if v else None}


class ExperienceCreate(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    current: bool = False
    location: Optional[str] = None
    achievements: Optional[List[str]] = None


class ExperienceUpdate(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    current: bool = False
    location: Optional[str] = None
    achievements: Optional[List[str]] = None

