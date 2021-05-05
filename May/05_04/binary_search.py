"""Write a binary search function 

Tests: 
    >>> binary_search(50):
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

"""

# 1. Divide the number in half, assign the middle number as bottom/top part of the range 
# 2. Determine if the number is in the range: if it isn't, then add 1 to number of guesses 
# 3. When the number is in the range divide that range in two, until you reach the number

def binary_search(number): 

    assert 0 < val < 101

    num_guesses = 0
    # counting the number of guesses within a range 

    return num_guesses







if __name__ == "__main__": 
    import doctest
    if doctest.testmod().failed == 0: 
        print("\nYou Guessed It!\n")