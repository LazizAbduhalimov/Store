from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.db.models import Q
from random import randint

from cart.models import Order
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
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super(ProductSinglePage, self).get_context_data(**kwargs)
        context["categories"] = ProductSubCategory.objects.all()
        context["similar_products"] = Product.objects.filter(
            is_active=True,
            category=self.object.category).exclude(id__in=(self.object.id,)).distinct()

        all_products = Product.objects.filter(is_active=True).exclude(id__in=(self.object.id,)).distinct()
        if len(all_products) > 4:
            r_num = randint(0, len(all_products)-5)
            other_products = all_products[r_num:r_num+4]
        else:
            other_products = all_products

        context["other_products"] = other_products

        return dict(list(context.items()) + list(self.get_user_context().items()))
