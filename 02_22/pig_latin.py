"""Pig Latin

    Tests:

    >>> pig_it('Pig latin is cool')
    'igPay atinlay siay oolcay'

    >>> pig_it('Hello world !')     
    'elloHay orldway !'

"""


def pig_it(text):
    result = ''
    
    for word in text:
        new_word = ''
        new_word += word[1:] + word[0] + 'ay'
    result += new_word
    print(result)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n oodgay objay , ouyay idday ityay \n')