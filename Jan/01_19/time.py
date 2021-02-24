"""Write a function, which takes a non-negative integer (seconds) 
as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

Test:   
    >>> make_readable(0)
    '00:00:00'

    >>> make_readable(60)
    '00:01:00'

    >>> make_readable(86399)
    '23:59:59'

    >>> make_readable(359999)
    '99:59:59'

    >>> make_readable(80)
    '00:01:20'

"""
def stringify(entity):
    # if < 10
    # if >= 10
    pass
def make_readable(seconds):
    if seconds >= 60:
        if seconds >= 3600:
            hours = seconds/(60 ** 2)
            # print(hours)
            if isinstance(hours, float):
                minutes = (hours-int(hours)) * 60
                # print(minutes)
                if isinstance(minutes, float):
                    seconds = (minutes-int(minutes)) * 60
                    # print(seconds)
        else:
            minutes = seconds / 60
            seconds = round((minutes-int(minutes)) * 60)
    
            min_string = str(minutes)
            sec_string = str(seconds)
            if minutes < 10:
                min_string = '0' + str(int(minutes))
            if seconds < 10: 
                sec_string = '0' + str(int(seconds))
            
            return f'00:{stringify(minutes)}:{stringify(seconds)}'
                
    else:
        
        return f'00:00:{seconds}'
    
    return f"{int(hours)}:{int(minutes)}:{round(seconds)}"

def make_readable_verbose(seconds):
    if seconds >= 60:
        if seconds >= 3600:
            hours = seconds/(60 ** 2)
            # print(hours)
            if isinstance(hours, float):
                minutes = (hours-int(hours)) * 60
                # print(minutes)
                if isinstance(minutes, float):
                    seconds = (minutes-int(minutes)) * 60
                    # print(seconds)
        else:
            minutes = seconds / 60
            seconds = round((minutes-int(minutes)) * 60)
    
            min_string = str(minutes)
            sec_string = str(seconds)
            if minutes < 10:
                min_string = '0' + str(int(minutes))
            if seconds < 10: 
                sec_string = '0' + str(int(seconds))
            
            return f'00:{min_string}:{sec_string}'
                
    else:
        if seconds < 10:
            return f'00:00:0{seconds}'
        return f'00:00:{seconds}'
    
    return f"{int(hours)}:{int(minutes)}:{round(seconds)}"



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("*** U DID IT ***")