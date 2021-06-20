from data_structure.data_structure.linked_list.linked_list import LinkedList, Node

class Hashtable:
    def __init__(self, size = 1024):
        self.size = size
        self.buckets = [None] * self.size 
    def add(self,key,value):
        """
        takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
        """

        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = LinkedList()
        return self.buckets[index].append([key,value])


        
    def get(self,key):
        index = self.hash(key)
        if not self.buckets[index]:
            return None
        else:
            current = self.buckets[index].head
            while current:
                if current.data[0] == key:
                    return current.data[1]
                current = current.next
            return None
    def contains(self,key):
        """
        takes in the key and returns a boolean, indicating if the key exists in the table already.
        """
        index = self.hash(key)
        if self.buckets[index]:
            return True
        return False

    def hash(self,key):
        """
         takes in an arbitrary key and returns an index in the collection.
        """
        sum = 0
        for char in key:
            sum+= ord(char)  ## ord() will return Unicode equivalence of the string 
        hash_key = (sum*23)%(self.size)
        return hash_key


hash1 = Hashtable()
# print(hash1.hash("A"))
hash1.add("A","first-a")
print(hash1.add("B","first-b"))

# print(str(hash1.buckets))
# print(hash1.contains("A"))
# print(hash1.get("A"))