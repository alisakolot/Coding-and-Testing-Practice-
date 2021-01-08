"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """
    #create list of vowels
    #if the first letter of the word phrase[0] is not in vowels
        #remove the letters from the beginning and add to the end 
        #then add the string 'ay'
    #if the first letter of the phrase is in vowels
        #add 'yay' to the end of the word

    vowels = ['a', 'e', 'i', 'o', 'u']
    phrase = phrase.split(' ')
 
    pl_words = []
    for word in phrase:
        
        if word[0] not in vowels:
            word.replace(word[0], '')
            pl_words.append(word.replace(word[0], '')+word[0]+'ay')
    
        else:
            pl_words.append(word+'yay')

    # print(' '.join(pl_words))   
    return ' '.join(pl_words) 
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. REATGAY OBJAY!\n")
