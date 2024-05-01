# cart_filters.py
from django import template

register = template.Library()

@register.filter
def total_price(products):
    return sum(product.price for product in products)
