class EmptySatckException(Exception):
    def __init__(self):
        print("This stack still empty") 
        # return "This stack still empty"

class EmptyQueueException(Exception):
    def __init__(self):
        # print("This Queue still empty") 
        return "This Queue still empty"

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, node = None):
        self.top = node
    def push(self, value):
        """Method adds new node to the top of Stack (take 1 arg = > new value)"""
        if not self.top:
            self.top = Node(value)
        else:
            node = Node(value)
            node.next = self.top
            self.top = node
    def is_empty(self):
        """Method (no args) returns a boolean indicating whether or not the stack is empty"""
        if self.top == None:
            return True
        else:
            return False
    def pop(self):
        """Method removes node from top of Stack (no args) and returns node's data"""

        if not self.is_empty():
            result = self.top.value
            temp = self.top.next
            self.top = temp
            return result
        else:
            raise EmptySatckException
    def peek(self):
        """Method (no args) returns the value of the node located on top of the stack"""
        if not self.is_empty():

            return self.top.value
        else:
            raise EmptySatckException


    def __str__(self):
        result = ""
        current = self.top
        while current:
            result += f"({current.value}) => "
            current = current.next
        return result

        
    
stack = Stack()
stack.push(" first node ")       
stack.push(" 2 node ")  
stack.push(" 3 node ")  
stack.push(" 4 node ")       
print(stack)
# stack.pop() 
# print(stack.pop())
# print(stack.peek())
# print(stack.is_empty())
print(stack)

