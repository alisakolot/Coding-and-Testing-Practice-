""""Hit the target
given a matrix n x n (2-7), determine if the arrow is directed to the target (x).
There will be only 1 arrow '>' and 1 target 'x'
An empty spot will be denoted by a space " ", the target with a cross "x", and the scope ">"
Examples:
given matrix 4x4:
[
[' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' '], --> return true
[' ', '>', ' ', 'x'],
[' ', ' ', ' ', ' ']
]
given matrix 4x4:
[
[' ', ' ', ' ', ' '],
[' ', '>', ' ', ' '], --> return false
[' ', ' ', ' ', 'x'],
[' ', ' ', ' ', ' ']
]

given matrix 4x4:
[
[' ', ' ', ' ', ' '],
[' ', 'x', '>', ' '], --> return false
[' ', '', ' ', ' '],
[' ', ' ', ' ', ' ']
]

In this example, only a 4x4 matrix was used, the problem will have matrices of dimensions from 2 to 7
Happy hacking as they say!

Tests:
    >>> solution([['>', ' '], [' ', 'x'],])
    False

    >>> solution([[' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' '],[' ', ' ', '>', ' ', 'x'],[' ', ' ', '', ' ', ' ']])
    True

    >>> 
"""


def solution(mtrx):
    # 1. iterate through each item in the nested lists
    # 2. Find location of target
    # 3. Compare location of target to location of pointer
    # 4. If the location of target is greater than pointer, return True

    for lst in mtrx:
        for item in lst:
            if item == 'x':
                print('target idx', lst.index('x'))
                target_idx = lst.index('x')
            elif item == '>':
                print('pointer idx', lst.index('>'))
                pointer_idx = lst.index('>')

    if target_idx > pointer_idx:
        return True 
    return False
            

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n On Target 🎯 \n')