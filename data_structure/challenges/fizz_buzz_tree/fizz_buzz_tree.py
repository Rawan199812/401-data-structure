
from data_structure.data_structure.stacks_and_queues.stacks_and_queues import Queue
from data_structure.data_structure.tree.tree import Node, BinaryTree

# def FizzBuzzTree():
#     tree = BinarySearchTree()
#     pass
# def FizzBuzzTree(tree):
#     """
#     k-ary : can have any number of nodes
#     """
#     if tree.root != None:
#         pass

#     else:
#         tree.root =Node('Tree is Empty')
        # return tree
# tree = BinaryTree("1")
# tree.root.left = Node("2")
# tree.root.right = Node("3")
# tree.root.left.left = Node("4")
# tree.root.left.right = Node("5")
# tree.root.right.left = Node("6")
# tree.root.right.right = Node("8")


def FizzBuzzTree(tree):
    new_tree = tree
    lst = []
    if new_tree.root is not None:

        def inner(node):
            if node.value %3==0 and node.value%5==0:
                lst.append('FizzBuzz')
            elif node.value%3==0:
                lst.append('Fizz')
                # print(node.value)
            elif node.value%5==0:
                lst.append('Buzz')
            else :
                lst.append(str(node.value))
            if node.left:
                inner(node.left)
            if node.right:
                inner(node.right)
        

        inner(new_tree.root)
        return lst
      
    else:
        new_tree.root =Node('Empty Tree')
        return new_tree
    

if __name__ == "__main__":
    b_tree = BinaryTree(1)
    b_tree.root = Node(2)
    b_tree.root.right = Node(6)
    b_tree.root.left = Node(7)
    b_tree.root.right.left = Node(9)
    b_tree.root.right.right = Node(15)
    b_tree.root.left.left = Node(3)
    b_tree.root.left.right = Node(8)
    print(FizzBuzzTree(b_tree))
