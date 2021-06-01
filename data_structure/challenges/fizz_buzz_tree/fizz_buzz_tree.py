from data_structure.data_structure.tree.tree import Node, BinaryTree

# def FizzBuzzTree():
#     tree = BinarySearchTree()
#     pass
def FizzBuzzTree(tree):
    new_tree = tree
    if new_tree.root != None:
        pass

    else:
        new_tree.root =Node('Tree is Empty')
        return new_tree
tree = BinaryTree("1")
tree.root.left = Node("2")
tree.root.right = Node("3")
tree.root.left.left = Node("4")
tree.root.left.right = Node("5")
tree.root.right.left = Node("6")
tree.root.right.right = Node("8")
print(tree.breadth_first_traversal(FizzBuzzTree(tree)))