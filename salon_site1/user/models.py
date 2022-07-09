from django.db import models

from salon_shop.models import Product


class UserProfile(models.Model):
    favorites = models.ManyToManyField(Product, related_name='favorit_by')
