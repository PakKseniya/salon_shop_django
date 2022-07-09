# Generated by Django 4.0.4 on 2022-07-07 10:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salon_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.RegexValidator(regex='^(([^<>()[\\]\\\\.,;:\\s@\\"]+(\\.[^<>()[\\]\\\\.,;:\\s@\\"]+)*)|(\\".+\\"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$')])),
                ('address', models.CharField(max_length=250, verbose_name='Адрес доставки')),
                ('postal_code', models.CharField(max_length=20, verbose_name='Индекс')),
                ('city', models.CharField(max_length=100, verbose_name='Город доставки')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('telephone', models.CharField(max_length=200, null=True, validators=[django.core.validators.RegexValidator(message='Значение в поле "Телефон" должно состоять из 11 цифр от 0 до 9,где первая цифра - 7/+7 или 8', regex='^((\\+7|7|8)+([0-9]){10})$')], verbose_name='телефон')),
                ('status', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачен?')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderNewItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена на момент заказа')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders_new.ordernew', verbose_name='Заказ №')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='salon_shop.product', verbose_name='ID продукта')),
            ],
        ),
    ]