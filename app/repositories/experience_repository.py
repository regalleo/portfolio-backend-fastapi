from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
import json
from app.models.sql_models import ExperienceModel
from app.models.experience import Experience, ExperienceCreate, ExperienceUpdate


class ExperienceRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[Experience]:
        result = await self.db.execute(select(ExperienceModel).order_by(ExperienceModel.start_date.desc()))
        documents = result.scalars().all()
        return [self._model_to_experience(doc) for doc in documents]

    async def get_by_id(self, id: int) -> Optional[Experience]:
        result = await self.db.execute(select(ExperienceModel).where(ExperienceModel.id == id))
        document = result.scalar_one_or_none()
        return self._model_to_experience(document) if document else None

    async def create(self, experience_data: ExperienceCreate) -> Experience:
        data = experience_data.model_dump(exclude_none=True)
        # Convert camelCase to snake_case for database
        db_data = {}
        for key, value in data.items():
            snake_key = ''.join(['_' + c.lower() if c.isupper() else c for c in key])
            snake_key = snake_key.lstrip('_')
            if key == 'achievements':
                db_data[snake_key] = json.dumps(value)
            else:
                db_data[snake_key] = value
        
        document = ExperienceModel(**db_data)
        self.db.add(document)
        await self.db.commit()
        await self.db.refresh(document)
        return self._model_to_experience(document)

    async def update(self, id: int, experience_data: ExperienceUpdate) -> Optional[Experience]:
        result = await self.db.execute(select(ExperienceModel).where(ExperienceModel.id == id))
        document = result.scalar_one_or_none()
        if not document:
            return None
        
        update_data = {k: v for k, v in experience_data.model_dump(exclude_none=True).items() if v is not None}
        # Convert camelCase to snake_case for database
        db_data = {}
        for key, value in update_data.items():
            snake_key = ''.join(['_' + c.lower() if c.isupper() else c for c in key])
            snake_key = snake_key.lstrip('_')
            if key == 'achievements':
                db_data[snake_key] = json.dumps(value)
            else:
                db_data[snake_key] = value
        
        for key, value in db_data.items():
            setattr(document, key, value)
        
        await self.db.commit()
        await self.db.refresh(document)
        return self._model_to_experience(document)

    async def delete(self, id: int) -> bool:
        result = await self.db.execute(select(ExperienceModel).where(ExperienceModel.id == id))
        document = result.scalar_one_or_none()
        if not document:
            return False
        
        await self.db.delete(document)
        await self.db.commit()
        return True

    def _model_to_experience(self, document: ExperienceModel) -> Experience:
        if document:
            achievements_list = []
            if document.achievements:
                try:
                    achievements_list = json.loads(document.achievements)
                except:
                    achievements_list = []
            
            return Experience(
                id=str(document.id),
                company=document.company,
                position=document.position,
                description=document.description,
                startDate=document.start_date,
                endDate=document.end_date,
                current=document.current,
                location=document.location,
                achievements=achievements_list
            )
        return None

