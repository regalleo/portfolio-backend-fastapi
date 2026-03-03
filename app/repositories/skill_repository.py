from typing import List, Optional
from bson import ObjectId
from app.config.database import get_database
from app.models.skill import Skill, SkillCreate, SkillUpdate


class SkillRepository:
    def __init__(self):
        self.collection = get_database()["skills"]

    async def get_all(self) -> List[Skill]:
        documents = await self.collection.find().to_list(length=100)
        return [self._document_to_skill(doc) for doc in documents]

    async def get_by_id(self, id: str) -> Optional[Skill]:
        try:
            document = await self.collection.find_one({"_id": ObjectId(id)})
            return self._document_to_skill(document) if document else None
        except Exception:
            return None

    async def get_by_category(self, category: str) -> List[Skill]:
        documents = await self.collection.find({"category": category}).to_list(length=100)
        return [self._document_to_skill(doc) for doc in documents]

    async def create(self, skill_data: SkillCreate) -> Skill:
        document = skill_data.model_dump(exclude_none=True)
        result = await self.collection.insert_one(document)
        document["_id"] = result.inserted_id
        return self._document_to_skill(document)

    async def update(self, id: str, skill_data: SkillUpdate) -> Optional[Skill]:
        try:
            update_data = {k: v for k, v in skill_data.model_dump(exclude_none=True).items() if v is not None}
            if not update_data:
                return await self.get_by_id(id)
            
            await self.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": update_data}
            )
            return await self.get_by_id(id)
        except Exception:
            return None

    async def delete(self, id: str) -> bool:
        try:
            result = await self.collection.delete_one({"_id": ObjectId(id)})
            return result.deleted_count > 0
        except Exception:
            return False

    def _document_to_skill(self, document: dict) -> Skill:
        if document:
            document["id"] = str(document.pop("_id"))
        return Skill(**document)

