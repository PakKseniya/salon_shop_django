from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path("favorite/<int:pk>/", views.favorite_add, name='favorite_add'),
    path("favorite_remove/<int:pk>/", views.favorite_remove, name='favorite_remove'),
    path("favorite_detail/", views.favorite_detail, name='favorite_detail'),
]