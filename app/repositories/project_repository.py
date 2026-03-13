from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
import json
from app.models.sql_models import ProjectModel
from app.models.project import Project, ProjectCreate, ProjectUpdate


class ProjectRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[Project]:
        result = await self.db.execute(select(ProjectModel))
        documents = result.scalars().all()
        return [self._model_to_project(doc) for doc in documents]

    async def get_by_id(self, id: int) -> Optional[Project]:
        result = await self.db.execute(select(ProjectModel).where(ProjectModel.id == id))
        document = result.scalar_one_or_none()
        return self._model_to_project(document) if document else None

    async def get_by_category(self, category: str) -> List[Project]:
        result = await self.db.execute(select(ProjectModel).where(ProjectModel.category == category))
        documents = result.scalars().all()
        return [self._model_to_project(doc) for doc in documents]

    async def get_featured(self) -> List[Project]:
        result = await self.db.execute(select(ProjectModel).where(ProjectModel.featured == True))
        documents = result.scalars().all()
        return [self._model_to_project(doc) for doc in documents]

    async def create(self, project_data: ProjectCreate) -> Project:
        data = project_data.model_dump(exclude_none=True)
        # Convert camelCase to snake_case for database
        db_data = {}
        for key, value in data.items():
            snake_key = ''.join(['_' + c.lower() if c.isupper() else c for c in key])
            snake_key = snake_key.lstrip('_')
            if key == 'technologies':
                db_data[snake_key] = json.dumps(value)
            else:
                db_data[snake_key] = value
        
        document = ProjectModel(**db_data)
        self.db.add(document)
        await self.db.commit()
        await self.db.refresh(document)
        return self._model_to_project(document)

    async def update(self, id: int, project_data: ProjectUpdate) -> Optional[Project]:
        result = await self.db.execute(select(ProjectModel).where(ProjectModel.id == id))
        document = result.scalar_one_or_none()
        if not document:
            return None
        
        update_data = {k: v for k, v in project_data.model_dump(exclude_none=True).items() if v is not None}
        # Convert camelCase to snake_case for database
        db_data = {}
        for key, value in update_data.items():
            snake_key = ''.join(['_' + c.lower() if c.isupper() else c for c in key])
            snake_key = snake_key.lstrip('_')
            if key == 'technologies':
                db_data[snake_key] = json.dumps(value)
            else:
                db_data[snake_key] = value
        
        for key, value in db_data.items():
            setattr(document, key, value)
        
        await self.db.commit()
        await self.db.refresh(document)
        return self._model_to_project(document)

    async def delete(self, id: int) -> bool:
        result = await self.db.execute(select(ProjectModel).where(ProjectModel.id == id))
        document = result.scalar_one_or_none()
        if not document:
            return False
        
        await self.db.delete(document)
        await self.db.commit()
        return True

    def _model_to_project(self, document: ProjectModel) -> Project:
        if document:
            technologies_list = []
            if document.technologies:
                try:
                    technologies_list = json.loads(document.technologies)
                except:
                    technologies_list = []
            
            return Project(
                id=str(document.id),
                title=document.title,
                description=document.description,
                imageUrl=document.image_url,
                githubLink=document.github_link,
                liveLink=document.live_link,
                technologies=technologies_list,
                category=document.category,
                completedDate=document.completed_date,
                featured=document.featured
            )
        return None

