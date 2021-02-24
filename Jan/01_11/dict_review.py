"""Tests:
    >>> wordcount(poem)
    {'seven': 4, 
        'Kits: 1,
        'sack': 1, 
        'As': 1, 
        'kits': 1,
        'Ives?': 1,
        'How': 1, 
        'St.': 2,
        'had': 3, 
        'sacks':1, 
        'to': 2,
        'going': 2, 
        'was': 1, 
        'cats': 1, 
        'wives': 1, 
        'met': 1, 
        'Every': 3, 
        'with': 1, 
        'man': 1, 
        'a':1, 
        'wife': 1, 
        'I:2, 
        'many': 1, 
        'cat': 1, 
        'Ives': 1, 
        'sacks': 1, 
        'wives.': 1
        'were': 1, 
        'cats':1 
        }
"""

poem = open('test1.txt', 'r')
# poem = 'the cat in the cat'
print(poem)
def wordcount(poem):

    count_words = {}
    # poem = poem.split(' ')
    for word in poem:
        if word in count_words:
            count_words[word] +=1
        else:
            count_words[word] = 1

    print(count_words)         


if __name__== '__main__': 
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ✨Good job practicing dictionaries today!✨ ***")