class Node:
    # constructor
    def __init__(self, data, next =  None):
        self.data = data
        self.next = next

# Creating a single node 
# first = Node(3)
# print(first.data)

# Linked List with a single head node
class LinkedList:
    def __init__(self):
        self.head = None


# Insert method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next  = newNode
        else: 
            self.head = newNode

# Print method for the linked list
    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Linked list with a single node 
# LL = LinkedList()
# LL.head = Node(3)
# print('Linked List head, single node:', LL.head.data)

# Linked list node insertion:
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()