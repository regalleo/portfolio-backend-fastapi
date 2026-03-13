from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.skill import Skill, SkillCreate, SkillUpdate
from app.repositories.skill_repository import SkillRepository


class SkillService:
    def __init__(self, db: AsyncSession):
        self.repository = SkillRepository(db)

    async def get_all(self) -> List[Skill]:
        return await self.repository.get_all()

    async def get_by_id(self, id: int) -> Optional[Skill]:
        return await self.repository.get_by_id(id)

    async def get_by_category(self, category: str) -> List[Skill]:
        return await self.repository.get_by_category(category)

    async def create(self, skill_data: SkillCreate) -> Skill:
        return await self.repository.create(skill_data)

    async def update(self, id: int, skill_data: SkillUpdate) -> Optional[Skill]:
        return await self.repository.update(id, skill_data)

    async def delete(self, id: int) -> bool:
        return await self.repository.delete(id)

