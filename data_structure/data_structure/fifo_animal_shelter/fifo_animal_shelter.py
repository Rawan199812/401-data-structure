from data_structure.data_structure.stacks_and_queues.stacks_and_queues import *
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None

#     def enqueue(self, value):
#         """Method takes any value as argument and adds node with that value to back of queue"""
#         node = Node(value)
#         if not self.front:
#             """If we have empty queue then the first node will be the front and the rear"""
#             self.front = node
#             self.rear = node
#         else:
#             """make the last node points to the new"""
#             self.rear.next = node
#             """make the new node is the back of the queue"""
#             self.rear = self.rear.next
#             # self.rear = node
#     def dequeue(self):
#         """Method removes node from front of queue (no args) and returns the node's data"""
#         if not self.is_empty():
#             result = self.front.value
#             self.front = self.front.next
#             return result
#         else:
#             raise EmptyQueueException
#     def peek(self):
#         """Method (no args) returns the value of the node located in the front of the queue"""
#         if not self.is_empty():
#             return self.front.value
#         else:
#             raise EmptyQueueException    

#     def is_empty(self):
#         """Method (no args) returns a boolean indicating whether or not the queeu is empty"""
#         if self.front == None:
#             return True
#         else:
#             return False

#     def __str__(self):
#         result = ""
#         current = self.front
#         while current:
#             result += f"({current.value}) => "
#             current = current.next
#         return result
    

# class Animal:
#     def __init__(self, name, type):
#         self.value = name
#         self.type = type
#         self.next = None

# class Cat(Animal)):
#     self.type= "cat"

# class Dog(Animal):
#     self.type= "dog"

    

# class AnimalShelter:
#     def __init__(self):
#         self.queue_cat = Queue()
#         self.queue_dog = Queue()

#     def enqueue(self, *animal):

#         for i in animal:
#             if isinstance(i, Cat):
#                 self.queue_cat.enqueue(i)
           
#             elif isinstance(i, Dog):
#                 self.queue_dog.enqueue(i)
#             else:
#                 return "only cats and dogs"
#     def dequeue(self, pref):
  
#         animal = None

#         while not self.queue_cat.is_empty():
#             if self.queue_cat.front.type == pref and animal == None:
#                 animal= self.queue_cat.dequeue()
#             else:
#                 self.queue_dog.enqueue(self.queue_cat.dequeue())

#         while not self.queue_dog.is_empty():
#             self.queue_cat.enqueue(self.queue_dog.dequeue())

#         return animal
        
    # def __str__(self):
    #     result = ""
    #     current = self.front
    #     while current:
    #         result += f"({current.value}) => "
    #         current = current.next
    #     return result



# dog1 = Dog('dd')
# dog2 = Dog("rex")
# cat1 = Cat("pussy")
# cat2 = Cat('suz')

    
# shelter = AnimalShelter()
# print(shelter.enqueue(dog1))
# shelter.enqueue(dog1)
# shelter.enqueue(dog1)
# # print(shelter.enqueue("ds"))
# # print(shelter.queue_dog.front.value)
# print(shelter.dequeue("dog"))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Dog : 
    def __init__(self , name) :
        self.name = name 

    def __str__(self):
        return 'dog'

class Cat : 
    def __init__(self , name) :
        self.name = name 

    def __str__(self):
        return 'cat'


class AnimalShelter : 

    def __init__(self):
        self.queue_dog = Queue()
        self.queue_cat = Queue()

    def enqueue(self, animal):

        if  str(animal) == "dog" :
             self.queue_dog.enqueue(animal) 
        elif  str(animal) == "cat" :
             self.queue_cat.enqueue(animal) 
        else :
             return "only cats and dogs"

    def dequeue(self, pref):

        if  str(pref) == "dog" :
              return self.queue_dog.dequeue() 
        elif  str(pref) == "cat" :
              return self.queue_cat.dequeue() 


    def __str__(self):
        res = ""
        current = self.front
        while current:
            res += f"{ [current.value]} -> "
            current = current.next
        return res 

queue = AnimalShelter()
cat1 = Cat('puss')
queue.enqueue(cat1)
dog1 = Dog('rexy')
# print(isinstance(cat1, Cat))
# print(queue.enqueue(dog1))
# queue.enqueue(dog1)
print(queue.queue_cat.front.value)
# print(queue.dequeue("dog1"))
# print(queue)








