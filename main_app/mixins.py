from shop.models import *
from main_app.models import *


class HeaderMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["base_categories"] = ProductBaseCategory.objects.all()

        return context
