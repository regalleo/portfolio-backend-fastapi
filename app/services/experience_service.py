from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.experience import Experience, ExperienceCreate, ExperienceUpdate
from app.repositories.experience_repository import ExperienceRepository


class ExperienceService:
    def __init__(self, db: AsyncSession):
        self.repository = ExperienceRepository(db)

    async def get_all(self) -> List[Experience]:
        return await self.repository.get_all()

    async def get_by_id(self, id: int) -> Optional[Experience]:
        return await self.repository.get_by_id(id)

    async def create(self, experience_data: ExperienceCreate) -> Experience:
        return await self.repository.create(experience_data)

    async def update(self, id: int, experience_data: ExperienceUpdate) -> Optional[Experience]:
        return await self.repository.update(id, experience_data)

    async def delete(self, id: int) -> bool:
        return await self.repository.delete(id)

