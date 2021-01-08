# '''def binary_search(val):
#     """Using binary search, find val in range 1-100. Return # of guesses."""

#     assert 0 < val < 101, "Val must be between 1-100"

#     num_guesses = 0
#     highest=101
#     lowest=0
#     guess = None

#     while guess!=val:
#         num_guesses+=1
#         guess = (highest-lowest)//2 + lowest

#         if val>guess:
#             lowest = guess
        
#         if val<guess:
#             highest = guess

#     return num_guesses


'''Create A Linked List'''

# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     def print_recursive(self, data):
#         pass 

#     def print_reverse(self):
#         if self.next == None:
#             print(self.data)
#             #if there is nothing in the last node print the last node
#         else:
#             self.data.print_reverse() #if there is data in the node print the current node, 
#                                         #after checking that the last has nothing in it
#             print(self.data)   
        


#     def __repr__(self):
#         return self.data

# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def __repr__(self):
#         node = self.head
#         nodes = []

#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append('None') #repr the last empty node
#         return ' -> ' ''.join(nodes) #display nodes as a string 


# llist = LinkedList()
# first_node = Node('a')
# llist.head = first_node

'''Count list recursively'''

# def count_recursively(lst):
#     """Return number of items in a list, using recursion."""
#     if not lst:
#         return 0 
#     return 1 + count_recursively(lst[1:])

'''In this challenge, you’ll write a decoder.
A valid code is a sequence of numbers and letters, always starting with a number and ending with letter(s).
Each number tells you how many characters to skip before finding a good letter. After each good letter should come the next next number.
For example, the string “hey” could be encoded by “0h1ae2bcy”. This means “skip 0, find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.
A single letter should work'''


# def decode(s):
#     """Decode a string."""
#     s = s.split() 

#     #S will result in a list of strings
#     # S = [‘2’,’a’,’b’,’h’]

#     num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     remove_string = []

#     for item in s:
#         if item in num:
#             remove_string.append(int(item)+1)
    
 
#     #Remove_string = [3]  # list of lengths of strings that need to be removed from given strings
#     #the resulting number can be used as the length of the string that needs to be removed
#         # From s to get to the next letter
    
#     # list of lengths of strings that need to be removed from given strings 
        
#     result_list = [] 
#     #removing the string of extra characters using the lengths (use indexing) provided remove_strng
#     #[1,2,3]
#     i=0
#     for length in remove_string:
#         result_list.append(s[length]) 
#         # [length[i]:length[i+1]+1]

#     #Result_list = [‘h’]

#     decoded_word = ''.join(result_list)

#     return decoded_word

# decode("0h")
# # 'h'

# decode("2abh")
# # 'h'

# # decode("0h1ae2bcy")
# # 'hey'
# decode("0h1ae2bcy")

'''Fit String to Width'''
def fit_to_width