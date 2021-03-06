from data_structure.data_structure.graph.graph import *
import pytest
from unittest.mock import patch

"""Node can be successfully added to the graph
An edge can be successfully added to the graph
A collection of all nodes can be properly retrieved from the graph
All appropriate neighbors can be retrieved from the graph
Neighbors are returned with the weight between nodes included
The proper size is returned, representing the number of nodes in the graph
A graph with only one node and edge can be properly returned
An empty graph properly returns null"""

graph = Graph()
def test_add_to_graph():

    graph.add_node("It's")
    graph.add_node('so')
    graph.add_node('sweet')
    dic = graph.get_nodes()
    actual = ([i.value for i in dic])
    expected = ["It's", "so", "sweet"]
    assert actual == expected

# def test_add_edge():
#     node1 = g.add_node("And")
#     node2 = g.add_node('I')
#     node3 = g.add_node('will')
#     node4 = g.add_node('gladly')
#     node5 = g.add_node('break')
#     node6 = g.add_node('it')

#     g.add_edge(node1, node2)
#     g.add_edge(node2, node1)

#     g.add_edge(node2, node3)
#     g.add_edge(node3, node2)

#     g.add_edge(node3, node4)
#     g.add_edge(node4, node3)

#     g.add_edge(node4, node5)
#     g.add_edge(node5, node4)

#     g.add_edge(node5, node6)
#     g.add_edge(node6, node1)


def test_size():
    g2 = Graph()
    g2.add_node("Knowing")
    g2.add_node("that")
    actual = g2.size()
    expected = 2
    assert actual == expected

def test_all_nodes_retrieved():
    graph_2 = Graph() 
    graph_2.add_node("It's")
    graph_2.add_node('so')
    graph_2.add_node('sweet')
    dic = graph_2.get_nodes()
    actual = ([i.value for i in dic])
    expected = ["It's", "so", "sweet"]
    assert actual == expected

def test_all_neighbors_retrieved():
    graph = Graph()
    Though = graph.add_node('Though')
    we = graph.add_node('we')
    dont  = graph.add_node("don't")
    graph.add_edge(Though, we)
    graph.add_edge(we, Though)
    graph.add_edge(we, we)
    graph.add_edge(we, dont)
    n = graph.get_neighbors(we)

    actual = ([i.vertex.value for i in n]) 
    expected = ['Though', 'we', "don't"]
    assert actual == expected

def test_empty_graph():
    pass

## Test Breadth First

@patch('builtins.print')
def test_BFS(mock_print):
    g1 = Graph()
    node1 = g1.add_node("Pandora")
    node2 = g1.add_node("Arendelle")
    node3 = g1.add_node("Metroville")
    node4 = g1.add_node("Monstroplolis")
    node5 = g1.add_node("Narnia")
    node6 = g1.add_node("Naboo")


    g1.add_edge(node1, node2)

    g1.add_edge(node2, node3)
    g1.add_edge(node2, node4)

    g1.add_edge(node3, node4)
    g1.add_edge(node3, node5)
    g1.add_edge(node3, node6)

    g1.breadth_first_search(node1 , lambda v: print(v.value))
    expected = {'Naboo', 'Monstroplolis', 'Arendelle', 'Pandora', 'Metroville', 'Narnia'}
    mock_print.assert_called_with(expected)


def test_BFS(): 
    g2 = Graph()
    node1 = g2.add_node("Pandora")
    node2 = g2.add_node("Arendelle")
    node3 = g2.add_node("Metroville")
    node4 = g2.add_node("Monstroplolis")
    node5 = g2.add_node("Narnia")
    node6 = g2.add_node("Naboo")
    
    g2.add_edge(node1, node2)
    g2.add_edge(node2, node3)
    g2.add_edge(node2, node4)

    g2.add_edge(node3, node4)
    g2.add_edge(node3, node5)
    g2.add_edge(node3, node6)
    expected = {'Naboo', 'Monstroplolis', 'Arendelle', 'Pandora', 'Metroville', 'Narnia'}
    lst = set()
    g2.breadth_first_search(node1, lambda ver: lst.add(ver.value))
    actual = lst
    assert actual == expected

    #=============Test business-trip
def test_trip_one(trip):
    trip1 = ['Pandora', 'Metroville']
    actual = trip.business_trip(trip1)
    expected = (True, '$ 82')
    assert actual == expected

def test_trip_two(trip):
    trip2= ['Naboo', 'Pandor']
    actual = trip.business_trip(trip2)
    expected = (True,'$ None')
    assert actual == expected

def test_trip_three(trip):
    trip3 = ["Narnia", "Arendelle", "Naboo"]
    actual = trip.business_trip(trip3)
    expected = (True,'$ None')
    assert actual == expected

    #=============Test DFS
def test_depth_first(DFS):
    
    obj = DFS.DFS() 
    actual = ""
    for i in obj:
        actual += i.value
    expected = "abcgdehf"
    assert actual == expected

def test_depth_first_empty():
    empty_g = Graph()

    actual =  empty_g.DFS() 
    expected = "empty graph"
    assert actual == expected




@pytest.fixture
def graph_1():
    g = Graph()
    node1 = g.add_node("1")
    node2 = g.add_node("2")
    node3 = g.add_node("3")
    node4 = g.add_node("4")
    g.add_edge(node1, node2)
    g.add_edge(node2, node1)

    g.add_edge(node2, node3)
    g.add_edge(node3, node2)

    g.add_edge(node3, node4)
    g.add_edge(node4, node3)

    g.add_edge(node4, node1)

    return g

@pytest.fixture

def trip():
    
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
    
    
    return gs


@pytest.fixture

def DFS():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')
    graph.add_edge(a,b)
    graph.add_edge(a,d)
    graph.add_edge(b,c)
    graph.add_edge(b,d)
    graph.add_edge(c,g)
    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)
    graph.add_edge(h,f)
 
    return graph










