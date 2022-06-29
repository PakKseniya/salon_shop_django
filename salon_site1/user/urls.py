from django.urls import path
from django.contrib.auth import views as auth_views
from .views import LoginView, ProfilePage, RegisterView


app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfilePage.as_view(), name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
]

