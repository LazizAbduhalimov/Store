from django.contrib.auth.views import LoginView

from cart.models import Order
from registration.forms import LoginForm
from shop.models import *


class HeaderMixin(LoginView):
    form_class = LoginForm

    def get_user_context(self, **kwargs):
        context = kwargs
        user = self.request.user
        context["base_categories"] = ProductBaseCategory.objects.all()
        if not user.is_anonymous:
            context["cart"] = Order.objects.get_or_create(user=user)[0]

        return context

    def get_success_url(self):
        return reverse("home")
