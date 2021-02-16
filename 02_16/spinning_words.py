"""Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter 
words reversed (Just like the name of this Kata). Strings passed
in will consist of only letters and spaces. Spaces will be 
included only when more than one word is present.

Tests:
>>> spin_words('Welcome') 
'emocleW'

>>> spin_words('Hey fellow warriors') 
'Hey wollef sroirraw'

>>> spin_words('This is a test') 
'This is a test'

>>> spin_words('This is another test')
'This is rehtona test'

"""

def spin_words(sentence):
    word_lst = sentence.split()
    result = ''
    for item in word_lst:
        if len(item) >= 5:
            result += item[::-1] + ' '
        else:
            result += item + ' '
            
    return result[:-1]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n You mixed up all the words \n')