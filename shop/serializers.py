from rest_framework.serializers import ModelSerializer

from shop.models import Product, ProductSubCategory, ProductBaseCategory


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductSubCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductSubCategory
        fields = "__all__"


class ProductBaseCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductBaseCategory
        fields = "__all__"