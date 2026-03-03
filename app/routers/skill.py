from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.skill import Skill, SkillCreate, SkillUpdate
from app.services.skill_service import SkillService

router = APIRouter()
skill_service = SkillService()


@router.get("/", response_model=List[Skill])
async def get_all_skills():
    """Get all skills"""
    return await skill_service.get_all()


@router.get("/{id}", response_model=Skill)
async def get_skill_by_id(id: str):
    """Get skill by ID"""
    skill = await skill_service.get_by_id(id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill


@router.get("/category/{category}", response_model=List[Skill])
async def get_skills_by_category(category: str):
    """Get skills by category"""
    return await skill_service.get_by_category(category)


@router.post("/", response_model=Skill, status_code=status.HTTP_201_CREATED)
async def create_skill(skill: SkillCreate):
    """Create new skill"""
    return await skill_service.create(skill)


@router.put("/{id}", response_model=Skill)
async def update_skill(id: str, skill: SkillUpdate):
    """Update skill"""
    updated = await skill_service.update(id, skill)
    if not updated:
        raise HTTPException(status_code=404, detail="Skill not found")
    return updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_skill(id: str):
    """Delete skill"""
    deleted = await skill_service.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Skill not found")

