""" Create a function that sakes an integer argument of seconds 
and converts the value into a string describing how many hours 
and minutes comprise that many seconds.

Any remaining seconds left over are ignored.

Note:
The string output needs to be in the specific form - "X hour(s) and X minute(s)"

3600 --> "1 hour(s) and 0 minute(s)"
3601 --> "1 hour(s) and 0 minute(s)"
3500 --> "0 hour(s) and 58 minute(s)"
323500 --> "89 hour(s) and 51 minute(s)"

Tests:
    >>> to_time(3600)
    '1 hour(s) and 0 minute(s)'

    >>> to_time(3601)
    '1 hour(s) and 0 minute(s)'

    >>> to_time(3500)
    '0 hour(s) and 58 minute(s)'

    >>> to_time(323500)
    '89 hour(s) and 51 minute(s)'
"""

def to_time(seconds): 

   
    hours = seconds // 3600 
    # print(hours)
    rem_minutes = seconds % 3600 
    minutes = rem_minutes // 60
    # print(minutes)
        
    return f"{hours} hour(s) and {minutes} minute(s)"
    


if __name__ == '__main__': 
    import doctest 
    if doctest.testmod().failed == 0: 
        print("\n ✨ WE GOT IT - THIS TIME! ⌚✨ ")