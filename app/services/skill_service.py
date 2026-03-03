from typing import List, Optional
from app.models.skill import Skill, SkillCreate, SkillUpdate
from app.repositories.skill_repository import SkillRepository


class SkillService:
    def __init__(self):
        self.repository = SkillRepository()

    async def get_all(self) -> List[Skill]:
        return await self.repository.get_all()

    async def get_by_id(self, id: str) -> Optional[Skill]:
        return await self.repository.get_by_id(id)

    async def get_by_category(self, category: str) -> List[Skill]:
        return await self.repository.get_by_category(category)

    async def create(self, skill_data: SkillCreate) -> Skill:
        return await self.repository.create(skill_data)

    async def update(self, id: str, skill_data: SkillUpdate) -> Optional[Skill]:
        return await self.repository.update(id, skill_data)

    async def delete(self, id: str) -> bool:
        return await self.repository.delete(id)

