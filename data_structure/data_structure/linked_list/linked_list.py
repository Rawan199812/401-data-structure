class Node():

    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next (self):
        return self.next_node

    def get_data (self):
        return self.data


class LinkedList ():

    def __init__(self, h = None):
        self.head = h
        self.size = 0

    def insert (self, d):
        new_node = Node (d, self.head)
        self.head = new_node
        self.size += 1
        return new_node.data

    def includes (self, d):
        this_node = self.head
        while this_node:
            if this_node.get_data() == d:
                return True
            else:
                this_node = this_node.get_next()
        return False
    def __str__(self):
        if self.head:
            saved_data = f"({ self.head.data}) "   
            this_node = self.head
            while this_node:
                this_node = this_node.next_node
                if  this_node:
                    saved_data += "-> ""("f"{ this_node.data}"") "
                else:
                    saved_data += "-> NULL"
        else:
            return "Your Linked List still empty"
        return saved_data
    def append(self,h):
        new_node = Node(h)
        current = self.head
        if not self.head : # check if the list empty so i only have to set the pointer oh the head to the new node
            self.head = new_node
            return 
        while current:# search for the last node that will be point to None 
            if current.next_node == None:
                current.next_node = new_node
                return
            else:
                current = current.next_node
    def insertBefore(self, prev_value, data):
        new_node = Node(data)
        current = self.head
        # if current.data == prev_value: #check it the node we wand to insert before is the first node in the list
        #       self.insert(data)  (we can call the insert another way)
        # else:
        while current:
                if current.data == prev_value:
                    new_node.next_node = current
                    self.head = new_node
                    return
                if current.next_node:
                     if current.next_node== prev_value:
                           new_node.next_node == current.next_node
                           current.next_node = new_node
                           return
                     current = current.next_node          

                if current.next_node == None:
                    raise Exception(f'{prev_value} node is not in the list')

    def insertAfter(self,prev_value,data):
        new_node = Node(data)
        current = self.head
        # check if the node we want to insert after is exisit
        while current: 
            if current.data == prev_value:
                new_node.next_node= current.next_node # the pointer for the new node points to the next node of the node we want to insert after
                current.next_node = new_node
                return
            current = current.next_node
        raise ValueError(f'{prev_value} node is not in the list')
    def kthFromEnd(self, k):

        try:
                
            n = -1
            current = self.head
            while current:
                current = current.next_node
                n = n + 1
            if n >= k:
                current = self.head
                for i in range(n - k):
                    current = current.next_node
            return current.data
        except:
            return "The Value Not Found"



# myList = LinkedList()
# myList.insert(5)
# myList.insert(8)
# myList.insert(12)
# myList.append(3)
# list=LinkedList()
# myList.insert(1)
# myList.insert(5)
# myList.insert(88)
# myList.append(4)

# myList.insertAfter(5,6)
# myList.insertBefore(12,4)
# myList.insertBefore(12,5)
# myList.insertBefore(8,4)
# print(myList.kthFromEnd(0))
# print(myList.includes(5))
# print(myList.includes(3))
# print(myList.zipLists(myList,list))
# print(myList.__str__())
