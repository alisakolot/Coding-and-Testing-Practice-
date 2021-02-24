"""Two integer numbers are added using the column addition method. 
When using this method, some additions of digits produce non-zero 
carries to the next positions. Your task is to calculate the number 
of non-zero carries that will occur while adding the given numbers.

The numbers are added in base 10.
Example

For a = 543 and b = 3456, the output should be 0

For a = 1927 and b = 6426, the output should be 2

For a = 9999 and b = 1, the output should be 4


Tests: 

    >>> number_of_carries(543, 3456)
    0

    >>> number_of_carries(1927,6426)
    2

    >>> number_of_carries(9999,1)
    4

    >>> number_of_carries(1234,5678)
    2


"""

def number_of_carries(a, b):
    #coding and coding..
    pass


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n Good job! \n')