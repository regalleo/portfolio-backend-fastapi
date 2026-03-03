from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


class Contact(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    email: EmailStr
    subject: Optional[str] = None
    message: str
    created_at: datetime = Field(default_factory=datetime.now)
    read: bool = False
    file: Optional[bytes] = None
    file_name: Optional[str] = None

    class Config:
        populate_by_name = True
        json_encoders = {bytes: lambda v: v.hex() if v else None}


class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    subject: Optional[str] = None
    message: str
    file_name: Optional[str] = None


class InterestRequest(BaseModel):
    email: EmailStr

