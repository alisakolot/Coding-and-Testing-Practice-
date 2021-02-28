import pytest 
from pete_the_baker import * 


def test_ingredients():
    assert cakes({'eggs': 1, 'flour': 500, 'sugar': 200}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}) == 2
    assert cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}) == 0
    assert cakes({'apples': 5, 'flour': 600, 'sugar': 300, 'milk': 200, 'oil': 200}, {'sugar': 500, 'flour': 2000, 'milk': 2000}) == 0

def test_outliers():
    assert cakes({'apples': 0, 'flour': 60, 'sugar': 30, 'milk': 20, 'oil': 2}, {'sugar': 0, 'flour': 200, 'milk': 2000}) == 0
    assert cakes({'apples': 0, 'flour': 60, 'sugar': 30, 'milk': 20, 'oil': 2},{}) == 0
    # Check the error message
    assert cakes({}, {}) ==  0

# def test_inputs():
#     # How to check if the inputs are the correct data type
#     assert isinstance(cakes(recipe), dict) ==  True