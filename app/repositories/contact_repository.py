from typing import List, Optional
from bson import ObjectId
from datetime import datetime
from app.config.database import get_database
from app.models.contact import Contact, ContactCreate


class ContactRepository:
    def __init__(self):
        self.collection = get_database()["contacts"]

    async def get_all(self) -> List[Contact]:
        documents = await self.collection.find().to_list(length=100)
        return [self._document_to_contact(doc) for doc in documents]

    async def get_unread(self) -> List[Contact]:
        documents = await self.collection.find({"read": False}).to_list(length=100)
        return [self._document_to_contact(doc) for doc in documents]

    async def get_by_id(self, id: str) -> Optional[Contact]:
        try:
            document = await self.collection.find_one({"_id": ObjectId(id)})
            return self._document_to_contact(document) if document else None
        except Exception:
            return None

    async def create(self, contact_data: ContactCreate, file_data: Optional[bytes] = None, file_name: Optional[str] = None) -> Contact:
        document = contact_data.model_dump(exclude_none=True)
        document["created_at"] = datetime.now()
        document["read"] = False
        
        if file_data:
            document["file"] = file_data
        if file_name:
            document["file_name"] = file_name
            
        result = await self.collection.insert_one(document)
        document["_id"] = result.inserted_id
        return self._document_to_contact(document)

    async def mark_as_read(self, id: str) -> Optional[Contact]:
        try:
            await self.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"read": True}}
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

    def _document_to_contact(self, document: dict) -> Contact:
        if document:
            document["id"] = str(document.pop("_id"))
            if isinstance(document.get("created_at"), datetime):
                document["created_at"] = document["created_at"].isoformat()
        return Contact(**document)

