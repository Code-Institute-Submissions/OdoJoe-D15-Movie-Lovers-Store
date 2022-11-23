from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=150)

    def __str__(self):
        return self.friendly_name

    def get_name(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=150)

    def __str__(self):
        return self.friendly_name

    def get_name(self):
        return self.name


class Format(models.Model):
    name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=150)

    def __str__(self):
        return self.friendly_name

    def get_name(self):
        return self.name


class Stockitem(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    format = models.ForeignKey('Format', null=True, on_delete=models.SET_NULL)
    is_special_edition = models.BooleanField()
    region = models.ForeignKey('Region', null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    genre = models.ForeignKey('Genre', null=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(decimal_places=2, max_digits=4)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
