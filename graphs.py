"""
A GRAPH in mathematics and computer science consists of NODES, also known
as VERTICES. Nodes may or may not be connected with one another.
The connecting line between two nodes is called an EDGE.
If the edges between the nodes are undirected, the graph is called an
undirected graph. If an edge is directed from one vertex (node) to another,
a graph is called a directed graph. An directed edge is called an ARC.
The DEGREE of a vertex in a graph is the number of edges connecting it,
with loops counted twice.
"""

my_graph = {'a': ['c'],
            'b': ['c', 'e'],
            'c': ['a', 'b', 'd', 'e'],
            'd': ['c'],
            'e': ['c', 'b'],
            'f': []
            }


def nodes(graph):
    """ Returns the vertices/nodes of a graph. """
    return list(graph.keys())


print('Vertices/nodes are:\n', nodes(my_graph))


def edges(graph):
    """ Generate a list of all edges. """
    edges_ = []
    for node in graph:
        for neighbour in graph[node]:

            # Non repeated
            if (node, neighbour) not in edges_:
                edges_.append((node, neighbour))

    return edges_


print('Edges are:\n', edges(my_graph))


def isolated_nodes(graph):
    """ Returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated


print('Isolated nodes are:\n', isolated_nodes(my_graph))
print('=' * 30)


def add_node(graph, new_node):
    if new_node not in graph:
        graph[new_node] = []


my_node = 'x'
print('Add new node: {}'.format(my_node))
add_node(my_graph, my_node)
print('Vertices/nodes are:\n', nodes(my_graph))
print('=' * 30)


def add_edge(graph, new_edge, arc=False):
    """ If arc is False, adds undirected edge.
    Directed edge otherwise. """
    node_1, node_2 = new_edge

    if node_1 in graph:
        graph[node_1].append(node_2)
    else:
        graph[node_1] = [node_2]

    if not arc:
        if node_2 in graph:
            graph[node_2].append(node_1)
        else:
            graph[node_2] = [node_1]


my_edge = ('x', 'a')
print('Add new edge: {}'.format(my_edge))
add_edge(my_graph, my_edge, arc=True)
print('Edges are:\n', edges(my_graph))
print('=' * 30)


def find_path(graph, start_vertex, end_vertex, path=None):
    """ Find a path from start_vertex to end_vertex in graph. """
    if not path:
        path = []

    path = path + [start_vertex]

    if start_vertex == end_vertex:
        return path

    if start_vertex not in graph:
        return None

    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_path = find_path(graph, vertex, end_vertex, path=path)
            if extended_path:
                return extended_path

    return None


start_node = 'x'
end_node = 'e'
print('Find path from {} to {}'.format(start_node, end_node))
print(find_path(my_graph, start_node, end_node))


def find_all_paths(graph, start_vertex, end_vertex, path=None):
    """ Find all paths from start_vertex to end_vertex in graph. """
    if not path:
        path = []

    path = path + [start_vertex]

    if start_vertex == end_vertex:
        return [path]

    if start_vertex not in graph:
        return []

    paths = []

    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_paths = find_all_paths(
                graph, vertex, end_vertex, path=path
            )

            for p in extended_paths:
                paths.append(p)

    return paths


print('Find all paths from {} to {}'.format(start_node, end_node))
print(find_all_paths(my_graph, start_node, end_node))