from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .utils import *
from .models import *
import uuid

def RegisterFun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
        
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username already exists')
                return redirect('RegisterNm')
            
            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.success(request, "Email already registered!")
                return redirect('RegisterNm')

            # Create a new user
            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj, auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)
            return redirect('TokenNm')
            
        except Exception as e:
            print(e)
        
        # messages.success(request, "Registration successful!")
        # return redirect('LoginNm')  # Redirect to login after successful registration
        
    return render(request, 'Register.html')


def LoginFun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username).first()
        
        if user_obj is None:
            messages.success(request, "User is not found")
            return redirect('LoginNm')
        
        profile_obj = Profile.objects.filter(user = user_obj).first()
        
        if not profile_obj.is_verified:
            messages.success(request, "Profile is not verified check your mail!")
            return redirect('LoginNm')
              
        user = authenticate(username=username, password=password)
        
        # Authenticate using username or email (depending on your setup)
        if user is None:
            messages.success(request, "Wrong Password")
            return redirect('LoginNm')
        
        login(request, user)
        return redirect('HomeNm')
        
        
            

    return render(request, 'login.html')



def HomeFun(request):
#     send_mail(
#         "Check Mail",
#         "I send mail through django",
#         "navedhusainshaikh@gmail.com",
#         ["navedhusain2004@gmail.com"],
#         fail_silently=False,
# )
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def token_send(request):
    return render(request, 'token_send.html')


def send_mail_after_registration(email, token):
    
    subject = 'Your Account Needs to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email ,]
    send_mail(subject, message, email_from, recipient_list)
    
    
    return render

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified')
                return redirect('LoginNm')
                
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, "Your account has been verified.")
            return redirect('LoginNm')
        else:
            return redirect("/error")
            
    except Exception as e:
        print(e)
        
def error_page(request):
    return render(request, 'error.html')


# def logoutFun(request):
#     logout(request)
#     return render(request, 'logout.html')



# def homeEmailFun(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         send_mail(
#         "just mail",
#         "Upadetd Mail find the error",
#         "navedhusainshaikh@gmail.com",
#         [User.email],
#         fail_silently=False,
# )
        
#         user_obj, created = User.objects.get_or_create(username=email)
#         if created:
#             user_obj.set_password(password)
#             user_obj.save()
        
        # user_obj, created = User.objects.get_or_create(username=email)
        # if created:
        #     user_obj.set_password(password)
        #     user_obj.save()
            
        # p_obj, created = Profile.objects.get_or_create(
        #     user=user_obj,
        #     defaults={'email_token': str(uuid.uuid4())}
        # )
        # if created:
        #     send_email_token(email, p_obj.email_token)
            
        # user_obj.set_password(password)
        # p_obj = Profile.objects.create(
        #     user = user_obj,
        #     email_token = str(uuid.uuid4())
        # )
        # send_email_token(email, p_obj.email_token)
        
        
    return render(request, 'home.html')

# def verify(request, token):
#     try:
#         obj = Profile.objects.get(email_token = token)
#         obj.is_verified = True
#         obj.save()
#         return HttpResponse('your account verified')
        
#     except Exception as e:
#         return HttpResponse('invalid token')
    
# from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
# from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetDoneView
# from django.urls import reverse_lazy
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags

# def forgot_password(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             associated_users = User.objects.filter(email=email)
#             if associated_users.exists():
#                 for user in associated_users:
#                     # Create a password reset token
#                     token = str(uuid.uuid4())
#                     Profile.objects.filter(user=user).update(email_token=token)
                    
#                     # Send the email
#                     subject = 'Password Reset Requested'
#                     html_message = render_to_string('registration/password_reset_email.html', {
#                         'email': email,
#                         'token': token,
#                     })
#                     plain_message = strip_tags(html_message)
#                     send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [email], html_message=html_message)
                    
#             return redirect('password_reset_done')
#     else:
#         form = PasswordResetForm()
#     return render(request, 'forgot_password.html', {'form': form})

# class PasswordResetConfirmView(PasswordResetConfirmView):
#     template_name = 'registration/password_reset_confirm.html'
#     success_url = reverse_lazy('password_reset_complete')

# from django.dispatch import receiver
# from django.contrib.auth.signals import user_logged_in

# def send_login_email(sender, request, user, **kwargs):
#     if user.email:  # Check if user has an email address
#         send_mail(
#             'Login Notification',
#             f'Hello {user.username},\n\nYou have successfully logged in.',
#             settings.EMAIL_HOST_USER,
#             [user.email],
#             fail_silently=False,
#         )
#     else:
#         # Log or handle the case where the user does not have an email address
#         print(f'User {user.username} does not have a valid email address.')

