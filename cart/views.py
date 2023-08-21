from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from cart.models import Order
from main_app.mixins import HeaderMixin
from shop.models import Product


class CartPage(LoginRequiredMixin, ListView, HeaderMixin):
    template_name = "cart/cart.html"
    model = Order
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super(CartPage, self).get_context_data(**kwargs)
        context["order"], context["created"] = Order.objects.get_or_create(user=self.request.user)
        return dict(list(context.items()) + list(self.get_user_context().items()))


def add_product(request, pk):
    product = Product.objects.get(pk=pk)
    order = Order.objects.get_or_create(user=request.user)[0]

    product_order, created = order.get_products().get_or_create(order=order, product=product)
    if not created:
        product_order.amount += 1

    product_order.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def substract_product(request, pk):
    product = Product.objects.get(pk=pk)

    order = Order.objects.get_or_create(user=request.user)[0]
    product_order = order.get_products().get(product=product)
    product_order.amount -= 1
    product_order.save()
    if product_order.amount < 1:
        product_order.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_product(request, pk):
    product = Product.objects.get(pk=pk)

    order = Order.objects.get_or_create(user=request.user)[0]
    product_order = order.get_products().get(product=product)
    product_order.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
