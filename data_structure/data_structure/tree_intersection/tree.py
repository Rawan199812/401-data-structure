
from data_structure.data_structure.stacks_and_queues.stacks_and_queues import Queue
class Node:
    def __init__(self, data=None, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

class BinaryTree:
    def __init__(self, data=None):
        if data:
            data = Node(data)
        self.root = data

    @staticmethod
    def breadth_first(tree, node=None, array=None):
        '''Returns all values of tree in order using breadth first approach'''

        q = Queue()

        if not array:
            array = []

        if tree.root:
            q.enqueue(tree.root)

        while q.peek():

            front_node = q.dequeue()

            array.append(front_node.data)

            if front_node.left:
                q.enqueue(front_node.left)

            if front_node.right:
                q.enqueue(front_node.right)

        return array

    def post_order(self, node=None, result=[]):
        '''Return an array from tree in post-order order'''
        
        node = node or self.root

        if node.left:
            self.post_order(node.left, result)

        if node.right:
            self.post_order(node.right, result)

        result.append(node.data)

        return result

    # def pre_order(self, node=None, result=[]):
    #     '''Return an array from tree in pre-order order'''
        
    #     node = node or self.root
    #     result.append(node.data)

    #     if node.left:
    #         self.pre_order(node.left, result)

    #     if node.right:
    #         self.pre_order(node.right, result)

    #     return result
    def pre_order(self):
        ''' Pre-order traversal of our tree (root -> left -> right) '''
        pre_out = []
        def pre(root):
            pre_out.append(root.data)
            
            if root.left:
                pre(root.left)
            
            if root.right:
                pre(root.right)
                
        pre(self.root)

        return pre_out

    def in_order(self, node=None, result=[]):
        '''Return an array from tree in in_order order.'''
        
        node = node or self.root
        
        if node.left:
            self.in_order(node.left, result)

        result.append(node.data)

        if node.right:
            self.in_order(node.right, result)

        return result