from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProductBaseCategory, ProductSubCategory, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ["get_image"]

    def get_image(self, instance):
        return mark_safe(f"<img src='{instance.image.url}' width='100' />")

    get_image.short_description = "Preview"

    extra = 0


@admin.register(ProductBaseCategory)
class AdminState(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    list_per_page = 20


@admin.register(ProductSubCategory)
class AdminState(admin.ModelAdmin):
    list_display = [
        "name",
        "base_category",
    ]

    list_per_page = 20


@admin.register(Product)
class AdminState(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "category",
        "is_active",
    ]
    list_editable = [
        "price",
        "is_active",
    ]

    inlines = [ProductImageInline]

    list_per_page = 15

