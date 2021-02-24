""""Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

Tests:
    >>> move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
    [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]

    >>> move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
    [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""


def move_zeros(array):
    zeros = []
    nums = []
    for num in array:
        if num == 0:
            zeros.append(num)
        else:
            nums.append(num)
    nums.extend(zeros)
    return nums



if __name__ == '__main__':
    import doctest 
    if doctest.testmod().failed == 0:
        print('\n Zero 7 is proud of you.🕵️ 😎 \n')