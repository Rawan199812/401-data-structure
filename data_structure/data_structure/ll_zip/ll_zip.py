from data_structure.data_structure.linked_list.linked_list import Node, LinkedList  
    
def zipLists(first, second):
     current_fll = first.head
     current_sll = second.head
     length_fll, length_sll =0,0

     temp = {}
     while(current_fll):
        length_fll += 1
        current_fll = current_fll.next_node
     while(current_sll):
        length_sll += 1
        current_sll = current_sll.next_node
     if length_fll < length_sll:
       temp =first
       first = second
       second =temp
       current_fll = first.head
       current_sll = second.head
     linked_first = first.head
     linked_second = second.head
     while linked_first and linked_second:
            first_next = linked_first.next_node
            second_next = linked_second.next_node
            linked_second.next_node = first_next 
            linked_first.next_node = linked_second 
            linked_first = first_next
            linked_second = second_next
            second.head = linked_second
     return first




myList = LinkedList()
myList.insert(5)
myList.insert(8)
myList.insert(12)
myList.append(3)

list=LinkedList()
myList.insert(1)
myList.insert(5)
myList.insert(88)
myList.append(4)

print(zipLists(myList,list))