import pytest
from data_structure.data_structure.queue_with_stacks.queue_with_stacks import PseudoQueue, EmptyQueueException

queue = PseudoQueue()
def test_version():
    pass


def test_enqueue_one_into_a_queue():
    expected = "(first node) => "
    queue.enqueue("first node")
    actual = str(queue)
    assert actual == expected

def test_enqueue_multiple_values_into_a_queue():
    expected = "(4 node) => (3 node) => (2 node) => (first node) => "
    queue.enqueue("2 node")
    queue.enqueue("3 node")
    queue.enqueue("4 node")
    actual = str(queue)
    assert actual == expected

def test_enqueue_off_the_queue():
    expected = "(5 node) => (4 node) => (3 node) => (2 node) => "
    queue.enqueue("5 node")
    queue.dequeue()
    actual = str(queue)
    assert actual == expected















@pytest.fixture
def Qu():
    queue = PseudoQueue()
    queue.enqueue('first node')
    queue.enqueue("2 node")
    queue.enqueue("3 node")
    queue.enqueue("4 node")

    return queue


@pytest.fixture
def empty_Qu():
    empty_queue= PseudoQueue()
    empty_queue.enqueue('first node')
    empty_queue.dequeue()
    return empty_queue