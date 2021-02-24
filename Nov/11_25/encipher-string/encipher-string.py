"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""
    print(shift, txt)
    alphabet = ['a', 'b', 'c', 'd', 'e'] 
    alphabet = 'abcdefg'
    alphabet_upper = 'ABCD'

    #iterate through txt, skipping Upper/symbols/numbers

    # string: "abc" shift 1 = "bcd" 
    # shift 2: "cde"
    # shift 3: "dea"
    shift3 = "dea"
    shift = []
    i = 0
    #shift by len(chunk)/3, every time, add to new list
    #when we reach the end of the list/alphabet[-1]
        #add to the beginning/shift[0]

    string = 'ace'
    # result = 'bda'
    # str1 = string[-1] + string[0] + string[1]
    shift = 1
    result = ''
    for x in string:
        # a
        current_index = alphabet.index(x)
        new_index = current_index + shift
        
        # len(alphabet) 
        # new_index == 5
        if new_index > len(alphabet) - 1:
            new_index = new_index - len(alphabet)
        print(x, new_index, alphabet[new_index])
        result+=alphabet[new_index]
    print(result)

    

    
    #for n in range(len(alphabet)):
     #   shift.append(alphabet[(i+n)::(i+n+3)])       
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
