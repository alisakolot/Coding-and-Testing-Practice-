"""Print points in matrix, going in a spiral.

Give a square matrix, like this 4 x 4 matrix, it's composed
of points that are x, y points (top-left is 0, 0):

    0,0  1,0  2,0  3,0
    0,1  1,1  2,1  3,1
    0,2  1,2  2,2  3,2
    0,3  1,3  2,3  3,3

Starting at the top left, print the x and y coordinates of each
point, continuing in a spiral.

(Since we provide 3 different versions, you can change this to
the routine you want to test:

    >>> spiral = spiral_by_nested_boxes

Here are different sizes:

    >>> spiral(1)
    (0, 0)

    >>> spiral(2)
    (0, 0)
    (1, 0)
    (1, 1)
    (0, 1)

    >>> spiral(3)
    (0, 0)
    (1, 0)
    (2, 0)
    (2, 1)
    (2, 2)
    (1, 2)
    (0, 2)
    (0, 1)
    (1, 1)

    >>> spiral(4)
    (0, 0)
    (1, 0)
    (2, 0)
    (3, 0)
    (3, 1)
    (3, 2)
    (3, 3)
    (2, 3)
    (1, 3)
    (0, 3)
    (0, 2)
    (0, 1)
    (1, 1)
    (2, 1)
    (2, 2)
    (1, 2)
"""


def spiral(matrix_size):
    """Spiral coordinates of a matrix of `matrix_size` size."""
    #length of one side = matrix size
    #each x coordinate = matrix_size - 1
    #beginning point: (0,0), matrix_size = 2
        #step 1. x + 1, y + 0
        #step 2. x + 0 , y + 1 
        #step 3. x - 1, y + 0

    #Origin => Right:
        #(0,0)
        #(1,0)
        #(2,0) 
        x = 0
        y = 0
        
    
    #Left Turn 1:
        #(2,0)
        #(2,1)
    
    #Left ^ Up:
        #(2,1)
        #(2,2)
    
    #Left Turn 2:
        #(2,2)
        #(1,2)
    
    #Left <= Cont:
        #(1,2)
        #(0,2)
    
    #Left Down:
        #(0,2)
        #(0,1)

    #Right Turn:
        #(0,1)
        #(1,1)
    





if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU MUST BE DIZZY WITH PRIDE!\n")
