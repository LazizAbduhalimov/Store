from django.db import models


class Slider(models.Model):
    title = models.CharField("Title", max_length=25, default="")
    subtitle = models.CharField("Subtitle", max_length=50, default="")
    image = models.ImageField("Image", upload_to='images/slider/')
    is_active = models.BooleanField("Is active", default=False)

    def __str__(self):
        return f'{self.title}-{self.id}'


class Collection(models.Model):
    title = models.CharField("Title", max_length=25, default="")
    subtitle = models.CharField("Subtitle", max_length=255, default="")
    sale = models.CharField("Sale", max_length=10, default="")
    image = models.ImageField("Image", upload_to='images/slider/')
    is_active = models.BooleanField("Is active", default=False)

    def __str__(self):
        return f'{self.title}-{self.id}'


class News(models.Model):
    pass


class BranchOffice(models.Model):
    title = models.CharField("Title", max_length=50, default="")
    description = models.TextField("Description", default="")
    location = models.TextField("Location", default="")
    phone = models.CharField("Phone number", max_length=20, default="")
    email = models.EmailField("Email", max_length=255, default="")
    image = models.ImageField("Image", upload_to='images/slider/', null=True)

    is_active = models.BooleanField("Is active", default=False)

    def __str__(self):
        return f"{self.title}-{self.id}"
