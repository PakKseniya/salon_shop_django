from django.db import models
from django.core.validators import MaxLengthValidator


class Slider(models.Model):
    name = models.CharField(max_length=100,
                            validators=[MaxLengthValidator(100)],
                            error_messages={'max_length': 'Очень большая длина'},
                            help_text='Название для слайда до 100 символов,обязательно к заполнению',
                            verbose_name="Название слайда")
    title = models.CharField(blank=True,
                             max_length=150,
                             validators=[MaxLengthValidator(150)],
                             error_messages={'max_length': 'Очень большая длина'},
                             help_text='до 150 символов,необязательное поле',
                             verbose_name="Заголовок слайда")
    description = models.CharField(blank=True,
                                   max_length=150,
                                   validators=[MaxLengthValidator(150)],
                                   error_messages={'max_length': 'Очень большая длина'},
                                   help_text='до 150 символов,необязательное поле',
                                   verbose_name="Текст под заголовком")
    slide_img = models.ImageField(blank=False,
                                  upload_to='slider/',
                                  help_text='изображение обрежется до 1920х1024рх, поэтому брать лучше большое',
                                  verbose_name="Добавить изображение")

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"

    def __str__(self):
        return self.name
