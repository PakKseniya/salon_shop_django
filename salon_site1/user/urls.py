from django.urls import path
from .views import ProfilePage, RegisterView, LoginView, LogoutView



app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfilePage.as_view(), name="profile"),
    path('logged_out/', LogoutView.as_view(), name='logged_out'),
    path('register/', RegisterView.as_view(), name="register"),
]

