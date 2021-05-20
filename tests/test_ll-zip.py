
import pytest
from data_structure.data_structure.ll_zip.ll_zip import zipLists
from data_structure.data_structure.linked_list.linked_list import Node, LinkedList
def test_version():
    pass


@pytest.fixture
def prepare_data():
    anime = LinkedList()
    node1 = anime.append("BLEACH")
    node2 = anime.append("God of high school")
    node3 = anime.append("Deat note")
    test1= anime.includes("BLEACH")
    test2= anime.includes("Conan")
    return {'anime':anime,"node1":node1,"node2":node2,"node3":node3,"test1":test1,"test2":test2}


def test_empty_ll():
    expected =LinkedList().__str__()
    actual ='Your Linked List still empty'
    assert expected == actual


def test_insert_ll():
    """
    Can properly insert into the linked list ?
    """
    anime = LinkedList()
    anime.insert("Slam Dunk")
    expected =anime.head.data
    actual ='Slam Dunk'
    assert expected == actual


def test_head_ll():

    anime = LinkedList()
    anime.insert("test head")
    expected =anime.head.data
    actual ='test head'
    assert expected == actual



def test_insert_multiple_nodes():
    anime = LinkedList()
    anime.insert("Abu")
    anime.insert("Rawan")
    expected =anime.__str__()
    actual ='(Rawan) -> (Abu) -> NULL'
    assert expected == actual



def test_include_true(prepare_data):

    expected =prepare_data['test1'].__str__()
    actual ='True'
    assert expected == actual



def test_include_false(prepare_data):
   
    expected =prepare_data['test2'].__str__()
    actual ='False'
    assert expected == actual

def test_values_in_linked_list(prepare_data):
 
    expected =prepare_data['anime'].__str__()
    actual ='(BLEACH) -> (God of high school) -> (Deat note) -> NULL'
    assert expected == actual


def test_insertbefore_first_node():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.insertBefore("Slam dunk","one puch man")
    assert anime.__str__() == '(one puch man) -> (Slam dunk) -> (death note) -> NULL'

def test_insertAfter_lastnode():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.insertAfter("death note","one puch man")
    assert anime.__str__() == '(Slam dunk) -> (death note) -> (one puch man) -> NULL'


def test_insertAfter():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.append("Naruto")
    anime.insertAfter("death note","one puch man")
    assert anime.__str__() == '(Slam dunk) -> (death note) -> (one puch man) -> (Naruto) -> NULL'



def test_kth_from_end1_Happy_Path():
    anime = LinkedList()
    anime.append(1)
    anime.append(3)
    anime.append(8)
    anime.append(2)
    assert anime.kthFromEnd(3) == 1
    assert anime.kthFromEnd(1) == 8


def test_kth_from_end_greater_than_length():
    anime = LinkedList()
    anime.append(1)
    anime.append(3)
    anime.append(8)
    anime.append(2)
    assert anime.kthFromEnd(5) =='The Value Not Found'


def test_kth_from_end_size1():
    anime = LinkedList()
    anime.append(3)
    assert anime.kthFromEnd(0) ==3
