"""
    Tests:
    >>> compressed_string("Hello, world! Cows go moooo...") 
    "Hel2o, world! Cows go mo4.3"

    >>> compressed_string("balloonicorn")
    "bal2o2nicorn"

"""

def compressed_string(string):
    result = ''
   
    for i in range(len(string)-1):
        count = 1 
        if string[i] not in result: 
            result += string[i]
        else:
            if string[i] == string[i+1]: 
                count += 1 
                result += str(count)
    return result

if __name__ == "__main__": 
    import doctest
    if doctest.testmod().failed == 0:
        print("\n You figured it out! good job! \n")

