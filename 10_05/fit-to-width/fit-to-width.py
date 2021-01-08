"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""
# spaces_idx=[]
    # for n in range(len(string)):
    #     if n % limit == 0:
    #         spaces_idx.append(n)
    
    # for item in spaces_idx:
    #     if string[item]:
    #         print(' ')


def fit_to_width(string, limit):
    """Print string within a character limit."""
    # while len(string) % limit == 0:
    #     print('\n')
    # word_list =  string.split(' ')
    # dictionary = {}
    
    # word_len = []
    # for word in word_list:
    #     word_len.append(len(word))

    # for k,v in zip(word_list, word_len):
    #     dictionary[k] = v
    # print(dictionary)

    #########################################################################################################################
    word_list = string.split(' ')
    
    lst = []
    for i in range(len(string)):
        if i % limit == 0:
            lst.append(i)
    print(lst)

    for x in lst:
        if string[x] != ' 'and x > 1:
            print(string[::x])

    
    ########################################################################################################################




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
