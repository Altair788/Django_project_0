from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users_alt.apps import UsersAltConfig
from users_alt.views import UserCreateView, email_verification

app_name = UsersAltConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users_alt/user_login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(template_name='users_alt/user_form.html'), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
]
