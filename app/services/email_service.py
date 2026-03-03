import resend
from app.config.settings import settings
from app.models.contact import Contact
import asyncio


class EmailService:
    def __init__(self):
        self.api_key = settings.RESEND_API_KEY
        self.from_email = settings.RESEND_FROM_EMAIL
        self.reply_to_email = settings.REPLY_TO_EMAIL
        self.admin_email = settings.ADMIN_EMAIL

    async def send_html_email(self, to: str, subject: str, html_content: str):
        """Send HTML email using Resend"""
        try:
            resend.api_key = self.api_key
            
            params = {
                "from": self.from_email,
                "reply_to": self.reply_to_email,
                "to": to,
                "subject": subject,
                "html": html_content,
            }
            
            resend.emails.send(params)
            print(f"✅ Email sent to {to}")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")

    async def send_contact_email_with_attachment(self, contact: Contact):
        """Send confirmation email to user and notification to admin"""
        name = contact.name if contact.name else "there"
        
        # User confirmation email
        user_html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; text-align:center; background-color:#f9f9f9; padding:20px;">
            <h2 style="color:#1a73e8;">👋 Hi {name}!</h2>
            <p>Thanks for reaching out via Quick Contact. 💬</p>
            <p>We've received your message and will get back to you shortly. 🚀</p>
            <p style="font-size:18px; margin:20px 0;">✨ Feel free to explore my work and connect anytime! 🌟</p>
            <a href="mailto:rajsingh170901@gmail.com"
               style="display:inline-block; padding:12px 25px; margin:15px 0; color:white;
                      background-color:#1a73e8; text-decoration:none; border-radius:8px; font-weight:bold;">
               Reach Out ✉️
            </a>
            <p>Best regards,<br/><b>Raj Shekhar Singh 🚀</b></p>
        </body>
        </html>
        """
        
        await self.send_html_email(contact.email, "📬 Message Received!", user_html)
        
        # Admin notification email
        subject = contact.get("subject", "No Subject") if isinstance(contact, dict) else (contact.subject or "No Subject")
        message = contact.message
        
        admin_html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; padding:20px; background-color:#fffbea;">
            <h3 style="color:#1a73e8;">📩 New Contact Message</h3>
            <p><b>Name:</b> {contact.name}</p>
            <p><b>Email:</b> {contact.email}</p>
            <p><b>Subject:</b> {subject}</p>
            <p><b>Message:</b> {message}</p>
            <p>💡 Reply directly to this email to respond!</p>
        </body>
        </html>
        """
        
        await self.send_html_email(self.admin_email, f"📩 New Contact from {contact.name}", admin_html)
        print("✅ Admin email sent")

    async def send_interest_email_async(self, user_email: str):
        """Send interest confirmation email to user and notification to admin"""
        name = self._extract_name_from_email(user_email)
        
        # User confirmation email
        user_html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; text-align:center; background-color:#f0f8ff; padding:20px;">
            <h2 style="color:#1a73e8;">👍 Hi {name}!</h2>
            <p>Thank you for showing interest in my portfolio! 💻✨</p>
            <p>You can reach out anytime for queries or collaboration. 📧</p>
            <a href="mailto:rajsingh170901@gmail.com"
               style="display:inline-block; padding:12px 25px; margin:15px 0; color:white; background-color:#1a73e8; text-decoration:none; border-radius:8px; font-weight:bold;">
               Reach Out ✉️
            </a>
            <p>Cheers,<br/><b>Raj Shekhar Singh 🚀</b></p>
        </body>
        </html>
        """
        
        # Admin notification email
        admin_html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; padding:15px; background-color:#f0f8ff;">
            <h3 style="color:#1a73e8;">💡 New Interest in Portfolio</h3>
            <p>A visitor showed interest in your portfolio website! 🌟</p>
            <p><b>Visitor Email:</b> {user_email}</p>
            <p>💡 Reach out to build connections!</p>
        </body>
        </html>
        """
        
        await self.send_html_email(user_email, "🎉 Thanks for Your Interest! 🌟", user_html)
        await self.send_html_email(self.admin_email, f"💡 New Interest from {name}", admin_html)

    def _extract_name_from_email(self, email: str) -> str:
        """Extract name from email address"""
        if not email or "@" not in email:
            return "there"
        
        name_part = email.split("@")[0].replace("[^A-Za-z]", " ")
        words = name_part.strip().split()
        
        result = []
        for word in words:
            if word:
                result.append(word.capitalize())
        
        return " ".join(result) if result else "there"

