"""Given a variable name in snake_case, return camelCase of name.

For example::

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

"""


def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""
    
    #find the index of the character after the _
    #capitalize that char
    #remove the _

    variable_name = list(variable_name)
    x = variable_name.index('_')
    y = []
    print(variable_name[x+1].upper())
    print(variable_name[x])

    for ch in variable_name:
        if ch != '_':
            y.append(ch)

    y.insert(x+1, variable_name[x+1].upper())
    return y
        
   



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
