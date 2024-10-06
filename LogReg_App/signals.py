from django.core.mail import send_mail
from django.conf import settings


def send_login_email(sender, request, user, **kwargs):
    if user.email:  # Check if user has an email address
        send_mail(
            'Login Notification',
            f'Hello {user.username},\n\nYou have successfully logged in.',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    else:
        # Log or handle the case where the user does not have an email address
        print(f'User {user.username} does not have a valid email address.')
