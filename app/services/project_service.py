from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.project import Project, ProjectCreate, ProjectUpdate
from app.repositories.project_repository import ProjectRepository


class ProjectService:
    def __init__(self, db: AsyncSession):
        self.repository = ProjectRepository(db)

    async def get_all(self) -> List[Project]:
        return await self.repository.get_all()

    async def get_by_id(self, id: int) -> Optional[Project]:
        return await self.repository.get_by_id(id)

    async def get_by_category(self, category: str) -> List[Project]:
        return await self.repository.get_by_category(category)

    async def get_featured(self) -> List[Project]:
        return await self.repository.get_featured()

    async def create(self, project_data: ProjectCreate) -> Project:
        return await self.repository.create(project_data)

    async def update(self, id: int, project_data: ProjectUpdate) -> Optional[Project]:
        return await self.repository.update(id, project_data)

    async def delete(self, id: int) -> bool:
        return await self.repository.delete(id)

