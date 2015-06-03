__author__ = 'jingyu'
from django import template
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

register = template.Library()
url_validator = URLValidator()

@register.filter()
def get_type(value):
    """
    Helper function that returns the class name of the variable.

    :param value:
    :return:
    """
    return type(value)

@register.filter()
def render_link(value, text=None):
    """
    If value is a url, hyperlink it with text if exist.

    :param value:
    :param text:
    :return:
    """
    try:
        url_validator(value)
        return "<a href='%s'>%s</a>" % (value, text if text else value)
    except ValidationError:
        return value
