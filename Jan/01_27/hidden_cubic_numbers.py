"""We search non-negative integer numbers, with at most 3 digits, 
such as the sum of the cubes of their digits is the number itself; 
we will call them "cubic" numbers.

153 is such a "cubic" number : 1^3 + 5^3 + 3^3 = 153

These "cubic" numbers of at most 3 digits are easy to find, even by hand,
so they are "hidden" with other numbers and characters in a string.

The task is to find, or not, the "cubic" numbers in the string and then 
to make the sum of these "cubic" numbers found in the string, if any, 
and to return a string such as:

"number1 number2 (and so on if necessary) sumOfCubicNumbers Lucky" 

if "cubic" numbers number1, number2, ... were found. The numbers 
in the output are to be in the order in which they are encountered 
in the input string.

If no cubic numbers are found return the string:
"Unlucky".

Tests:

    >>> is_sum_of_cubes("aqdf& 0 1 xyz 153 777.777")
    "0 1 153 154 Lucky"

    >>> is_sum_of_cubes("QK29 45[&erui")
    "Unlucky"

"""

def is_sum_of_cubes(s):
    
    pass

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n 🧊 🧊 👶 \n')