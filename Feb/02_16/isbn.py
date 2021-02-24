"""ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. 
The last digit can be 0-9 or X, to indicate a value of 10.

An ISBN-10 number is valid if the sum of the digits multiplied by their position 
modulo 11 equals zero.

For example:

ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10

Tests:
    >>> valid_ISBN10('1112223339')
    True

    >>> valid_ISBN10('048665088X')
    True

    >>> valid_ISBN10('1293000000')
    True
 
    >>> valid_ISBN10('1234554321')
    True

    >>> valid_ISBN10('1234512345')
    False

    >>> valid_ISBN10('1293')
    False

    >>> valid_ISBN10('X123456788')
    False
"""

def valid_ISBN10(isbn): 
    # position = index + 1
    if len(isbn) == 10:
        nums = 0
        for num in isbn:
            if num.isdigit():
                n = isbn.index(num)
                nums += int(num) * (n+1)
                if nums % 11 == 0:
                    return True 
            else:

                return False
                
    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n V A L I D   I S B N \n')