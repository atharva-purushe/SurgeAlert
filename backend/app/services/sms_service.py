from twilio.rest import Client
from app.core.config import settings

def send_sms(to: str, body: str):
    """
    Sends SMS using Twilio.
    """
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to
        )
        return {"status": "sent", "sid": message.sid}
    except Exception as e:
        return {"status": "error", "error": str(e)}
