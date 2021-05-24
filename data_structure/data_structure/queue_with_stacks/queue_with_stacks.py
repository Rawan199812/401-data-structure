from data_structure.data_structure.stacks_and_queues.stacks_and_queues import Stack, EmptyQueueException

class PseudoQueue:
    def __init__(self):
        self.fisrt_stack = Stack()
        self.reverse_stack = Stack()
    def enqueue(self, value):
        self.fisrt_stack.push(value)
    def dequeue(self):

        while self.fisrt_stack.top:
            dele = self.fisrt_stack.pop() ## delete the top which is the last one added to the first stack
            self.reverse_stack.push(dele) ## pop method return the deleted node so I added the deleted one to the second stack

        removed = self.reverse_stack.pop() 

        while self.reverse_stack.top:
            dele_last = self.reverse_stack.pop()

            self.enqueue(dele_last)

        return removed
    def __str__(self):
        result = ""
        if self.fisrt_stack.is_empty():
            current = self.reverse_stack.top
        else:
            current = self.fisrt_stack.top
        while current:
            result += f"({current.value}) => "
            current = current.next
        return result




# queue = PseudoQueue()
 
# queue.enqueue(" first node ")
# queue.enqueue(" 2 node ")  
# queue.enqueue(" 3 node ")  
# queue.enqueue(" 4 node ") 
# queue.enqueue(" 5 node ") 
# queue.enqueue(" 6 node ") 

# print(queue.fisrt_stack.top.value)
# print(queue.dequeue())


# print(queue)