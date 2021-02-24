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
    # >>> word_mesh(["beacon", "condominium", "umbilical", "california"])
    # 'conumcal'

    # >>> word_mesh(["allow", "lowering", "ringmaster", "terror"]) 
    # 'lowringter'

    >>> word_mesh(["allow", "lowering"])
    'low'

    >>> word_mesh(["a", "a"])
    'a'

    >>> word_mesh(["abba", "abab"])
    'a'

    >>> word_mesh(['abc', 'xyz'])
    "failed to mesh"
"""
# Pseudocode:
# 1. Iterate through the list 
# 2. Each item ending needs to be compared to the following item in the list
# 3. Iterate in reverse through the last char of item at prev index
# 4.  If the items match then add them to a string 
# 5. When the items stop matching then append the string to a results list

def word_mesh(words):
    # for i in range(len(words)-1):
    #     for rev in words[i][::-1]:
    #         # print(rev, ' *')
    #         if rev == words[i][-(i+1)]:
    #             print('match found:', rev, words[i][-(i+1)])
    #         else:
    #             print('stop')
    # print(words)
    if len(words) <= 1:
        return "failed to mesh"

    # ["allow", "lowering"]
    string = 'll' 
    allow
    lowering 

    elif len(words) == 2: 
   
        item1 = words[0][::-1]
        item2 = words[1]

        # string = ''
        # for char in item1:
        #     if char in item2:
        #         if char not in string:
        #             string += char

        word_lengths = []
        for item in words:
            word_lengths.append(len(item))
        
        string = ''
        for i in range(min(word_lengths)):
            if item1[i] == item2[i]:
                string += item1[i]
            else:
                break
        
        print(string[::-1])

        








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n Great Job! \n')