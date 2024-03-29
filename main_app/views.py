from django.views.generic import ListView

from shop.models import ProductSubCategory, Product
from .mixins import HeaderMixin
from .models import Slider, Collection, BranchOffice


class MainPage(HeaderMixin, ListView):
    model = Product
    template_name = "main_app/index.html"
    queryset = model.objects.filter(is_active=True)
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context["sliders"] = Slider.objects.filter(is_active=True)
        context["collections"] = Collection.objects.filter(is_active=True)
        context["categories"] = ProductSubCategory.objects.filter(product__isnull=False).distinct()
        context["js_filter"] = self.request.GET.get("filter", "*")
        return dict(list(context.items()) + list(self.get_user_context().items()))


class ContactPage(HeaderMixin, ListView):
    model = BranchOffice
    template_name = "main_app/contacts.html"
    queryset = model.objects.filter(is_active=True)
    context_object_name = "contacts"

    def get_context_data(self, **kwargs):
        context = super(ContactPage, self).get_context_data(**kwargs)
        return dict(list(context.items()) + list(self.get_user_context().items()))

