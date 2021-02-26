import pytest 
from pete_the_baker import * 


def test_ingredients():
    assert cakes({'eggs': 1, 'flour': 500, 'sugar': 200}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200} == 2