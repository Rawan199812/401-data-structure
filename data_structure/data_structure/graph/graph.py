from collections import deque
from types import coroutine

class Vertex: ## Like Node
    def __init__(self , value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def enqueue(self, value): ## first In First Out
        self.dq.appendleft(value)

    def dequeue(self): ## from the other side
        return self.dq.pop()
    
    def __len__(self):
        return len(self.dq)

class Stack():
    pass
class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """
        Adds value to a node and adds the node to a graph
        """
        # Create new node
        v = Vertex(value)
        # Add to the _adjacency_list 
        self._adjacency_list[v] = []
        return v

    def size(self):
        return len(self._adjacency_list)
 
    def add_edge(self, start_vertex, end_vertex, weight = 0): ## no weight by default
        """
        Adds an edge to the graph
        """
        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not found in graph")
        
        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not found in graph")
        
        self._adjacency_list[start_vertex].append(Edge(end_vertex, weight))


    def get_nodes(self):
        """
        Get all of the nodes in the  graph
        """
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        Get all the of the neighbors of a vertex
        """
        return self._adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex, action = (lambda x : None)):
        queue = Queue()
        visited = set() ## the set will check if the vertex visited before

        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        while len(queue): ## will break when it become 0
            current_vertex = queue.dequeue()
            action(current_vertex)
            neighbors = self.get_neighbors(current_vertex) 

            for edge in neighbors:
                neighbors_vertex = edge.vertex

                if neighbors_vertex in visited:
                    continue
                
                else:
                    visited.add(neighbors_vertex)
                queue.enqueue(neighbors_vertex)


if __name__ == "__main__":
    graph = Graph()
    node1 = graph.add_node('node1')
    node2 = graph.add_node('node2')
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node1)
    # graph.breadth_first_search(node1 , lambda v: print(v.value))
    dic = graph.get_nodes()
    for i in dic:
        print(i.value)
    n = graph.get_neighbors(node1)
    for i in n:
        print(i.vertex.value)
    
    
                    

