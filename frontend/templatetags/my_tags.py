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
def render_link(url, text=None):
    """
    If value is a url, hyperlink it with text if exist.

    :param url:
    :param text:
    :return:
    """
    try:
        url_validator(url)
        return "<a href='%s'>%s</a>" % (url, text if text else url)
    except ValidationError:
        return url

@register.filter()
def render_input(name, value=None, label=None):
    return "<label for='%s'>%s: </label><input id='%s' type='text' name='%s' value='%s'>" % \
           (name, label if label else name.capitalize(), name, name, value if value else '')
