"""Define models needed for foods representation."""

from django.db import models


class Products(models.Model):
    product_name = models.TextField
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    nutrition_grade_fr = models.CharField(max_length=1)
    ingredients_text_fr = models.TextField
    allergens = models.TextField
    purchase_places = models.TextField
    stores = models.TextField
    url = models.URLField
    image_url = models.URLField

    def __str__(self):
        return self.product_name


class Categories(models.Model):
    categ_name = models.CharField(max_length=50)

    def __str__(self):
        return self.categ_name
