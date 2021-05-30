from data_structure.data_structure.tree.tree import Node, BinaryTree, BinarySearchTree
from data_structure.data_structure.tree.tree import BinarySearchTree
import pytest
from unittest.mock import patch

# ===================== BinaryTree Tests ===============

@patch('builtins.print')
def test_print_preOrder(mock_print):
    tree = BinaryTree("1")
    tree.root.left = Node("2")
    tree.root.right = Node("3")
    tree.root.left.left = Node("4")
    tree.root.left.right = Node("5")
    tree.root.right.left = Node("6")
    tree.root.right.right = Node("7")
    print(tree.print_tree("preOrder"))
    mock_print.assert_called_once_with(['1', '2', '4', '5', '3', '6', '8'])

@patch('builtins.print')
def test_print_inOrder(mock_print):
    tree = BinaryTree("1")
    tree.root.left = Node("2")
    tree.root.right = Node("3")
    tree.root.left.left = Node("4")
    tree.root.left.right = Node("5")
    tree.root.right.left = Node("6")
    tree.root.right.right = Node("7")
    print(tree.print_tree("inOrder"))
    mock_print.assert_called_once_with(['4', '2', '5', '1', '6', '3', '8'])

@patch('builtins.print')
def test_print_postOrder(mock_print):
    tree = BinaryTree("1")
    tree.root.left = Node("2")
    tree.root.right = Node("3")
    tree.root.left.left = Node("4")
    tree.root.left.right = Node("5")
    tree.root.right.left = Node("6")
    tree.root.right.right = Node("7")
    print(tree.print_tree("postOrder"))
    mock_print.assert_called_once_with(['4', '5', '2', '6', '8', '3', '1'])


@patch('builtins.print')
def test_print_maximum_value(mock_print):
    tree = BinaryTree("1")
    tree.root.left = Node("2")
    tree.root.right = Node("3")
    tree.root.left.left = Node("4")
    tree.root.left.right = Node("5")
    tree.root.right.left = Node("6")
    tree.root.right.right = Node("7")
    tree.root.right.right = Node("8")
    print(tree.find_maximum_value(tree.print_tree("preOrder")))
    mock_print.assert_called_once_with(8)

# needs a root to work 
   
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


def test_one_root_tree():
    tree = BinaryTree(1)
    assert tree.root.value == 1  


# ===================== BinarySearchTree Tests ===============

def test_BinarySearchTree_contains(tree_s):
    tree_s = BinarySearchTree(1001)
    tree_s.add(300)
    tree_s.add(-1)
    tree_s.add(15)
    assert tree_s.contains(-6) == False
    assert tree_s.contains(300) == True
    assert tree_s.contains(-5) == False
    assert tree_s.contains(-1) == True
    assert tree_s.contains(10) == False 
    assert tree_s.contains(15) == True 

def test_add_node_to_BinarySearchTree(tree_s):

    tree_s.add(9)
    tree_s.add(66)

    assert tree_s.root.value == 15
    assert tree_s.root.left.value == 9
    assert tree_s.root.right.value == 66

@pytest.fixture
def tree_s():
    tree_s = BinarySearchTree(15)

    return tree_s