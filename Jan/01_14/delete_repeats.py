"""Task

Given a list lst and a number N, create a new list that contains each number of 
lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], 
you take [1,2,3,1,2], drop the next [1,2] since this would lead to 
1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

    Test: 
    
    >>> delete_nth([20,37,20,21], 1)
    [20,37,21]

    >>> delete_nth([1,1,3,3,7,2,2,2,2], 3)
    [1, 1, 3, 3, 7, 2, 2, 2]
"""

def delete_nth(order, n):
    # n = number of repetitions allowed
    # create result list
    # count the number of times each number appears in the list
    # if the count is greater than n then do not append the number to the new list
    # return result

    result = []
    count = 0
    order = sorted(order)
    count_list = []
    for i in range(len(order)-1):
        if order[i] == order[i+1]:
            count+=1 
            if count > 1:
                count_list.append(count)
            
    return count_list    






if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("**** Yay! You solved this one! ****")
