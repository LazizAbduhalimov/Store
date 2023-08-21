from django.urls import path
from .views import *


urlpatterns = [
    path("products-menu/men/", MenProductsMenuPage.as_view(), name="men-products-menu"),
    path("products-menu/women/", WomanProductsMenuPage.as_view(), name="women-products-menu"),
    path("products-menu/product/<slug:slug>/", ProductSinglePage.as_view(), name="product-single")
]
