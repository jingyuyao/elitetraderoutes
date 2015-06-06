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
    return "<label for='{name}'>{label}: </label>" \
           "<input id='{name}_input' type='text' name='{name}' value='{value}'><br>"\
        .format(name=name, label=label if label else name.capitalize(), value=value if value else '')

@register.filter()
def render_form(obj):
    """
    Renders a basic form with a text input for each element in the object.

    If the object is a dict, then the input will be prepopulated.
    If it is a list, every item in the list will be treated as a field name
    and rendered with an empty input.
    :param obj:
    :return:
    """
    if obj:
        try:
            return '<br>'.join([render_input(name, value) for name, value in obj.items()])
        except:
            pass
        try:
            return '<br>'.join([render_input(name) for name in obj])
        except:
            pass
        return "INVALID DATA FOR render_form: " + str(type(obj)) + str(obj)

    return ''
