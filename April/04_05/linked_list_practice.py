class Node(object): 
    def __init__(self, value): 
        self.value = value
        # two pointers: left and right for children 

        self.left =  None
        self.right = None

class BinaryTree(object): 
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        # helper fxn, responsible for printing out the tree and will specify
        #  what type of traversal algorith we want to print tree out on
        # traversal_type: string param
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder": 
            return self.inorder_print(tree.root, "")
        else: 
            print("Traversal type" + str(traversal_type) + "is not supported.")
    
    
    def preorder_print(self, start, traversal):
        # start: node that will be updated on each call of recursive fxn
        # traversal: string that prints out to screen
        '''Root => Left => Right''' 
        if start: 
            traversal += (str(start.value) + "-")
            # every recursive call to the function, as long as start is not None, 
            # => print out the value and add a dash to show dash to show how values are chained  
            
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        
        return traversal 

    # In Order Traversal: Going to the very end of the node first, 
        # then print starting from the end of the node going up
        # left subtree first, then right subtree

    def inorder_print(self, start, traversal):
        """Left=>Root=>Right"""
        if start: 
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    #           1
    #       /    \
        #  2         3 
    #   / \       / \  
    #  4   5     6   7
                    # \
                    #  8

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right =  Node(7)

tree.root.right.right.right = Node(8)

print(tree.print_tree("preorder"))






