from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.skill import Skill, SkillCreate, SkillUpdate
from app.services.skill_service import SkillService
from app.config.database import get_db

router = APIRouter()


def get_skill_service(db: AsyncSession = Depends(get_db)) -> SkillService:
    return SkillService(db)


@router.get("/", response_model=List[Skill])
async def get_all_skills(service: SkillService = Depends(get_skill_service)):
    """Get all skills"""
    return await service.get_all()


@router.get("/{id}", response_model=Skill)
async def get_skill_by_id(id: int, service: SkillService = Depends(get_skill_service)):
    """Get skill by ID"""
    skill = await service.get_by_id(id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill


@router.get("/category/{category}", response_model=List[Skill])
async def get_skills_by_category(category: str, service: SkillService = Depends(get_skill_service)):
    """Get skills by category"""
    return await service.get_by_category(category)


@router.post("/", response_model=Skill, status_code=status.HTTP_201_CREATED)
async def create_skill(skill: SkillCreate, service: SkillService = Depends(get_skill_service)):
    """Create new skill"""
    return await service.create(skill)


@router.put("/{id}", response_model=Skill)
async def update_skill(id: int, skill: SkillUpdate, service: SkillService = Depends(get_skill_service)):
    """Update skill"""
    updated = await service.update(id, skill)
    if not updated:
        raise HTTPException(status_code=404, detail="Skill not found")
    return updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_skill(id: int, service: SkillService = Depends(get_skill_service)):
    """Delete skill"""
    deleted = await service.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Skill not found")

