from django import template

register = template.Library()


@register.filter
def mul(value, arg):
    return value * arg


@register.filter
def total_cost(cart):
    return sum(item.product.price * item.quantity for item in cart)


@register.filter
def total_quantity(cart):
    return sum(item.quantity for item in cart)