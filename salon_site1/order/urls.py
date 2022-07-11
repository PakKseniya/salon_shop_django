from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('history_orders/', views.history_orders, name='history_orders'),
    path('list_order_item/<int:order_id>/', views.list_order_item, name='list_order_item'),

]