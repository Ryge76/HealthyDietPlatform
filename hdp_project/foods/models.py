from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.TextField
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    nutrition_grade_fr = models.CharField(max_length=1)
    ingredients_text_fr = models.TextField
    allergens = models.TextField
    purchase_places = models.TextField
    stores = models.TextField
    url = models.URLField
    image_url = models.URLField


class Category(models.Model):
    categ_name = models.CharField(max_length=50)



"""
    categories = ['fruits', 'legumes-et-derives', 'produits-laitiers',
                  'viandes', 'poissons', 'boissons',
                  'aliments-et-boissons-a-base-de-vegetaux', 'petit-dejeuners',
                  'snacks']
"""

