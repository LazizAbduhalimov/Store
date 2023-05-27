from django.urls import path
from .views import *


urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("contacts/", ContactPage.as_view(), name="contact"),
]
