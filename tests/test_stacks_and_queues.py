import pytest
from data_structure.data_structure.stacks_and_queues.stacks_and_queues import Node, Stack, EmptySatckException, EmptyQueueException

stack = Stack()
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
    stack.push("(5 node)")
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