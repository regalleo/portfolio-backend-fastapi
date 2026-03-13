from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_serializer
from typing import Optional, List
from datetime import datetime


class Contact(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(x.split('_')))
    )
    
    id: Optional[str] = Field(None, alias="id")
    name: str = Field(..., alias="name")
    email: EmailStr = Field(..., alias="email")
    subject: Optional[str] = Field(None, alias="subject")
    message: str = Field(..., alias="message")
    createdAt: datetime = Field(default_factory=datetime.now, alias="createdAt")
    read: bool = Field(False, alias="read")
    file: Optional[bytes] = Field(None, alias="file")
    fileName: Optional[str] = Field(None, alias="fileName")

    @field_serializer('createdAt')
    def serialize_created_at(self, value: datetime) -> str:
        return value.isoformat() if value else None

    @field_serializer('file')
    def serialize_file(self, value: Optional[bytes]) -> Optional[str]:
        return value.hex() if value else None


class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    subject: Optional[str] = None
    message: str
    fileName: Optional[str] = None


class InterestRequest(BaseModel):
    email: EmailStr
