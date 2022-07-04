from django.urls import path
from . import views
from .views import about, base, index, new_in, show_post, pr, salon_kr

app_name = 'salon_shop'

urlpatterns = [
    path('', base, name='main_page'),
    path('about/', about, name='about'),
    path('index/', index, name='index'),
    path('new_in/', new_in, name='news'),
    path('product/', pr),
    path('post/<int:post_id>', show_post, name='post'),
    path('product_list/', views.product_list, name='product_list'),
    path('category/<category_slug>/', views.product_list, name='product_list_by_category'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
    path('salon_kr/', salon_kr, name='salon_kr'),
]
