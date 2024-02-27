from cart.models import Order
from shop.models import Product


def add_product_to_user_cart(user, product_id) -> None:
    product_to_add = Product.objects.get(pk=product_id)
    order = Order.objects.get_or_create(user=user)[0]

    product_order, created = order.products.get_or_create(product=product_to_add)
    if not created:
        product_order.amount += 1

    product_order.save()


def substract_product_from_user_cart(user, product_id) -> None:
    product_to_substract = Product.objects.get(pk=product_id)
    order = Order.objects.get_or_create(user=user)[0]

    product_order = order.products.get(product=product_to_substract)
    product_order.amount -= 1
    product_order.save()
    if product_order.amount < 1:
        product_order.delete()


def remove_product_from_user_cart(user, product_id):
    product = Product.objects.get(pk=product_id)
    order = Order.objects.get_or_create(user=user)[0]

    product_order = order.products.get(product=product)
    product_order.delete()
