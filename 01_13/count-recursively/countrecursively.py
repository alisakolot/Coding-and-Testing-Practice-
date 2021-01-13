"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

        >>> count_recursively([3, 4, 5, 6, 7])
        5
"""


def count_recursively(lst):
    """Return number of items in a list, using recursion."""
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return 1
    count = count_recursively(lst)

    if count== 0:
        return None
    else:
        return len(lst)

# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))

# num = 3
# print("The factorial of", num, "is", factorial(num))



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")
