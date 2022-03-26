from django import template

from core.checkers.user_checkers import has_group

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


@register.filter(name='has_group')
def user_has_group(user, group_name):
    return has_group(user, group_name)
