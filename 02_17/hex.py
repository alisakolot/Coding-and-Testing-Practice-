"""The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a 
hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values 
that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3


Tests: 
    >>> rgb(255, 255, 255)
    'FFFFFF'

    >>> rgb(255, 255, 300) 
    'FFFFFF'

    >>> rgb(0,0,0) 
    '000000'

    >>> rgb(148, 0, 211) 
    '9400D3'

"""

# def rgb(r, g, b):
#     return '%02x%02x%02x' % rgb

def rgb(r, g, b):
    return f'%02{r}%02{g}%02{b}' % rgb
# rgb_to_hex((255, 255, 195))





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n 🌈🌈🌈 C o l o r s! 🌈🌈🌈 \n')