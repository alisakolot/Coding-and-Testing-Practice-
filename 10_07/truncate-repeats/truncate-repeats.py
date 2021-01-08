"""Truncate repeating characters into one character.

For example:

>>> truncate('aaaaabbbbbcccaaaa')
'abca'

>>> truncate('hi there')
'hi there'

The function should be able to handle special characters, punctuation, and/or
numbers:

>>> truncate('hi   !!! wooow')
'hi ! wow'
"""

def truncate(string):
    """Truncate repeating characters in a string."""
    lst = []

    for ch in string:
        if not lst or ch!=lst[-1]:
            lst.append(ch)
    return ''.join(lst)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
