"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats:

>>> compress('aabbaabb')
'a2b2a2b2'

If a character appears once, it should not be followed by a number:

>>> compress('abc')
'abc'

The function should handle letters, whitespace, and punctuation:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""


def compress(string):
    """Return a compressed version of the given string."""
        # find char that repeats
        # if the char repeats consec count how many times 
        # return the string with the number of repetitions
    
    compressed = [] 
    current = ''
    count =0 

    for ch in string:
        if ch!= current:
            compressed.append(current)

            if count > 1:
                compressed.append(str(int(count)))

            current = ch
            count = 0
        count += 1 
    compressed.append(current)
    if count > 1:
        compressed.append(str(int(count)))
    return ''.join(compressed)





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
