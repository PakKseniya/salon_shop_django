from django.core.validators import RegexValidator
from django.db import models
from salon_shop.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    email_validator = RegexValidator(
        regex=r"^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|"
              r"(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$")

    ph_numb_validator = RegexValidator(regex=r"^((\+7|7|8)+([0-9]){10})$",
                                       message='Значение в поле "Телефон" должно '
                                               'состоять из 11 цифр от 0 до 9,'
                                               'где первая цифра - 7/+7 или 8')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    email = models.EmailField(validators=[email_validator])
    address = models.CharField(max_length=250, verbose_name='Адрес доставки')
    postal_code = models.CharField(max_length=20, verbose_name='Индекс')
    city = models.CharField(max_length=100, verbose_name='Город доставки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True)
    telephone = models.CharField(validators=[ph_numb_validator], max_length=200, null=True, verbose_name='телефон')
    status = models.BooleanField(default=False)
    paid = models.BooleanField(default=False, verbose_name='Оплачен?')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ №: {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ №')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT,
                                verbose_name='ID продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена на момент заказа')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
