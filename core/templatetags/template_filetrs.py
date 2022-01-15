from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def subtract(value, arg):
    return value - arg


@register.filter
def percentage_of(value, arg):
    return 100 - ((value * 100) / arg)
