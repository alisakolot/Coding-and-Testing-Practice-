"""Let's pretend your company just hired your friend from college 
and paid you a referral bonus. Awesome! To celebrate, you're taking 
your team out to the terrible dive bar next door and using the 
referral bonus to buy, and build, the largest three-dimensional beer 
can pyramid you can. And then probably drink those beers, because 
let's pretend it's Friday too.

A beer can pyramid will square the number of cans in each level - 
1 can in the top level, 4 in the second, 9 in the next, 16, 25...

Complete the beeramid function to return the number of complete 
levels of a beer can pyramid you can make, given the parameters of:

1) your referral bonus, and

2) the price of a beer can


Test:
    >>> beeramid(9, 2)
    1

    >>> beeramid(21, 1.5)
    3

    >>> beeramid(-1, 4)
    0

    >>> beeramid(1500, 2)
    12

    >>> beeramid(5000, 3)
    16 

"""

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))

import math
def beeramid(bonus, price):
    # bonus > 1
    lst = []
    if bonus > 1:
        beers = bonus // price
        # print(beers)
        # create list of squares in range beers
        for num in range(1, int(beers)):
            n = math.sqrt(num)
            
            if n - int(n) == 0:
                lst.append((n))
        # print(len(lst))
    else:
        return 0
    
    return len(lst)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ✨🌟  Cheers! 🍻  🌟✨ \n')