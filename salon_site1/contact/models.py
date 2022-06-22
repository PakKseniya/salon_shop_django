from django.db import models


class Contact(models.Model):
    """Подписка по email"""
    email = models.EmailField(verbose_name='Почтовый адрес')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        verbose_name = 'Адрес для рассылки'
        verbose_name_plural = 'Адреса для рассылки'

    def __str__(self):
         return self.email
