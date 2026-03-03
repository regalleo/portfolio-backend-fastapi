from fastapi import APIRouter, HTTPException, status, File, UploadFile, Form
from typing import List, Optional
import asyncio
from app.models.contact import Contact, ContactCreate, InterestRequest
from app.services.contact_service import ContactService
from app.services.email_service import EmailService

router = APIRouter()
contact_service = ContactService()
email_service = EmailService()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def submit_contact(
    name: str = Form(...),
    email: str = Form(...),
    subject: Optional[str] = Form(None),
    message: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    """Submit contact form with optional file upload"""
    try:
        contact_data = ContactCreate(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        file_data = None
        file_name = None
        
        if file and file.filename:
            file_data = await file.read()
            file_name = file.filename
        
        contact = await contact_service.create(contact_data, file_data, file_name)
        
        # Send confirmation emails (fire and forget)
        asyncio.create_task(email_service.send_contact_email_with_attachment(contact))
        
        return {
            "success": True,
            "message": "Thank you! Your message has been received."
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "success": False,
            "message": "Failed to send message. Please try again."
        }



@router.post("/interest")
async def send_interest_email(request: InterestRequest):
    """Send interest email"""
    try:
        if not request.email or not request.email.strip():
            return {
                "success": False,
                "message": "Email is required"
            }
        
        await email_service.send_interest_email_async(request.email)
        
        return {
            "success": True,
            "message": "Thank you for your interest! Check your email for confirmation."
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "success": False,
            "message": "Failed to process your request. Please try again."
        }, status.HTTP_500_INTERNAL_SERVER_ERROR


@router.get("/", response_model=List[Contact])
async def get_all_contacts():
    """Get all contacts"""
    return await contact_service.get_all()


@router.get("/unread", response_model=List[Contact])
async def get_unread_contacts():
    """Get unread contacts"""
    return await contact_service.get_unread()


@router.get("/{id}", response_model=Contact)
async def get_contact_by_id(id: str):
    """Get contact by ID"""
    contact = await contact_service.get_by_id(id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.patch("/{id}/read", response_model=Contact)
async def mark_as_read(id: str):
    """Mark contact as read"""
    contact = await contact_service.mark_as_read(id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(id: str):
    """Delete contact"""
    deleted = await contact_service.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")

