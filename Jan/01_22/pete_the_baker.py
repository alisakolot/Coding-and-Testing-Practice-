"""Pete likes to bake some cakes. He has some recipes and ingredients. 
Unfortunately he is not good in maths. Can you help him to find out, 
how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the 
available ingredients (also an object) and returns the maximum number 
of cakes Pete can bake (integer). For simplicity there are no units 
for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 
200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

Tests:
    >>> cakes({'eggs': 1, 'flour': 500, 'sugar': 200}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
    2

    >>> cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000})
    0
"""

def cakes(recipe, available):
    assert isinstance(recipe, dict) ==  True
    # min_cakes = 10 ** 10 # TODO: DON'T MAKE ASSUMPSTIONS
    ing_num_lst = []
    for x in recipe:
        if x in available:
            ing_num = available[x] // recipe[x]
            ing_num_lst.append(ing_num)
            # if ing_num < min_cakes:
            # min_cakes = ing_num
        else:
            return 0

    return min(ing_num_lst)
    

    # return min_cakes

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🌟 You baked some cakes! 🧑‍🍳🌟 \n')