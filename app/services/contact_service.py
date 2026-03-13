from typing import List, Optional
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.contact import Contact, ContactCreate
from app.repositories.contact_repository import ContactRepository
from app.services.email_service import EmailService

logger = logging.getLogger(__name__)


class ContactService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactRepository(db)
        self.email_service = EmailService()

    async def create(self, contact_data: ContactCreate, file_data: Optional[bytes] = None, file_name: Optional[str] = None) -> Contact:
        try:
            contact = await self.repository.create(contact_data, file_data, file_name)
            logger.info(f"✅ Contact saved: {contact_data.name}")
            
            # Send email asynchronously
            await self.email_service.send_contact_email_with_attachment(contact)
            
            return contact
        except Exception as e:
            logger.error(f"❌ Error creating contact: {e}")
            raise

    async def get_all(self) -> List[Contact]:
        return await self.repository.get_all()

    async def get_unread(self) -> List[Contact]:
        return await self.repository.get_unread()

    async def get_by_id(self, id: int) -> Optional[Contact]:
        return await self.repository.get_by_id(id)

    async def mark_as_read(self, id: int) -> Optional[Contact]:
        return await self.repository.mark_as_read(id)

    async def delete(self, id: int) -> bool:
        return await self.repository.delete(id)

