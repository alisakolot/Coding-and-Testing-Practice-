reversellinplace_weds_review.py

class LinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return '{data} -> {next}'.format(
                data=self.data, 
                next=self.next,
            )

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        return self.head.__repr__()
    
    def is_empty(self):
        return self.size == 0

    def insert_at_head(self, data):
        new_node = self.Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self._head
            self.head = new_node
        
        self.size += 1

    def append(self, data):
        new_node = self.Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    
    def pop(self):
        current = self.head
        previous = None

        while current.next:
            previous = current
            current = current.next
        
        if previous:
            previous.next = None
            self.tail = previous
        else:
            self.head = None
            self.tail = None
        
        self.size -= 1
        return current.data

def reverse(lst):

  # identify the head 
  # identify previous 
  # set previous to next 
  
    current = lst.head #1
    previous = None 
    #   lst.head = head.next
    while current:
        next = current.next # None
        current.next = previous # 4 -> 3
        previous = current # previous = 4
        current = next # None

    return previous

# None < - 1     

  #head.next 

  #end = None
  #end.next = 
    #current, previous, next 
   
# 1 -> 2 -> 3 -> 4 -> None
# None <- 1 <- 2 <- 3 <- 4

# Ex. 1
ll = LinkedList()
for i in range(5):
    ll.append(i)
 
print('Pre-reversed: ', ll)
print('Reversed: ', reverse(ll))
 
# Ex. 2
ll = LinkedList()
ll.append(0)
 
print('\nPre-reversed: ', ll)
print('Reversed: ', reverse(ll))


