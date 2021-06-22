from data_structure.data_structure.hashtable.hashtable import Hashtable
from data_structure.data_structure.tree_intersection.tree import BinaryTree, Node

## With hashmap and tree

# def tree_intersection(tree_one, tree_two):

#     tree_one_list = tree_one.pre_order()
#     tree_two_list = tree_two.pre_order()
#     # print(tree_one_list)
#     # print(tree_two_list)

#     repeated = []
#     hashmap = Hashtable()
#     for element in tree_one_list:
#         if not hashmap.contains(element):
#             hashmap.add(str(element), 'l')

#     for element in tree_two_list:
#         if hashmap.contains(element):
#             repeated.append(str(element))
#     return repeated

## With tree
def tree_intersection(tree_1,tree_2):
    if not tree_1.root == None or not tree_2.root == None:
        list_tree_1 = tree_1.pre_order() 
        list_tree_2 = tree_2.pre_order() 
        repeated = []
        for i in list_tree_1:
            if i in list_tree_2:
                repeated.append(i)
        if len(repeated) > 0:
            return repeated
        else:
            return 'No matches was found'
    else:
        return 'Empty Tree'
tree1 = BinaryTree()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(50)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(30)
tree1.root.right.left = Node(6)
tree1.root.right.right = Node(8)

tree2 = BinaryTree()
tree2.root = Node(9)
tree2.root.left = Node(2)
tree2.root.right = Node(300)
tree2.root.left.left = Node(40)
tree2.root.left.right = Node(50)
tree2.root.right.left = Node(60)
tree2.root.right.right = Node(10)
# tree_intersection(tree1,tree2)
tree3 = BinaryTree()
tree4 =BinaryTree()
print(tree_intersection(tree4,tree3))


