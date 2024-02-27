from django.urls import path
from .views import *

urlpatterns = [
    path("cart/", CartPage.as_view(), name="cart"),
    path("add_product/<pk>", add_product_to_user_cart_view, name="add-product"),
    path("remove_product/<pk>", remove_product_from_user_cart_view, name="remove-product"),
    path("substract_product/<pk>", substract_product_from_user_cart_view, name="substract-product"),
]

htmx_urlpatterns = [
    path("cart/refresh_cart/", get_user_cart, name="refresh-cart")
]

urlpatterns += htmx_urlpatterns
