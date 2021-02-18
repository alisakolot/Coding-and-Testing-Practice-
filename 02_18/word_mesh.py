"""You will be given an array of strings. The words in the array should mesh together 
where one or more letters at the end of one word will have the same letters 
(in the same order) as the next word in the array. But, there are times when all the words won't mesh.

Examples of meshed words:
"apply" and "plywood"

Examples of words that don't mesh:
"apply" and "playground"

If all the words don't mesh together, then your code should return "failed to mesh".

Input: An array of strings. There will always be at least two words in the input array.

Output: Either a string of letters that mesh the words together or the string "failed to mesh".


Tests:
    >>> word_mesh("beacon", "condominium", "umbilical", "california"])
    'conumcal'

    >>> word_mesh(["allow", "lowering", "ringmaster", "terror"]) 
    'lowringter'

"""

def word_mesh(words):
    pass



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n Great Job! \n')