from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.about import About, AboutCreate, AboutUpdate
from app.repositories.about_repository import AboutRepository


class AboutService:
    def __init__(self, db: AsyncSession):
        self.repository = AboutRepository(db)

    async def get_all(self) -> List[About]:
        return await self.repository.get_all()

    async def get_by_id(self, id: int) -> Optional[About]:
        return await self.repository.get_by_id(id)

    async def get_primary(self) -> Optional[About]:
        return await self.repository.get_primary()

    async def create(self, about_data: AboutCreate) -> About:
        return await self.repository.create(about_data)

    async def update(self, id: int, about_data: AboutUpdate) -> Optional[About]:
        return await self.repository.update(id, about_data)

    async def delete(self, id: int) -> bool:
        return await self.repository.delete(id)

