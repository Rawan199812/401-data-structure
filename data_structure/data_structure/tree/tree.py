from data_structure.data_structure.stacks_and_queues.stacks_and_queues import Queue, EmptyQueueException

# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):
#         self.items.insert(0, item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop()

#     def is_empty(self):
#         return len(self.items) == 0

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1].value


#     def __len__(self):
#         return self.size()

#     def size(self):
#         return len(self.items)

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
    
    def find_maximum_value(self,traversal):
        """
        return the maximum value stored in the tree.
        """
        if self.root:
            max = int(self.root.value)
            returned_list = self.preOrder(self.root,traversal)
            new_list = list(map(int, returned_list))
            for i in new_list:
                if max < new_list[i]:
                     max = new_list[i]
            return max
        else:
            return "empty tree"
    def breadth_first_traversal(self):
        """
        takes a Binary Tree as its unique input. traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.
        """
        if self.root:
            # print(self.root.value)
            list1 = [self.root]
            list2 = []

            while len(list1) > 0:
                # current = list1[1:]
                current = list1.pop(0)
                list2.append(current.value)

                if current.left:
                    list1.append(current.left)
                if current.right:
                    list1.append(current.right)
            list2 = list(map(int, list2))
            return list2
        else:
            return "empty tree"

    # def breadth_first_traversal(self, start):


    #     if start:
    
    #         queue = Queue()
    #         queue.enqueue(start)
    #         result = ""
    #         while len(queue) > 0:
    #             result += str(queue.peek()) 
    #             node = queue.dequeue()

    #             if node.left:
    #                 queue.enqueue(node.left)
    #             if node.right:
    #                 queue.enqueue(node.right)
    #         str_result = list(result)
    #         new_list = list(map(int, str_result))
    #         return new_list



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
# tree = BinaryTree("A")
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
# print(tree_s.root.value)
# print(tree_s.root.right.value)
# print(tree_s.root.left)
# print(tree_s.root.right.right.value)
# print(tree_s.root.right.right.right.value)

# print(tree_s.contains(1))
# Set up tree:
tree = BinaryTree("1")
# tree.root.left = Node("2")
# tree.root.right = Node("3")
# tree.root.left.left = Node("4")
# tree.root.left.right = Node("5")
# tree.root.right.left = Node("6")
# tree.root.right.right = Node("8")
# print(tree.print_tree("preOrder"))
# print("\n\n\n\n")
# print(tree.print_tree("inOrder"))
# print("\n\n\n\n")
# print(tree.print_tree("postOrder"))
# print(tree.find_maximum_value(tree.print_tree("preOrder")))

# print(tree.breadth_first_traversal(tree.root))
# print(tree.breadth_first_traversal())
