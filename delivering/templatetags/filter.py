from django import template

register = template.Library()


@register.filter
def replacer(value):
    return value.replace("5", "0")
