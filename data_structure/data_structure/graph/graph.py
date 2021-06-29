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

    def get_tuple_vertex(self):
    
        nodes_list = []
        # nodes = self.get_nodes()
        nodes = self._adjacency_list.keys()
        for ver in nodes:
            nodes_list.append(ver.value)
        return nodes_list

    def contains_all(self, nodes_list):
        """
        take list and return a boolean if all the list elements in the graph
        """
        v = self.get_tuple_vertex()
        bool = False
        for l in nodes_list:
            if l in v:
                bool =  True
            else:
                bool = False
        return bool

    def business_trip(self, trips):
        """
        take grap and list of city names and returns bollean value with the cost or null
      
        """
        all_vertex = self._adjacency_list.keys()
        vertex_values = self.get_tuple_vertex()
        found = self.contains_all(vertex_values)
        visited = set()
        cost_list = []
        cost = 0
        v = 0
        if found == True:
            if self.get_neighbors(trips[0]) == trips[1]:
                print(found)
            for value in all_vertex:
                if value.value in trips:
                    v = value
                    break
            def calc_weight(vertex, cost):
                cost = cost
                visited.add(vertex)
                neighbors = self.get_neighbors(vertex)
                for vertex in neighbors:
                    x = vertex.vertex
                    if x in visited:
                        continue
                    y = vertex.vertex.value
                    if y in trips:
                        cost += vertex.weight
                        cost_list.append(cost)
                        calc_weight(x, cost)
                        return cost_list[-1]
        # if not calc_weight(v, cost) == None:
                        
            return found,f'$ {calc_weight(v, cost)}'
        else:
            return False, "$0"





if __name__ == "__main__":
    # graph = Graph()
    # node1 = graph.add_node('node1')
    # node2 = graph.add_node('node2')
    # graph.add_edge(node1, node2,30)
    # graph.add_edge(node1, node1)
    # # graph.breadth_first_search(node1 , lambda v: print(v.value))
    # dic = graph.get_nodes()
    # for i in dic:
    #     print(i.value)
    # n = graph.get_neighbors(node1)
    # for i in n:
    #     print(i.vertex.value)

    gs = Graph()

    Pandora = gs.add_node('Pandora')
    Arendelle = gs.add_node('Arendelle')
    Metroville = gs.add_node('Metroville')
    Monstroplolis = gs.add_node('Monstroplolis')
    Narnia = gs.add_node('Narnia')
    Naboo = gs.add_node('Naboo')
    
    gs.add_edge(Pandora, Arendelle, 150)
    gs.add_edge(Pandora, Metroville, 82)
    gs.add_edge(Arendelle, Metroville, 99)
    gs.add_edge(Arendelle, Monstroplolis, 42)
    gs.add_edge(Monstroplolis, Naboo, 73)
    gs.add_edge(Metroville, Monstroplolis, 105)
    gs.add_edge(Metroville, Narnia, 37)
    gs.add_edge(Metroville, Naboo, 26)
    gs.add_edge(Narnia, Naboo, 26)
    gs.add_edge( Arendelle, Pandora,150)
    gs.add_edge( Metroville, Pandora, 82)
    gs.add_edge( Metroville,Arendelle, 99)
    gs.add_edge( Monstroplolis, Arendelle,42)
    gs.add_edge( Naboo, Monstroplolis,73)
    gs.add_edge( Monstroplolis, Metroville,105)
    gs.add_edge(Narnia, Metroville, 37)
    gs.add_edge( Naboo, Metroville,26)
    gs.add_edge(Naboo,Narnia,  26)
    trip1 = ['Pandora', 'Metroville']
    trip2= ['Naboo', 'Pandora']
    trip3 = ['Arendelle', 'Monstroplolis', 'Naboo']
    trip4 = ["Narnia", "Arendelle", "Naboo"]
    
    print(gs.business_trip(trip3))



    

    
    
    
    
                    

