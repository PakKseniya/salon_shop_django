from django.urls import path
from django.urls import re_path
from . import views
from .views import about, base, index, new_in, show_post, pr, login

app_name = 'salon_shop'

urlpatterns = [
    path('', base, name='main_page'),
    path('about', about, name='about'),
    path('index/', index, name='index'),
    path('new_in', new_in, name='news'),
    path('login', login, name="login"),
    path('product', pr),
    path('post/<int:post_id>', show_post, name='post'),
    re_path(r'category/(?P<slug>[\w\-]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[\w\-]+)/$', views.product_detail, name='product_detail'),
]
"""На глав.странице будут отображены все товары"""
"""На странице будут отображены товары по категориям"""
"""На странице будут отображены детали 1 товара"""
