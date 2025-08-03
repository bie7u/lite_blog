import re
from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def clean_html(value):
    value = re.sub(r'<img[^>]*>', '', value)  # remove <img>
    return strip_tags(value)  # remove all other tags
