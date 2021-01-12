"""Given three arrays of integers, return the sum of elements that are common in all three arrays.

common([1,2,3],[5,3,2],[7,3,2]) = 5 because 2 & 3 are common in all 3 arrays
common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays

Test:

    >>> common([1,2,3],[5,3,2],[7,3,2])
    5
    
    >>> common([1,2,2,3],[5,3,2,2],[7,3,2,2])
    7
    """

import statistics 
def common(a,b,c):
    lst = []
    lst1 = []
    for items in a, b, c:
        for num in items:
            lst.append(num)
        num1 =  statistics.mode(lst)
        lst1.append(num1)
        lst = [i for i in lst if i!= num1]
    # lst1 = set(lst1)
    print(lst1)
    print(lst)
    return sum(lst1)
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ✨Good job today!✨ ***")