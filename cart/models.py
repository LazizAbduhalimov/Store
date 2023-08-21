from django.contrib.auth.models import User
from django.db import models

from shop.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)

    def get_products(self):
        return self.productorder_set.all()

    def get_total_price(self):
        total = 0
        products_in_order = self.get_products()
        for product in products_in_order:
            total += product.get_total_price()

        return round(total, 2)

    def __str__(self):
        return f"Order - {self.pk}, user - {self.user}"


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, verbose_name="Order", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField("Amount", default=1)

    def get_total_price(self):
        return round(self.product.price * self.amount, 2)

    def __str__(self):
        return f"Product: {self.product.name} (x{self.amount}), user: {self.order.user}"

