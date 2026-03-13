from sqlalchemy import Column, String, Integer, Text, Boolean, Date, DateTime
from sqlalchemy.sql import func
from app.config.database import Base


class AboutModel(Base):
    __tablename__ = "about"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    title = Column(String(255), nullable=True)
    bio = Column(Text, nullable=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    location = Column(String(255), nullable=True)
    profile_image = Column(String(500), nullable=True)
    resume_url = Column(String(500), nullable=True)
    github_url = Column(String(500), nullable=True)
    linkedin_url = Column(String(500), nullable=True)
    twitter_url = Column(String(500), nullable=True)


class ContactModel(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    subject = Column(String(500), nullable=True)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    read = Column(Boolean, default=False)
    file = Column(Text, nullable=True)  # Stored as base64
    file_name = Column(String(255), nullable=True)


class ExperienceModel(Base):
    __tablename__ = "experiences"
    
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(255), nullable=True)
    position = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    current = Column(Boolean, default=False)
    location = Column(String(255), nullable=True)
    achievements = Column(Text, nullable=True)  # Stored as JSON string


class ProjectModel(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=True)
    github_link = Column(String(500), nullable=True)
    live_link = Column(String(500), nullable=True)
    technologies = Column(Text, nullable=True)  # Stored as JSON string
    category = Column(String(100), nullable=True)
    completed_date = Column(Date, nullable=True)
    featured = Column(Boolean, default=False)


class SkillModel(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=True)
    category = Column(String(100), nullable=True)
    proficiency = Column(Integer, nullable=True)
    icon_url = Column(String(500), nullable=True)
    years_of_experience = Column(Integer, nullable=True)

