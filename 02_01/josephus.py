"""This problem takes its name by arguably the most important event in the life of the 
ancient historian Josephus: according to his tale, he and his 40 soldiers were trapped 
in a cave by the Romans during a siege.

Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: 
they formed a circle and proceeded to kill one man every three, until one last man was 
left (and that it was supposed to kill himself to end the act).

Well, Josephus and another man were the last two and, as we now know every detail of the 
story, you may have correctly guessed that they didn't exactly follow through the original idea.

You are now to create a function that returns a Josephus permutation, taking as parameters 
the initial array/list of items to be permuted as if they were in a circle and counted out 
every k places until none remained.

Tips and notes: it helps to start counting from 1 up to n, 
instead of the usual range 0..n-1; k will always be >=1.

For example, with n=7 and k=3 josephus(7,3) should act this way.

Test: 
    >>> josephus([1,2,3,4,5,6,7],3)
    [3,6,2,7,5,1,4]

    >>> josephus([1,2,3,4,5,6,7,8,9,10],2)
    [2, 4, 6, 8, 10, 3, 7, 1, 9, 5]

    >>> josephus(["C","o","d","e","W","a","r","s"],4)
    ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a']

    >>> josephus([1,2,3,4,5,6,7],3)
    [3, 6, 2, 7, 5, 1, 4]

    >>> josephus([],3)
    []

"""

def josephus(items, k):
    # find all the  indices in the list that are multiples of k 
        # if the index number % k == 0, then add to the lst
        # pop items from list
    # begin process again
    # conditions: if the length of the list is less than k, then 
    if len(items) <= 0:
        return items
    else:
        lst = []
        i = items.index(k-1)
        for i in range(len(items)-1):
            if i % 4 == 0:
                lst.append(items[i-1])
                items.pop(i-1)
                josephus(items, k)
    return lst

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n ✨ You're solving it! Good job! ✨ \n ")
