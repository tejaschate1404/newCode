from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.conf import settings

def send_email_token(email, token):
    try:
        subject = "Email Verification"
        message = f" click here to verify : http://127.0.0.1:8000/verify/{token}"
        from_email = settings.DEFAULT_FROM_EMAIL  # or specify the sender email directly
        recipient_list = [email]  # Send to the provided email

        send_mail(
            subject,
            message,
            from_email,
            recipient_list)
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

    return True
