'''Given a list of integers and a single sum value, 
return the first two values (parse from the left 
please) in order of appearance that add up to form the sum.

Tests: 
    >>> sum_pairs([1, 4, 8, 7, 3, 15], 8)
    [1, 7]

    >>> sum_pairs([1, -2, 3, 0, -6, 1], -6)
    [0, -6]


'''

def sum_pairs(lst, n):
    result = []
    for i in range(len(lst)-1):
        pair_sum = lst[i]+lst[i+1] 
        print(f'{lst[i]} + {lst[i+1]} = {pair_sum}')
        if n == pair_sum:
            result.append(lst[i])
            result.append(lst[i+1])
            print('ok')
    return result

# Some solution ideas: 
    # turn the given list into a stack?
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n You solved the thing! Here's a star! ⭐ \n")