# Challenge Summary
Create a binary tree class that can return a collection from a preorder traversal, a collection from an inorder traversal, collection from a postorder traversal and a max method to find the maximum value in a binary tree.
And create a binary search tree that can add a node in its correct location and search for a given value through tree nodes
## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
Binary Tree:
- preOrder(): return a collection from a preorder traversal
- inOrder():  return a collection from an inorder traversal
- postOrder():  return a collection from a postorder traversal
- print_tree() :  return collection passed on the traversal order methodes 
- find_maximum_value() : return the maximum value in a Binary Tree


Binary Search Tree:

-  add(value) accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

- contains(value) accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

## Solution

1. preOrder
**[A, B, D, E, C, F, G]**
#               A          
#            /     \
#          B         E  
#         /  \     /   \
#        C    D   C     G 


2. inOrder
**[D, B, E, A, F, C, G]**
#               A          
#            /     \
#          B         C  
#         /  \     /   \
#        D    E   F     G 


3. postOrder
**[D, E, B, F, G, C, A]**
#               A          
#            /     \
#          B         C  
#         /  \     /   \
#        D    E   F     G 
