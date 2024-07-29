from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import RegistrationView

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
]
