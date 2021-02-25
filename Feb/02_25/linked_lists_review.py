class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_ll(self, data):
        if head == None:
            head = self.data

        current = self.data
        while self.data != None:
            current = current.next
    
    def add_new_head(self, data):
        new_head = self.data
        new_head.next = head
        head = new_head
    
    def delete(self, data):
        if head == None:
            return "No thoughts. Head empty."
        if head.data == data: # if we want to delete the head, reset the node to the next node
            head = head.next
            

        current = self.head
        
        # to avoid running off the edge of the linked list
        while current.next != None:
            if current.next.data == data #  the data we are trying to delete,if the next value is the one we are trying to delete
                current.next = current.next.next # cutting out the next value
                # if the next you want to delete, walk around it to get to the node you want
            
            current = current.next
    


            
