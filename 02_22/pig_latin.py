"""Pig Latin

    Tests:

    >>> pig_it('Pig latin is cool')
    'igPay atinlay siay oolcay'

    >>> pig_it('Hello world !')     
    'elloHay orldway !'

"""


def pig_it(text):
    text = text.split()
    result = ''
    
    for word in text:
        if word.isalpha():
            result += word[1:] + word[0] + 'ay '
        else:
            result += word

    return result.strip()


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n oodgay objay , ouyay idday ityay \n')