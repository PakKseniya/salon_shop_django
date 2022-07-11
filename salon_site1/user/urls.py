from django.urls import path
from .views import ProfilePage, RegisterView, LoginView, LogoutView, ProfileInfo

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfilePage.as_view(), name="profile"),
    path('profile_info/', ProfileInfo.as_view(), name='profile_info'),
    path('logged_out/', LogoutView.as_view(), name='logged_out'),
    path('register/', RegisterView.as_view(), name="register"),
]

