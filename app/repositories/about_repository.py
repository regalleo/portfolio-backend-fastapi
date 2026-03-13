from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.models.sql_models import AboutModel
from app.models.about import About, AboutCreate, AboutUpdate


class AboutRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[About]:
        result = await self.db.execute(select(AboutModel))
        documents = result.scalars().all()
        return [self._model_to_about(doc) for doc in documents]

    async def get_by_id(self, id: int) -> Optional[About]:
        result = await self.db.execute(select(AboutModel).where(AboutModel.id == id))
        document = result.scalar_one_or_none()
        return self._model_to_about(document) if document else None

    async def get_primary(self) -> Optional[About]:
        result = await self.db.execute(select(AboutModel).limit(1))
        document = result.scalar_one_or_none()
        return self._model_to_about(document) if document else None

    async def create(self, about_data: AboutCreate) -> About:
        data = about_data.model_dump(exclude_none=True)
        # Convert camelCase to snake_case for database
        db_data = {}
        for key, value in data.items():
            snake_key = ''.join(['_' + c.lower() if c.isupper() else c for c in key])
            snake_key = snake_key.lstrip('_')
            db_data[snake_key] = value
        
        document = AboutModel(**db_data)
        self.db.add(document)
        await self.db.commit()
        await self.db.refresh(document)
        return self._model_to_about(document)

    async def update(self, id: int, about_data: AboutUpdate) -> Optional[About]:
        result = await self.db.execute(select(AboutModel).where(AboutModel.id == id))
        document = result.scalar_one_or_none()
        if not document:
            return None
        
        update_data = {k: v for k, v in about_data.model_dump(exclude_none=True).items() if v is not None}
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
        return self._model_to_about(document)

    async def delete(self, id: int) -> bool:
        result = await self.db.execute(select(AboutModel).where(AboutModel.id == id))
        document = result.scalar_one_or_none()
        if not document:
            return False
        
        await self.db.delete(document)
        await self.db.commit()
        return True

    def _model_to_about(self, document: AboutModel) -> About:
        if document:
            return About(
                id=str(document.id),
                name=document.name,
                title=document.title,
                bio=document.bio,
                email=document.email,
                phone=document.phone,
                location=document.location,
                profileImage=document.profile_image,
                resumeUrl=document.resume_url,
                githubUrl=document.github_url,
                linkedinUrl=document.linkedin_url,
                twitterUrl=document.twitter_url
            )
        return None

