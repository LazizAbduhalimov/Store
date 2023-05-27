from django.views.generic import ListView, DetailView

from .models import Product, ProductSubCategory, ProductBaseCategory


class ProductsMenuPage(ListView):
    template_name = "shop/products-menu.html"
    model = Product
    queryset = model.objects.filter(is_active=True)
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super(ProductsMenuPage, self).get_context_data(**kwargs)
        context["categories"] = ProductSubCategory.objects.all()
        context["base_categories"] = ProductBaseCategory.objects.all()
        context["js_filter"] = self.request.GET.get("filter", "*")
        return context


class ProductSinglePage(DetailView):
    template_name = "shop/product-single.html"
    model = Product
    slug_field = "pk"

    # def get_context_data(self, **kwargs):
    #     context = super(ProductSinglePage, self).get_context_data(**kwargs)
    #     context["categories"] = ProductSubCategory.objects.all()
    #     return context

