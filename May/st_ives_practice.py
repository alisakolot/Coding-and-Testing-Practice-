""" Create Count Dictionary: 
As I was going to St. Ives
I met a man with seven wives
Every wife had seven sacks
Every sack had seven cats
Every cat had seven kits
Kits, cats, sacks, wives.
How many were going to St. Ives?

Tests: 
    >>> count_dictionary(st_ives)
    word_count = {'seven': 4,
    'Kits': 1, 'sack': 1, 'As': 1, 'kits': 1, 'Ives?': 1, 'How': 1, 'St.': 2,
    'had': 3, 'sacks': 1, 'to': 2, 'going': 2, 'was': 1, 'cats': 1, 'wives': 1, 
    'met': 1, 'Every': 3, 'with': 1, 'man': 1, 'a': 1, 'wife': 1, 'I': 2, 'many': 1, 
    'cat': 1, 'Ives': 1, 'sacks': 1, 'wives.': 1, 'were': 1, 'cats': 1}

"""
st_ives = "As I was going to St. Ives\nI met a man with seven wives\nEvery wife had seven sacks\nEvery sack had seven cats\nEvery cat had seven kits\nKits, cats, sacks, wives.\nHow many were going to St. Ives?"

def count_dictionary(st_ives): 
    lines = st_ives.split("\n")
    words = []
    word_count = {}
    sorted_word_count = {}

    for line in lines: 
        for word in line.split(" "): 
            words.append(word)

    for item in words: 
        if item not in word_count: 
            word_count[item] = 1
        else: 
            word_count[item] += 1
    

if __name__ == "__main__": 
    import doctest
    if doctest.testmod().failed == 0: 
        print('\n You counted the cats! \n')

