"""Complete the function that

    1. accepts two integer arrays of equal length
    2. compares the value each member in one array to the corresponding member in the other
    3. squares the absolute value difference between those two values
    4. and returns the average of those squared absolute value difference between each member pair.

Tests: 
    
    >>> solution([1,2,3], [4,5,6])
    9

    >>> solution([10, 20, 10, 2], [10, 25, 5, -2])
    16.5
"""

def avg(nums_lst):
    return sum(nums_lst) / len(nums_lst)



def solution(array_a, array_b):
    # if arrays are not the same length:
    nums_lst = []
    if len(array_a) ==  len(array_b):
        for i in range(len(array_a)):
            nums_lst.append(abs(array_a[i] - array_b[i]) ** 2)
    
    return avg(nums_lst)
      
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ⭐Great Job! ⭐ \n')
