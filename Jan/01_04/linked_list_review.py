# Node Class
class Node:

    # Function to initialize node object
    def __init__(self, data):
        self.data = data #assign data to each node
        self.next = None  #initialize next node as null/establish the endpoint of a list

# Linked list class
class LinkedList:
    # function to initialize the Linked list object
    def __init__(self):
        self.head = None


    def print(self):
        curr = self.head
        while curr:
            print(curr.data) # get the data of each node
            curr = curr.next



llist = LinkedList() 

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third


