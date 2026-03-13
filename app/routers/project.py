from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.project import Project, ProjectCreate, ProjectUpdate
from app.services.project_service import ProjectService
from app.config.database import get_db

router = APIRouter()


def get_project_service(db: AsyncSession = Depends(get_db)) -> ProjectService:
    return ProjectService(db)


@router.get("/", response_model=List[Project])
async def get_all_projects(service: ProjectService = Depends(get_project_service)):
    """Get all projects"""
    return await service.get_all()


@router.get("/{id}", response_model=Project)
async def get_project_by_id(id: int, service: ProjectService = Depends(get_project_service)):
    """Get project by ID"""
    project = await service.get_by_id(id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/category/{category}", response_model=List[Project])
async def get_projects_by_category(category: str, service: ProjectService = Depends(get_project_service)):
    """Get projects by category"""
    return await service.get_by_category(category)


@router.get("/featured", response_model=List[Project])
async def get_featured_projects(service: ProjectService = Depends(get_project_service)):
    """Get featured projects"""
    return await service.get_featured()


@router.post("/", response_model=Project, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate, service: ProjectService = Depends(get_project_service)):
    """Create new project"""
    return await service.create(project)


@router.put("/{id}", response_model=Project)
async def update_project(id: int, project: ProjectUpdate, service: ProjectService = Depends(get_project_service)):
    """Update project"""
    updated = await service.update(id, project)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(id: int, service: ProjectService = Depends(get_project_service)):
    """Delete project"""
    deleted = await service.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")

