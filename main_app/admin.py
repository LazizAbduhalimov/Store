from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Slider, Collection, BranchOffice


@admin.register(Slider)
class AdminState(admin.ModelAdmin):
    list_display = [
        "title",
        "get_image",
        "is_active",
    ]
    list_editable = [
        "is_active"
    ]

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='100' />")

    get_image.short_description = "Image"
    list_per_page = 15


@admin.register(Collection)
class AdminState(admin.ModelAdmin):
    list_display = [
        "title",
        "get_image",
        "is_active",
    ]
    list_editable = [
        "is_active"
    ]

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='100' />")

    get_image.short_description = "Image"

    list_per_page = 15


@admin.register(BranchOffice)
class AdminState(admin.ModelAdmin):
    list_display = [
        "title",
        "get_image",
        "is_active",
    ]
    list_editable = [
        "is_active"
    ]

    def get_image(self, obj):
        if not obj.image:
            return "Image not Found"

        return mark_safe(f"<img src='{obj.image.url}' width='100' />")

    get_image.short_description = "Image"

    list_per_page = 15
