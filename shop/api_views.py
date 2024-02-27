from rest_framework.generics import ListCreateAPIView

from shop.models import Product, ProductSubCategory, ProductBaseCategory
from .serializers import ProductSerializer, ProductSubCategorySerializer, ProductBaseCategorySerializer


class ProductAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        sex_list = self.request.GET.getlist("sex", None)
        if not sex_list:
            return Product.objects.filter(is_active=True)
        return Product.objects.filter(is_active=True, sex__in=sex_list)


class ProductSubCategoryAPIList(ListCreateAPIView):
    serializer_class = ProductSubCategorySerializer
    queryset = ProductSubCategory.objects.filter(product__isnull=False).distinct()


class ProductBaseCategoryAPIList(ListCreateAPIView):
    serializer_class = ProductBaseCategorySerializer
    queryset = ProductBaseCategory.objects.filter(productsubcategory__product__isnull=False).distinct()
