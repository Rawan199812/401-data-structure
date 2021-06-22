import re
from data_structure.data_structure.tree_intersection.tree_intersection import *
from data_structure.data_structure.tree_intersection.tree import Node , BinaryTree
import pytest

def test_tree_intersection_1(tree1):
    expected = [50,2]
    tree1,tree2 = tree1
    actual = tree_intersection(tree1,tree2)
    assert expected == actual


@pytest.fixture
def tree_1():
    tree1 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(50)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(30)
    tree1.root.right.left = Node(6)
    tree1.root.right.right = Node(8)
    return tree1

@pytest.fixture
def tree_2():

    tree2 = BinaryTree()
    tree2.root = Node(9)
    tree2.root.left = Node(2)
    tree2.root.right = Node(300)
    tree2.root.left.left = Node(40)
    tree2.root.left.right = Node(50)
    tree2.root.right.left = Node(60)
    tree2.root.right.right = Node(10)
    return tree2
@pytest.fixture
def tree_3():
    tree3 = BinaryTree()
    return tree3

@pytest.fixture
def tree3():
    tree4 =BinaryTree()

    return tree4
