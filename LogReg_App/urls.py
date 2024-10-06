from django.urls import path
from .views import *
# from .views import forgot_password, PasswordResetConfirmView
# from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView


urlpatterns = [
    path('', LoginFun, name='LoginNm'),
    path('register/', RegisterFun, name='RegisterNm'),
    path('home/', HomeFun, name='HomeNm'),
    path('token/', token_send, name='TokenNm'),
    path('success/', success, name='SuccessNm'),
    path('verify/<auth_token>/', verify, name='verify'),
    path('error/', error_page, name='error'),
    
    
    # path('', homeEmailFun, name='HomeNm'),
    # path('')
    
    
    # path('forgot_password/', forgot_password, name='forgot_password'),
    # path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    
]