from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import json
from app.models.sql_models import ContactModel
from app.models.contact import Contact, ContactCreate


class ContactRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[Contact]:
        result = await self.db.execute(select(ContactModel).order_by(ContactModel.created_at.desc()))
        documents = result.scalars().all()
        return [self._model_to_contact(doc) for doc in documents]

    async def get_unread(self) -> List[Contact]:
        result = await self.db.execute(select(ContactModel).where(ContactModel.read == False).order_by(ContactModel.created_at.desc()))
        documents = result.scalars().all()
        return [self._model_to_contact(doc) for doc in documents]

    async def get_by_id(self, id: int) -> Optional[Contact]:
        result = await self.db.execute(select(ContactModel).where(ContactModel.id == id))
        document = result.scalar_one_or_none()
        return self._model_to_contact(document) if document else None

    async def create(self, contact_data: ContactCreate, file_data: Optional[bytes] = None, file_name: Optional[str] = None) -> Contact:
        # Convert camelCase to snake_case for database
        db_data = {
            'name': contact_data.name,
            'email': contact_data.email,
            'subject': contact_data.subject,
            'message': contact_data.message,
            'created_at': datetime.now(),
            'read': False,
            'file': file_data.hex() if file_data else None,
            'file_name': file_name or contact_data.fileName
        }
        
        document = ContactModel(**db_data)
        self.db.add(document)
        await self.db.commit()
        await self.db.refresh(document)
        return self._model_to_contact(document)

    async def mark_as_read(self, id: int) -> Optional[Contact]:
        result = await self.db.execute(select(ContactModel).where(ContactModel.id == id))
        document = result.scalar_one_or_none()
        if not document:
            return None
        
        document.read = True
        await self.db.commit()
        await self.db.refresh(document)
        return self._model_to_contact(document)

    async def delete(self, id: int) -> bool:
        result = await self.db.execute(select(ContactModel).where(ContactModel.id == id))
        document = result.scalar_one_or_none()
        if not document:
            return False
        
        await self.db.delete(document)
        await self.db.commit()
        return True

    def _model_to_contact(self, document: ContactModel) -> Contact:
        if document:
            return Contact(
                id=str(document.id),
                name=document.name,
                email=document.email,
                subject=document.subject,
                message=document.message,
                createdAt=document.created_at,
                read=document.read,
                file=bytes.fromhex(document.file) if document.file else None,
                fileName=document.file_name
            )
        return None

