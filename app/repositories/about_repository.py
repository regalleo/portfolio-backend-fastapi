from typing import List, Optional
from bson import ObjectId
from app.config.database import get_database
from app.models.about import About, AboutCreate, AboutUpdate


class AboutRepository:
    def __init__(self):
        self.collection = get_database()["about"]

    async def get_all(self) -> List[About]:
        documents = await self.collection.find().to_list(length=100)
        return [self._document_to_about(doc) for doc in documents]

    async def get_by_id(self, id: str) -> Optional[About]:
        try:
            document = await self.collection.find_one({"_id": ObjectId(id)})
            return self._document_to_about(document) if document else None
        except Exception:
            return None

    async def get_primary(self) -> Optional[About]:
        document = await self.collection.find().first()
        return self._document_to_about(document) if document else None

    async def create(self, about_data: AboutCreate) -> About:
        document = about_data.model_dump(exclude_none=True)
        result = await self.collection.insert_one(document)
        document["_id"] = result.inserted_id
        return self._document_to_about(document)

    async def update(self, id: str, about_data: AboutUpdate) -> Optional[About]:
        try:
            update_data = {k: v for k, v in about_data.model_dump(exclude_none=True).items() if v is not None}
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

    def _document_to_about(self, document: dict) -> About:
        if document:
            document["id"] = str(document.pop("_id"))
        return About(**document)

