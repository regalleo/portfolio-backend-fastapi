from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.about import About, AboutCreate, AboutUpdate
from app.services.about_service import AboutService
from app.config.database import get_db

router = APIRouter()


def get_about_service(db: AsyncSession = Depends(get_db)) -> AboutService:
    return AboutService(db)


@router.get("/", response_model=List[About])
async def get_all_about(service: AboutService = Depends(get_about_service)):
    """Get all about entries"""
    return await service.get_all()


@router.get("/primary", response_model=About)
async def get_primary_about(service: AboutService = Depends(get_about_service)):
    """Get primary about entry"""
    about = await service.get_primary()
    if not about:
        raise HTTPException(status_code=404, detail="About not found")
    return about


@router.get("/{id}", response_model=About)
async def get_about_by_id(id: int, service: AboutService = Depends(get_about_service)):
    """Get about by ID"""
    about = await service.get_by_id(id)
    if not about:
        raise HTTPException(status_code=404, detail="About not found")
    return about


@router.post("/", response_model=About, status_code=status.HTTP_201_CREATED)
async def create_about(about: AboutCreate, service: AboutService = Depends(get_about_service)):
    """Create new about entry"""
    return await service.create(about)


@router.put("/{id}", response_model=About)
async def update_about(id: int, about: AboutUpdate, service: AboutService = Depends(get_about_service)):
    """Update about entry"""
    updated = await service.update(id, about)
    if not updated:
        raise HTTPException(status_code=404, detail="About not found")
    return updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_about(id: int, service: AboutService = Depends(get_about_service)):
    """Delete about entry"""
    deleted = await service.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="About not found")

