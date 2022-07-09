from django.db import models
from django.contrib.auth.models import User
from salon_shop.models import Product


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product,  on_delete=models.CASCADE, verbose_name='Товар')



