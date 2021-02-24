"""Define a function that takes in two non-negative integers 
a and b and returns the last decimal digit of a^b. 
Note that a and b may be very large!

For example, the last decimal digit of 979^797 is 999, 
since 97=47829699^7 = 478296997=4782969. 
The last decimal digit of (2200)2300({2^{200}})^{2^{300}}(2200)2300, 
which has over 109210^{92}1092 decimal digits, is 666. Also, please take 000^000 to be 111.

You may assume that the input will always be valid.


Tests::

    >>> last_digit(4, 1) 
    4

    >>> last_digit(4, 2)
    6

    >>> last_digit(9, 7)
    9

    # >>> last_digit(10, 10 ** 10) 
    # 0

    # >>> last_digit(2 ** 200, 2 ** 300)
    # 6 
"""


def last_digit(n1, n2):
    n = n1 ** n2
    n = str(n)
    return int(n[-1])
    


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n 💫🌟 Look at that! You solved it! 🌟💫 \n')