from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from cart.models import Order
from cart.services import add_product_to_user_cart, substract_product_from_user_cart, remove_product_from_user_cart
from main_app.mixins import HeaderMixin


class CartPage(LoginRequiredMixin, ListView, HeaderMixin):
    template_name = "cart/cart.html"
    model = Order
    login_url = reverse_lazy("registration")

    def get_context_data(self, **kwargs):
        context = super(CartPage, self).get_context_data(**kwargs)
        context["order"] = self.model.objects.get_or_create(user=self.request.user)[0]
        return dict(list(context.items()) + list(self.get_user_context().items()))


def add_product_to_user_cart_view(request, pk):
    add_product_to_user_cart(request.user, pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def substract_product_from_user_cart_view(request, pk):
    substract_product_from_user_cart(request.user, pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_product_from_user_cart_view(request, pk):
    remove_product_from_user_cart(request.user, pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def get_user_cart(request):
    order = Order.objects.get_or_create(user=request.user)[0]
    return render(request, "cart/blocks/cart-update-part.html", {"order": order})
