from data_structure.data_structure.tree.tree import Node, BinaryTree, BinarySearchTree
from data_structure.data_structure.tree.tree import BinarySearchTree



from unittest.mock import patch

@patch('builtins.print')
def test_print(mock_print):
    # The actual test
    tree = BinaryTree("1")
    tree.root.left = Node("2")
    tree.root.right = Node("3")
    tree.root.left.left = Node("4")
    tree.root.left.right = Node("5")
    tree.root.right.left = Node("6")
    tree.root.right.right = Node("7")
    tree.print_tree("preOrder")
    mock_print.assert_called_once_with(1,2,3,4)
   


    # Showing what is in mock
    # import sys
    # sys.stdout.write(str( mock_print.call_args ) + '\n')
    # sys.stdout.write(str( mock_print.call_args_list ) + '\n')
    


# def test_empty_tree():
#     tree = BinaryTree()
#     assert tree.root == None


def test_one_root_tree():
    tree = BinaryTree(1)
    assert tree.root.value == 1

def test_add_left_child():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    assert tree.root.left.value == 2

def test_add_right_child():
    tree = BinaryTree(1)
    tree.root.right = Node(3)
    assert tree.root.right.value == 3

# def test_collection_preorder_traversal():
#     tree = BinaryTree("1")
#     tree.root.left = Node("2")
#     tree.root.right = Node("3")
#     tree.root.left.left = Node("4")
#     tree.root.left.right = Node("5")
#     tree.root.right.left = Node("6")
#     tree.root.right.right = Node("7")
#     actual = tree.preOrder(tree,"preOrder")
#     assert actual == 3

