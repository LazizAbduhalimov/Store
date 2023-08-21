from django.contrib import admin

from cart.models import ProductOrder, Order


class ProductOrderInLine(admin.TabularInline):
    model = ProductOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductOrderInLine]

    list_per_page = 20
