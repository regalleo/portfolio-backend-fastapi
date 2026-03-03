from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.project import Project, ProjectCreate, ProjectUpdate
from app.services.project_service import ProjectService

router = APIRouter()
project_service = ProjectService()


@router.get("/", response_model=List[Project])
async def get_all_projects():
    """Get all projects"""
    return await project_service.get_all()


@router.get("/{id}", response_model=Project)
async def get_project_by_id(id: str):
    """Get project by ID"""
    project = await project_service.get_by_id(id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/category/{category}", response_model=List[Project])
async def get_projects_by_category(category: str):
    """Get projects by category"""
    return await project_service.get_by_category(category)


@router.get("/featured", response_model=List[Project])
async def get_featured_projects():
    """Get featured projects"""
    return await project_service.get_featured()


@router.post("/", response_model=Project, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate):
    """Create new project"""
    return await project_service.create(project)


@router.put("/{id}", response_model=Project)
async def update_project(id: str, project: ProjectUpdate):
    """Update project"""
    updated = await project_service.update(id, project)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(id: str):
    """Delete project"""
    deleted = await project_service.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")

