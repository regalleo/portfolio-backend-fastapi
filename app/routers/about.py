from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.about import About, AboutCreate, AboutUpdate
from app.services.about_service import AboutService

router = APIRouter()
about_service = AboutService()


@router.get("/", response_model=List[About])
async def get_all_about():
    """Get all about entries"""
    return await about_service.get_all()


@router.get("/primary", response_model=About)
async def get_primary_about():
    """Get primary about entry"""
    about = await about_service.get_primary()
    if not about:
        raise HTTPException(status_code=404, detail="About not found")
    return about


@router.get("/{id}", response_model=About)
async def get_about_by_id(id: str):
    """Get about by ID"""
    about = await about_service.get_by_id(id)
    if not about:
        raise HTTPException(status_code=404, detail="About not found")
    return about


@router.post("/", response_model=About, status_code=status.HTTP_201_CREATED)
async def create_about(about: AboutCreate):
    """Create new about entry"""
    return await about_service.create(about)


@router.put("/{id}", response_model=About)
async def update_about(id: str, about: AboutUpdate):
    """Update about entry"""
    updated = await about_service.update(id, about)
    if not updated:
        raise HTTPException(status_code=404, detail="About not found")
    return updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_about(id: str):
    """Delete about entry"""
    deleted = await about_service.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="About not found")

