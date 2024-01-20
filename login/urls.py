from django.contrib import admin
from django.urls import path
from login import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view()),
    path('login',views.login,name='login'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('register',views.register,name='register'),
    path('otp',views.otp,name='otp'),
    path('forgot_otp',views.forgot_otp,name='forgot_otp'),
    path('validation',views.validation,name='validation'),
    path('forgot_validation',views.forgot_validation,name='forgot_validation'),
    path('new_password',views.new_password,name='new_password'),
]
