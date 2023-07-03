from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter('reportkey')
def reportkey(dict_data, key):
    if key in dict_data:
        return dict_data.get(key)
    

@register.filter
def custom_filter(text, color):
    safe_text = '<span style="color:{color}">{text}</span>'.format(color=color, text=text)
    return mark_safe(safe_text)