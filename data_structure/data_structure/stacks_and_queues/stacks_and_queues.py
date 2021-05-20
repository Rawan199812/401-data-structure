class EmptySatckException(Exception):
    def __init__(self):
        print("This stack still empty") 
        # return "This stack still empty"

class EmptyQueueException(Exception):
    def __init__(self):
        print("This Queue still empty") 
        # return "This Queue still empty"

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
            self.top = self.top.next
             
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

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """Method takes any value as argument and adds node with that value to back of queue"""
        node = Node(value)
        if not self.front:
            """If we have empty queue then the first node will be the front and the rear"""
            self.front = node
            self.rear = node
        else:
            """make the last node points to the new"""
            self.rear.next = node
            """make the new node is the back of the queue"""
            self.rear = self.rear.next
    def dequeue(self):
        """Method removes node from front of queue (no args) and returns the node's data"""
        if not self.is_empty():
            result = self.front.value
            self.front = self.front.next
            return result
        else:
            raise EmptyQueueException
    def peek(self):
        """Method (no args) returns the value of the node located in the front of the queue"""
        if not self.is_empty():
            return self.front.value
        else:
            raise EmptyQueueException    

    def is_empty(self):
        """Method (no args) returns a boolean indicating whether or not the queeu is empty"""
        if self.front == None:
            return True
        else:
            return False

    def __str__(self):
        result = ""
        current = self.front
        while current:
            result += f"({current.value}) => "
            current = current.next
        return result
    



        

        
    
stack = Stack()
# stack.push(" first node ")       
# stack.push(" 2 node ")  
# stack.push(" 3 node ")  
# stack.push(" 4 node ")       
# print(stack)
# stack.pop() 
# print(stack)
# print(stack.pop())
# print(stack.peek())
# print(stack.is_empty())
# print(stack)

queue = Queue()
 
# queue.enqueue(" first node ")
# queue.enqueue(" 2 node ")  
# queue.enqueue(" 3 node ")  
# queue.enqueue(" 4 node ") 
# print(queue)
# queue.dequeue()
# print(queue)
# print(queue.peek())

# print(queue.is_empty())

