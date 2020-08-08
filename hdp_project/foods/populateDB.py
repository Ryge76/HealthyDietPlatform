"""Handle initial population of the DB for foods"""
from django.db import IntegrityError

from .models import Categories
from .requestAPI import FoodAPI
from .prepareData import Parser

# populate DB with food categories
categories = ['fruits', 'legumes-et-derives', 'produits-laitiers','viandes',
              'poissons', 'boissons',
              'aliments-et-boissons-a-base-de-vegetaux', 'petit-dejeuners',
              'snacks']

for category in categories:
    try:
        entry = Categories.objects.create(categ_name=category)

    except IntegrityError:
        #  TODO strategy
        continue

# query Open Food Facts API


# clean received food data


# populate DB with cleaned food data
