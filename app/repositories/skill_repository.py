from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.sql_models import SkillModel
from app.models.skill import Skill, SkillCreate, SkillUpdate


class SkillRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[Skill]:
        result = await self.db.execute(select(SkillModel))
        documents = result.scalars().all()
        return [self._model_to_skill(doc) for doc in documents]

    async def get_by_id(self, id: int) -> Optional[Skill]:
        result = await self.db.execute(select(SkillModel).where(SkillModel.id == id))
        document = result.scalar_one_or_none()
        return self._model_to_skill(document) if document else None

    async def get_by_category(self, category: str) -> List[Skill]:
        result = await self.db.execute(select(SkillModel).where(SkillModel.category == category))
        documents = result.scalars().all()
        return [self._model_to_skill(doc) for doc in documents]

    async def create(self, skill_data: SkillCreate) -> Skill:
        data = skill_data.model_dump(exclude_none=True)
        # Convert camelCase to snake_case for database
        db_data = {}
        for key, value in data.items():
            snake_key = ''.join(['_' + c.lower() if c.isupper() else c for c in key])
            snake_key = snake_key.lstrip('_')
            db_data[snake_key] = value
        
        document = SkillModel(**db_data)
        self.db.add(document)
        await self.db.commit()
        await self.db.refresh(document)
        return self._model_to_skill(document)

    async def update(self, id: int, skill_data: SkillUpdate) -> Optional[Skill]:
        result = await self.db.execute(select(SkillModel).where(SkillModel.id == id))
        document = result.scalar_one_or_none()
        if not document:
            return None
        
        update_data = {k: v for k, v in skill_data.model_dump(exclude_none=True).items() if v is not None}
        # Convert camelCase to snake_case for database
        db_data = {}
        for key, value in update_data.items():
            snake_key = ''.join(['_' + c.lower() if c.isupper() else c for c in key])
            snake_key = snake_key.lstrip('_')
            db_data[snake_key] = value
        
        for key, value in db_data.items():
            setattr(document, key, value)
        
        await self.db.commit()
        await self.db.refresh(document)
        return self._model_to_skill(document)

    async def delete(self, id: int) -> bool:
        result = await self.db.execute(select(SkillModel).where(SkillModel.id == id))
        document = result.scalar_one_or_none()
        if not document:
            return False
        
        await self.db.delete(document)
        await self.db.commit()
        return True

    def _model_to_skill(self, document: SkillModel) -> Skill:
        if document:
            return Skill(
                id=str(document.id),
                name=document.name,
                category=document.category,
                proficiency=document.proficiency,
                iconUrl=document.icon_url,
                yearsOfExperience=document.years_of_experience
            )
        return None

