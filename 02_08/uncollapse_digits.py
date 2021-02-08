"""You will be given a string of English digits "stuck" together, like this:

"zeronineoneoneeighttwoseventhreesixfourtwofive"

Your task is to split the string into separate digits:

"zero nine one one eight two seven three six four two five"\

Test: 
    >>> uncollapse("three")
    "three"

    >>> uncollapse("eightsix")
    "eight six"

    >>> uncollapse("fivefourseven")
    "five four seven"

    >>> uncollapse("ninethreesixthree")
    "nine three six three"

    >>> uncollapse("fivethreefivesixthreenineonesevenoneeight")
    "five three five six three nine one seven one eight"


"""

def uncollapse(digits):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = []
    index_list = []
    for number in nums:
        if number in digits:
            lastchar = digits.index(number)
            index_list.append(lastchar)
            result.append(number)
        else:
            print('*')
    
    print(index_list)
    return result


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n 🐬 U DID IT! 🌊 \n")