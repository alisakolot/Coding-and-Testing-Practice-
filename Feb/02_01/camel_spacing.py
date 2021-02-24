"""Complete the solution so that the function will break up camel casing, using a space between words.
Example

solution("camelCasing")  ==  "camel Casing"

Test:
    >>> spacing("camelCasing")
    'camel Casing'
    
    >>> spacing("helloWorld")
    'hello World'

    >>> spacing("breakCamelCase")
    'break Camel Case'
    
"""


def spacing(s):
    t = '' 
    for char in s:
        if char == char.upper():
            i = s.index(char)
            t += f' {char}'
        else:
            t += char

    return t
if __name__ ==  '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n ✨ You're doing great! ✨ \n")