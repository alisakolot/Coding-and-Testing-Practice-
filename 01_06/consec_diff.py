"""
Given a list of integers, find the positive difference between each 
consecutive pair of numbers, and put this into a new list of differences. 
Then, find the differences between consecutive pairs in this new list, 
and repeat until the list has a length of 1. Then, return the single value.
The list will only contain integers, and will not be empty.


Tests:
    >>> differences([1, 2, 3])
    0

    >>> differences([1, 5, 2, 7, 8, 9, 0])
    1

    >>> differences([2, 3, 1])
    1

    >>> differences([])
    0
    
"""

def differences(a):
    while len(a)>1:
        k = []
        for i in range(len(a)-1):
            k.append(abs(a[i+1]-a[i]))
        a = k
    else:
        if a == []:
            return 0
        if len(a) == 1:
            return a[0]
    return k[0]







# def differences(lst):
#     if len(lst) == 0:
#         return 0
#     if len(lst) == 1:
#         return 1
    
#     diff = differences(lst)
#     lst2 = []

#     if diff == 0:
#         return None
    
#     for i in range(len(lst)):
#         lst2.append(lst[i+1] - lst[i])
#         return lst2








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")