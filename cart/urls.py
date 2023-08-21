from django.urls import path
from .views import *

urlpatterns = [
    path("cart/", CartPage.as_view(), name="cart"),
    path("add_product/<pk>", add_product, name="add-product"),
    path("remove_product/<pk>", remove_product, name="remove-product"),
    path("substract_product/<pk>", substract_product, name="substract-product"),
]
