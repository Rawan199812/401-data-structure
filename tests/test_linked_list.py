import pytest
from linked_list.linked_list import Node, LinkedList
myList = LinkedList()


# def test_import():
#     assert LinkedList

# def test_import():
#     assert Node

def test_empty_linked_list():
    expected = "Your Linked List still empty"
    actual = str(LinkedList())
    assert actual == expected

def test_insert_properly():
    actual = myList.insert("12")
    expected = "12"
    assert actual == expected
 
def test_head_point_first_node(linked):
    actual = str(linked.head)
    expected = 'Rawan'
    assert actual == expected

def test_insert_multiple_nodes():
    expected = ['so','cool','yes']
    myList = LinkedList()
    actual = [myList.insert('so'),myList.insert('cool'),myList.insert('yes')]
    assert actual == expected

def test_find_value_exists():
    myList = LinkedList()
    myList.insert('great')
    actual = myList.includes('great')
    expected = True
    assert actual == expected

def test_find_value_not_exists():
    actual = myList.includes('close')
    expected = False
    assert actual == expected

def add_to_the_end():
    myList.append('100')
    actual = myList.includes('100')
    expected = False
    assert actual == expected

def test_collection_data(linked):
    expected = "{yes} -> {cool} -> {so} -> {12} -> {Rawan} -> NULL"
    actual = str(linked)
    print(actual)
    assert actual == expected


@pytest.fixture
def linked():
    item = LinkedList()
    item.insert('Rawan')
    item.insert('12')
    item.insert('so')
    item.insert('cool')
    item.insert('yes')



    return item