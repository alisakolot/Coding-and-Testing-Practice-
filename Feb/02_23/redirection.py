"""Once upon a time, on a way through the old wild mountainous west,…

… a man was given directions to go from one point to another. 
The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, 
"WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. 
Since this is the wild west, with dreadfull weather and not much water, it's important to save 
yourself some energy, otherwise you might die of thirst!
How I crossed a mountainous desert the smart way.

The directions given to the man are, for example, the following:
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

Tests: 
    >>> redirection(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
    ['WEST']

    >>> redirection(["NORTH", "WEST", "SOUTH", "EAST"])
    ["NORTH", "WEST", "SOUTH", "EAST"]

"""

def redirection(arr):
    dir = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}

    for direction in arr:
        if dir[direction]:
            dir.get(direction, dir[direction])
            arr.remove((dir.get(direction, dir[direction])))
            print(arr)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n Well, I'll be hornswaggled! 🤠 You made it across the West, partner! 🌵 \n")
