from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class About(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(x.split('_')))
    )
    
    id: Optional[str] = Field(None, alias="id")
    name: Optional[str] = Field(None, alias="name")
    title: Optional[str] = Field(None, alias="title")
    bio: Optional[str] = Field(None, alias="bio")
    email: Optional[str] = Field(None, alias="email")
    phone: Optional[str] = Field(None, alias="phone")
    location: Optional[str] = Field(None, alias="location")
    profileImage: Optional[str] = Field(None, alias="profileImage")
    resumeUrl: Optional[str] = Field(None, alias="resumeUrl")
    githubUrl: Optional[str] = Field(None, alias="githubUrl")
    linkedinUrl: Optional[str] = Field(None, alias="linkedinUrl")
    twitterUrl: Optional[str] = Field(None, alias="twitterUrl")


class AboutCreate(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    bio: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    profileImage: Optional[str] = None
    resumeUrl: Optional[str] = None
    githubUrl: Optional[str] = None
    linkedinUrl: Optional[str] = None
    twitterUrl: Optional[str] = None


class AboutUpdate(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    bio: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    profileImage: Optional[str] = None
    resumeUrl: Optional[str] = None
    githubUrl: Optional[str] = None
    linkedinUrl: Optional[str] = None
    twitterUrl: Optional[str] = None
