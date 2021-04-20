""" 
Tests: 
    >>> is_anagram("a")
    True

    >>> is_anagram("banana")
    False

    >>> is_anagram("racecar")
    True 

    >>> is_anagram("arceace")
    True
"""

def is_anagram(string):
    lst = []
    if string == string[::-1]: 
        for item in string: 
            if item not in lst:
                lst.append(item)

            

#  solve with dictionary 

if __name__ == "__main__": 
    import doctest
    if doctest.testmod().failed == 0: 
        print("\n You solved it! \n")

