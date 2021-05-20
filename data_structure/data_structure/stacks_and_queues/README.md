# Stacks and Queues
**Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle.**
 
**Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.**

## Challenge

***Create Queue and Stack classes and implemente the (Stack and Queue data structure ) with common methods used with it***

## Approach & Efficiency 
- I implemented both data structures ( stack && queue) using a basic node class with a next and a value set to none

**For the stack, I created a class Stack() and initialized it with self and top properties then do the other methods in the class**

**For the queue, I created a class Queue() and initialized it with self and front and rear properties ten i do the other methods in this class**


## API

**Stack class has 4 methods:**

- pop() Since stacks use a last in first out approach, this method removes the item on top of the stack by setting its pointer to self.top.next. 

- push() This method pushes a new node onto the stack by setting the current top node as the incoming node's next, then setting the new node as self.top This method takes in a single value as its only parameter

- peek() This method returns the value at the top of the stack, if it exists

- is_empty() Checks if self.front exists and returns a boolean


**Queue class has 4 methods:**

- enqueue() Appends a node to the end of the queue by pointing the current rear (if it exists) to the new node, and assigning self.rear to the new node.

- dequeue() removes a node from the front of the queue, if the queue is empty, I print a message and return the empty queue.

- peek() This method returns the value at the front of the stack, if it exists

- is_empty() Checks if self.front exists and returns a boolean