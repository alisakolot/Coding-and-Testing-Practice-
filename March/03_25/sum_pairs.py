'''Given a list of integers and a single sum value, 
return the first two values (parse from the left 
please) in order of appearance that add up to form the sum.

Tests: 
    >>>  sum_pairs([1, 4, 8, 7, 3, 15], 8)
    [1, 7]

    >>> sum_pairs([1, -2, 3, 0, -6, 1], -6)
    [0, -6]


'''

def sum_pairs(lst, n):
    result = []
    for i in range(len(lst)-1):
        if lst[i] + lst[i+1] == n:
            print('true')

    pass

