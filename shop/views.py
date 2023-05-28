from django.views.generic import ListView, DetailView
from django.db.models import Q

from main_app.mixins import HeaderMixin
from .models import Product, ProductSubCategory, SexEnum


class ProductsMenuPage(ListView, HeaderMixin):
    template_name = "shop/products-menu.html"
    model = Product
    queryset = model.objects.all()
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super(ProductsMenuPage, self).get_context_data(**kwargs)
        context["categories"] = ProductSubCategory.objects.filter(product__isnull=False).distinct()
        context["js_filter"] = self.request.GET.get("filter", "*")
        return dict(list(context.items()) + list(self.get_user_context().items()))


class MenProductsMenuPage(ProductsMenuPage):
    def get_context_data(self, **kwargs):
        context = super(MenProductsMenuPage, self).get_context_data(**kwargs)
        queryset = context["categories"]
        context["categories"] = queryset.filter(
            Q(product__sex=SexEnum.man.value) | Q(product__sex=SexEnum.unisex.value))
        return context

    def get_queryset(self):
        return self.model.objects.filter(is_active=True).exclude(sex=SexEnum.woman.value)


class WomanProductsMenuPage(ProductsMenuPage):
    def get_context_data(self, **kwargs):
        context = super(WomanProductsMenuPage, self).get_context_data(**kwargs)
        queryset = context["categories"]
        context["categories"] = queryset.filter(
            Q(product__sex=SexEnum.woman.value) | Q(product__sex=SexEnum.unisex.value))
        return context

    def get_queryset(self):
        return self.model.objects.filter(is_active=True).exclude(sex=SexEnum.man.value)


class ProductSinglePage(DetailView, HeaderMixin):
    template_name = "shop/product-single.html"
    model = Product
    slug_field = "pk"

    def get_context_data(self, **kwargs):
        context = super(ProductSinglePage, self).get_context_data(**kwargs)
        context["categories"] = ProductSubCategory.objects.all()
        return dict(list(context.items()) + list(self.get_user_context().items()))

