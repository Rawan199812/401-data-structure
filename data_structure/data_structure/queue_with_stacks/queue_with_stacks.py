from data_structure.data_structure.stacks_and_queues.stacks_and_queues import Node, Stack, EmptyQueueException,EmptySatckException

class PseudoQueue:
    def __init__(self):
        self.fisrt_stack = Stack()
    def enqueue(self, value):
        self.fisrt_stack.push(value)
    def dequeue(self):
        reverse_stack = Stack()

        while self.fisrt_stack.top:
            dele = self.fisrt_stack.pop() ## delete the top which is the last one added to the first stack
            reverse_stack.push(dele) ## pop method return the deleted node so I added the deleted one to the second stack

        removed = reverse_stack.pop() 

        while reverse_stack.top:
            dele_last = reverse_stack.pop()

            self.enqueue(dele_last)

        return removed



queue = PseudoQueue()
 
queue.enqueue(" first node ")
queue.enqueue(" 2 node ")  
queue.enqueue(" 30 node ")  
queue.enqueue(" 4 node ") 
queue.enqueue(" 5 node ") 
queue.enqueue(" 6 node ") 

print(queue.fisrt_stack.top.value)
print(queue.dequeue())

print(queue.fisrt_stack.top.value)
print(queue.__str__())