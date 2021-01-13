"""In this kata, you have an input string and you should check whether 
it is a valid message. To decide that, you need to split the string by 
the numbers, and then compare the numbers with the number of characters 
in the following substring.


Tests: 

    >>> is_a_valid_message("3hey5hello2hi")
    True

    >>> is_a_valid_message("")
    True

    >>> is_a_valid_message("3hey5hello2hi5")
    False
"""

def is_a_valid_message(message):
    # your code
    pass

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("✨G 0 0 D J 0 B✨")