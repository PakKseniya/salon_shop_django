from django.contrib import admin
from .models import Slider


class SliderAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Slider, SliderAdmin)
