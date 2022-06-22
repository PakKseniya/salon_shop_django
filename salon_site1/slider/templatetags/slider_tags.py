from django import template
from slider.models import Slider

register = template.Library()


@register.inclusion_tag('slider/tags/widget_slider.html')
def slider_block():
    block_slider = Slider.objects.all()
    return {'block_slider': block_slider}
