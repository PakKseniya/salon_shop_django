# Generated by Django 4.0.4 on 2022-06-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Адрес для рассылки', 'verbose_name_plural': 'Адреса для рассылки'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почтовый адрес'),
        ),
    ]
