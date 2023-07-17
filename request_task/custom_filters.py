from django import template

register = template.Library()


@register.filter(name="split_string")
def split_string(value):
    delimiter = ";" if ";" in value else ","
    return value.split(delimiter)
