from django.views import View

from cart.models import Order
from shop.models import *


class HeaderMixin(View):
    def get_user_context(self, **kwargs):
        context = kwargs
        user = self.request.user
        context["base_categories"] = ProductBaseCategory.objects.all()
        context["cart"] = Order.objects.get_or_create(user=user)[0]
        return context
