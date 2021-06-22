from data_structure.data_structure.hashtable.hashtable import Hashtable
def left_join_hash(hash1,hash2):
    output = []
    lst = []
    if hash1 and hash2:
        for element in hash1.buckets:
            if element:
                current = element.head
                while current:
                    lst.append(current.data[0])
                    lst.append(current.data[1])
                    if hash2.contains(current.data[0]):
                        # val = hash2.get(current.data[0])
                        # lst.append(val)
                        print(current.data[0])
                        pass
                    else:
                        lst.append(None)
                    output.append(lst)
                    lst = []
                    current = current.next_node
        return output
    else:
        return "Empty Hash"

 

hash1 = Hashtable()
hash1.add("A","first-a")
hash1.add("B","first-b")
hash1.add("D","first-d")



hash2 = Hashtable()
# hash2.add("C","first-c")
# hash2.add("B","first-d")

# print(left_join_hash(hash1, hash2))

print(left_join_hash(hash1, hash2))








