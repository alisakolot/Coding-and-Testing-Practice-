def furthest_optimized(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    #subtract items from the list cafes from num_holes
    #example, test1: 
    #   num_holes = 3
        #
    #   cafe_idx = [0,1,2]
    #       3-0 = 3 <= this is not a good idea because we skip idx 1,2
    #       3-1 = 2 <= this skips a hole. 
    #       3-2 = 1 <= this is in the situation that a lemming does not move
    #       REMEMBER THAT IF YOU'RE SUBTRACTING, A NUMBER CANNOT INCLUDE ITSELF
    #           ALSO: keep in mind that its redundant for a lemming to include the hole that
    #           is a nearby cafe
    #       dist = len(num_holes)-2
    #       let's give dist its own list, len_dist = [] 
    #       add dist to len_dist
    #       find the longest value in len_dist and print it

    dist = num_holes-2
    len_dist = []

    #idx_loc is the index of the location of the cafe in a sorted list 
    for idx_loc in cafes:
        l = dist - idx_loc
        len_dist.append(l)
        print(len_dist)

        return max(len_dist)

"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(7, [0, 6])
    3
    

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2
"""



        






    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
