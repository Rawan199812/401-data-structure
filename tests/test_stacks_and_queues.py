import pytest
from data_structure.data_structure.stacks_and_queues.stacks_and_queues import Node, Queue, Stack, EmptySatckException, EmptyQueueException

stack = Stack()
queue = Queue()
def test_version():
    pass

def test_push_one_onto_a_stack():
    expected = "(first node) => "
    stack.push("first node")
    actual = str(stack)
    assert actual == expected

def test_push_multiple_values_onto_a_stack():
    expected = "(4 node) => (3 node) => (2 node) => (first node) => "
    stack.push("2 node")
    stack.push("3 node")
    stack.push("4 node")
    actual = str(stack)
    assert actual == expected

def test_pop_off_the_stack():
    expected = "(4 node) => (3 node) => (2 node) => (first node) => "
    stack.push("5 node")
    stack.pop()
    actual = str(stack)
    assert actual == expected

def test_empty_a_stack_after_multiple_pops(STK):
    STK.pop()
    STK.pop()
    STK.pop()
    STK.pop()
    with pytest.raises(EmptySatckException):
         STK.pop()

def  test_peek_the_next_item_on_the_stack():
    expected = "4 node"
    actual = stack.peek()
    assert actual == expected

def  test_pop_on_empty_stack_raises_exception(empty_STK):

    with pytest.raises(EmptySatckException):
         empty_STK.pop()

def  test_peek_on_empty_stack_raises_exception(empty_STK):

    with pytest.raises(EmptySatckException):
         empty_STK.peek()

# =========================== Queue tests ========================
def test_enqueue_one_into_a_queue():
    expected = "(first node) => "
    queue.enqueue("first node")
    actual = str(queue)
    assert actual == expected

def test_enqueue_multiple_values_into_a_queue():
    expected = "(first node) => (2 node) => (3 node) => (4 node) => "
    queue.enqueue("2 node")
    queue.enqueue("3 node")
    queue.enqueue("4 node")
    actual = str(queue)
    assert actual == expected

def test_enqueue_off_the_queue():
    expected = "(2 node) => (3 node) => (4 node) => (5 node) => "
    queue.enqueue("5 node")
    queue.dequeue()
    actual = str(queue)
    assert actual == expected

def  test_peek_into_the_queue():
    expected = "2 node"
    actual = queue.peek()
    assert actual == expected


def test_empty_a_queue_after_multiple_dequeues(Qu):
    Qu.dequeue()
    Qu.dequeue()
    Qu.dequeue()
    Qu.dequeue()
    with pytest.raises(EmptyQueueException):
         Qu.dequeue()

def  test_dequeue_on_empty_queue_raises_exception(empty_Qu):

    with pytest.raises(EmptyQueueException):
         empty_Qu.dequeue()

def  test_peek_on_empty_queue_raises_exception(empty_Qu):

    with pytest.raises(EmptyQueueException):
         empty_Qu.peek()









@pytest.fixture
def STK():
    stack = Stack()
    stack.push('first node')
    stack.push("2 node")
    stack.push("3 node")
    stack.push("4 node")

    return stack


@pytest.fixture
def empty_STK():
    empty_stack= Stack()
    empty_stack.push('first node')
    empty_stack.pop()
    return empty_stack

@pytest.fixture
def Qu():
    queue = Queue()
    queue.enqueue('first node')
    queue.enqueue("2 node")
    queue.enqueue("3 node")
    queue.enqueue("4 node")

    return queue


@pytest.fixture
def empty_Qu():
    empty_queue= Queue()
    empty_queue.enqueue('first node')
    empty_queue.dequeue()
    return empty_queue