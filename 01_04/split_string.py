"""Tests: 
    >>> solution('asdfadsf')
    ['as', 'df', 'ad', 'sf']

    >>> solution('asdfads')
    ['as', 'df', 'ad', 's_']

    >>> solution('')
    []

    >>> solution('x')
    ['x_']

"""


def solution(s):
    lst = []
    if len(s) % 2:
        s += '_'
    # print(s)

    n = 2
    for index in range(0, len(s), n):
        lst.append(s[index:index+n])
    # print(lst)
    return lst
        


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n")