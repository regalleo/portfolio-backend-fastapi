from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.experience import Experience, ExperienceCreate, ExperienceUpdate
from app.services.experience_service import ExperienceService
from app.config.database import get_db

router = APIRouter()


def get_experience_service(db: AsyncSession = Depends(get_db)) -> ExperienceService:
    return ExperienceService(db)


@router.get("/", response_model=List[Experience])
async def get_all_experiences(service: ExperienceService = Depends(get_experience_service)):
    """Get all experiences"""
    return await service.get_all()


@router.get("/{id}", response_model=Experience)
async def get_experience_by_id(id: int, service: ExperienceService = Depends(get_experience_service)):
    """Get experience by ID"""
    experience = await service.get_by_id(id)
    if not experience:
        raise HTTPException(status_code=404, detail="Experience not found")
    return experience


@router.post("/", response_model=Experience, status_code=status.HTTP_201_CREATED)
async def create_experience(experience: ExperienceCreate, service: ExperienceService = Depends(get_experience_service)):
    """Create new experience"""
    return await service.create(experience)


@router.put("/{id}", response_model=Experience)
async def update_experience(id: int, experience: ExperienceUpdate, service: ExperienceService = Depends(get_experience_service)):
    """Update experience"""
    updated = await service.update(id, experience)
    if not updated:
        raise HTTPException(status_code=404, detail="Experience not found")
    return updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_experience(id: int, service: ExperienceService = Depends(get_experience_service)):
    """Delete experience"""
    deleted = await service.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Experience not found")
