from django import template

register = template.Library()


@register.filter(name="is_exist_in_cart")
def is_exist_in_cart(food_item, cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == food_item.id:
            return True
    return False
