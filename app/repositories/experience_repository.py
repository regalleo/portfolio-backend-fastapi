from typing import List, Optional
from bson import ObjectId
from app.config.database import get_database
from app.models.experience import Experience, ExperienceCreate, ExperienceUpdate


class ExperienceRepository:
    def __init__(self):
        self.collection = get_database()["experiences"]

    async def get_all(self) -> List[Experience]:
        documents = await self.collection.find().sort("start_date", -1).to_list(length=100)
        return [self._document_to_experience(doc) for doc in documents]

    async def get_by_id(self, id: str) -> Optional[Experience]:
        try:
            document = await self.collection.find_one({"_id": ObjectId(id)})
            return self._document_to_experience(document) if document else None
        except Exception:
            return None

    async def create(self, experience_data: ExperienceCreate) -> Experience:
        document = experience_data.model_dump(exclude_none=True)
        result = await self.collection.insert_one(document)
        document["_id"] = result.inserted_id
        return self._document_to_experience(document)

    async def update(self, id: str, experience_data: ExperienceUpdate) -> Optional[Experience]:
        try:
            update_data = {k: v for k, v in experience_data.model_dump(exclude_none=True).items() if v is not None}
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

    def _document_to_experience(self, document: dict) -> Experience:
        if document:
            document["id"] = str(document.pop("_id"))
            if document.get("start_date"):
                document["start_date"] = str(document["start_date"])
            if document.get("end_date"):
                document["end_date"] = str(document["end_date"])
        return Experience(**document)

