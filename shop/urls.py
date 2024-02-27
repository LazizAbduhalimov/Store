from django.urls import path

from .api_views import ProductAPIView, ProductSubCategoryAPIList, ProductBaseCategoryAPIList
from .views import *


urlpatterns = [
    path("products-menu/men/", MenProductsMenuPage.as_view(), name="men-products-menu"),
    path("products-menu/women/", WomanProductsMenuPage.as_view(), name="women-products-menu"),
    path("products-menu/product/<slug:slug>/", ProductSinglePage.as_view(), name="product-single")
]

api_urlpatterns = [
    path("api/v1/products/", ProductAPIView.as_view()),
    path("api/v1/products/basecategory/", ProductBaseCategoryAPIList.as_view()),
    path("api/v1/products/subcategory/", ProductSubCategoryAPIList.as_view()),
]

urlpatterns += api_urlpatterns
