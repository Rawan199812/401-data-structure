from data_structure.data_structure.graph.graph import *
import pytest

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









