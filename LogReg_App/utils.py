# from django.core.mail import send_mail
# from django.conf import settings

# def send_email_token(email, token):
#     try:
#         subject = "Your account needs to be verified"
#         message = f'click on the link to verified http://127.0.0.1:8000/verify/{token}/'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email, ]
#         send_mail(subject, message, email_from, recipient_list)
        
#     except Exception as e:
#         return False
#     return True