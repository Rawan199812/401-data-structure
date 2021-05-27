class Node:
    def __init__(self,value) :
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    returns an array of the values, ordered appropriately
    """
    def __init__(self, root):
        self.root = Node(root)

    def preOrder(self,start,traversal):
        """
        root >> left >> right
        """
        if start: # Check if the current node is empty / null.
            traversal += str(start.value) # Display the data part of the root (or current node)
            if start.left:
              traversal = self.preOrder(start.left, traversal) 
            if start.right:
             traversal = self.preOrder(start.right, traversal)
        return list(traversal)
        
    def inOrder(self,start,traversal):
        """
        left >> root >> right
        """
        if start: # Check if the current node is empty / null.
            if start.left:
                traversal = self.inOrder(start.left, traversal) 
            traversal += str(start.value) # Display the data part of the root (or current node)
            if start.right:
                traversal = self.inOrder(start.right, traversal)
        return list(traversal) 
        
    def postOrder(self,start,traversal):
        """
        left >> right >> root
        """
        if start: # Check if the current node is empty / null.
            if start.left:
                traversal = self.postOrder(start.left, traversal) 
            if start.right:
                traversal = self.postOrder(start.right, traversal)
            traversal += str(start.value) # Display the data part of the root (or current node)
        return list(traversal)  
  
    
    def print_tree(self, traversal_type): # traversal type will be provided when i print the tree
        if traversal_type == "preOrder": # check if the the traversal type is preOrder
            return self.preOrder(tree.root, "") 
        elif traversal_type == "inOrder":
            return self.inOrder(tree.root, "")
        elif traversal_type == "postOrder":
            return self.postOrder(tree.root, "")

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

class BinarySearchTree(BinaryTree):
    

    def add(self, value): 
        """
        accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once
        """

        if not self.root:
            self.root = Node(value)
        else:
            current = self.root

            while current:
                if value < current.value:
                    if current.left == None:
                        current.left = Node(value)
                        break

                    current = current.left

                else:
                    if current.right == None:
                        current.right = Node(value)    
                        break
                    current = current.right
                    

    def contains(self, value):
        """  
        accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once 
        """

        if not self.root:
            raise "empty tree"

        current = self.root

        while self.root:
            if value == current.value:
                
                return True
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                   return False
            else:
                if current.right:
                    current = current.right
                else:

                    return False
# 1. preOrder
# A-B-D-E-C-F-G-
#               A          
#            /     \
#          B         E  
#         /  \     /   \
#        C    D   C     G 
#
# 2. inOrder
# D-B-E-A-F-C-G-
#               A          
#            /     \
#          B         C  
#         /  \     /   \
#        D    E   F     G 
# 3. postOrder
# D-E-B-F-G-C-A-
#               A          
#            /     \
#          B         C  
#         /  \     /   \
#        D    E   F     G 

# Set up tree:
tree = BinaryTree("A")
# tree.root.left = Node("B")
# tree.root.right = Node("C")
# tree.root.left.left = Node("D")
# tree.root.left.right = Node("E")
# tree.root.right.left = Node("F")
# tree.root.right.right = Node("G")
# print(tree.print_tree("preOrder"))
# print(tree.print_tree("inOrder"))
# print(tree.print_tree("postOrder"))
# print(tree.print_tree("wwwwwwwOrder"))
tree_s = BinarySearchTree(1)
tree_s.add(2)
tree_s.add(3)
tree_s.add(4)
tree_s.add(5)
tree_s.add(6)
tree_s.add(7)
tree_s.add(8)
print(tree_s)
print(tree_s.root.value)
print(tree_s.root.right.value)
# print(tree_s.root.left)
print(tree_s.root.right.right.value)
print(tree_s.root.right.right.right.value)

# print(tree_s.contains(1))
# Set up tree:
# tree = BinaryTree("1")
# tree.root.left = Node("2")
# tree.root.right = Node("3")
# tree.root.left.left = Node("4")
# tree.root.left.right = Node("5")
# tree.root.right.left = Node("6")
# tree.root.right.right = Node("7")
# print(tree.print_tree("preOrder"))
# print(tree.print_tree("inOrder"))

