from enum import Enum

from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class SexEnum(str, Enum):
    man = "M"
    woman = "W"
    unisex = "U"


sex_choices = [
    (SexEnum.man.value, 'Man'),
    (SexEnum.woman.value, 'Women'),
    (SexEnum.unisex.value, 'Unisex'),
]


class ProductBaseCategory(models.Model):
    name = models.CharField("Title", max_length=30, default="")

    def __str__(self):
        return f"{self.name}-{self.id}"


class ProductSubCategory(models.Model):
    name = models.CharField("Title", max_length=30, default="")
    base_category = models.ForeignKey(ProductBaseCategory, verbose_name="Base type", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}-{self.id}"


class Product(models.Model):
    name = models.CharField("Title", max_length=50, default="")
    description = RichTextField("Description")
    price = models.FloatField("Price", default=4.99)
    category = models.ForeignKey(ProductSubCategory, verbose_name="Category", on_delete=models.DO_NOTHING)
    sex = models.CharField("Sex", default=SexEnum.man.value, max_length=1, choices=sex_choices)

    is_active = models.BooleanField("Is active", default=False)

    def get_absolute_url(self):
        return reverse('product-single', kwargs={'slug': self.pk})

    def __str__(self):
        return f"{self.name}-{self.id}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product image", on_delete=models.CASCADE)
    image = models.ImageField("Image", upload_to="images/products/}")

    def __str__(self):
        return "{}-{}".format(self.product.name, self.id)


