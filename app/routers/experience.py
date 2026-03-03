from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response
from typing import List
import json
from app.models.experience import Experience, ExperienceCreate, ExperienceUpdate
from app.services.experience_service import ExperienceService

router = APIRouter()
experience_service = ExperienceService()


@router.get("/", response_model=List[Experience])
async def get_all_experiences():
    """Get all experiences"""
    print("=== GET /api/experience CALLED ===")
    experiences = await experience_service.get_all()
    print(f"Found {len(experiences)} experiences")
    for e in experiences:
        print(f"  - {e.company}")
    return experiences


# Alternative route with cache control headers
@router.get("/nocache", response_model=List[Experience])
async def get_all_experiences_no_cache():
    """Get all experiences with no cache headers"""
    experiences = await experience_service.get_all()
    return Response(
        content=experiences.model_dump_json(),
        media_type="application/json",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
    )


@router.get("/{id}", response_model=Experience)
async def get_experience_by_id(id: str):
    """Get experience by ID"""
    experience = await experience_service.get_by_id(id)
    if not experience:
        raise HTTPException(status_code=404, detail="Experience not found")
    return experience


@router.post("/", response_model=Experience, status_code=status.HTTP_201_CREATED)
async def create_experience(experience: ExperienceCreate):
    """Create new experience"""
    return await experience_service.create(experience)


@router.put("/{id}", response_model=Experience)
async def update_experience(id: str, experience: ExperienceUpdate):
    """Update experience"""
    updated = await experience_service.update(id, experience)
    if not updated:
        raise HTTPException(status_code=404, detail="Experience not found")
    return updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_experience(id: str):
    """Delete experience"""
    deleted = await experience_service.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Experience not found")

