'''Object Orientation'''

# class MyObject:
#     def __init__(self, data):
#         self.columns = data
#         self.rows = None
#         self.attribute_name = ...

# class MyCar:
#     def __init__(self, automatic, miles):
#         self.transmission = automatic #boolean
#         self.mileage = miles
#         self.preowned = False 
    
#     def sell(self, min_price):
#         self.min_price = min_price

#     def __repr__(self, automatic, miles, min_price):
#         #printable format
#         pass
        

# xyz = MyCar(True, 123)
# abc = MyCar(False, 999)

# xyz.sell(20000) # equivalent to calling sell(xyz, 20000)
# abc.sellf(5000)

#Think of objects that have methods. The only thing that they have are 
#the attributes.
#Instances are 'singular examples' of class
#create linked list of one million elements

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def print_reverse(self):
        if self.next == None:
            print(self.data)
        else:
            self.next.print_reverse() 
            print(self.data)
    

    def __repr__(self):
        return self.data
    
    

class LinkedList:
    def __init__(self):
        self.head = None
    
                    

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# llist = LinkedList()
# llist
# None
llist = LinkedList()
first_node = Node('a')
llist.head = first_node

second_node = Node("b")
third_node = Node("c")

first_node.next = second_node
second_node.next = third_node

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    
#     def print_reverse(self):
#         if self.next == None:
#             print(self.data)
#         else:
#             print(self.data)
#             self.data.print_reverse()
    
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
#             node=node.next
#         nodes.append("None")
#         return ' -> '.join(nodes)

