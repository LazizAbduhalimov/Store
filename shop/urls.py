from django.urls import path
from .views import *


urlpatterns = [
    path("products-menu/", ProductsMenuPage.as_view(), name="products-menu"),
    path("products-menu/product/<slug:slug>/", ProductSinglePage.as_view(), name="product-single")
]
