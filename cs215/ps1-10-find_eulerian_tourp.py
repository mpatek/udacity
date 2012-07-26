# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    """
    Return a Eulerian path through the graph. 
    
    Using Fleury's algorithm
    """
    
    if not is_connected(graph):
        return [] # No possible tour

    odd_nodes = odd_degree_nodes(graph)
    if len(odd_nodes) not in (0, 2):
        return [] # No possible tour

    tour = []
    current_node = None
    if len(odd_nodes) == 2:
        current_node = list(odd_nodes)[0] # start on odd degree node
    else:
        current_node = graph[0][0] # start on arbitrary node

    unused_edges = set(graph)

    tour.append(current_node)
    while len(unused_edges) > 0:
        possible_next_edges = []
        for edge in unused_edges:
            if current_node in edge:
                possible_next_edges.append(edge)
        if not possible_next_edges:
            return [] # seems there is no solution
        next_edge = None 
        for poss_edge in possible_next_edges:
            next_edge = poss_edge
            if not would_disconnect(unused_edges, poss_edge):
                break # favor non-disconnecting edges
        unused_edges.remove(next_edge)
        if next_edge[0] == current_node:
            current_node = next_edge[1]
        else:
            current_node = next_edge[0]
        tour.append(current_node)

    return tour

def node_edges(graph):
    """ Return map from nodes to edges. """
    node_edges = {}
    for edge in graph:
        n1, n2 = edge
        if not n1 in node_edges:
            node_edges[n1] = []
        if not n2 in node_edges:
            node_edges[n2] = []
        node_edges[n1].append(edge)
        node_edges[n2].append(edge)
    return node_edges


def node_degrees(graph):
    """ Return map from nodes to degrees (number of edges). """
    node_edge = node_edges(graph)
    node_degrees = {}
    for node, edges in node_edge.items():
        node_degrees[node] = len(edges)
    return node_degrees


def odd_degree_nodes(graph):
    """ Return set of nodes with odd degree in graph. """
    node_degree = node_degrees(graph)
    odd_nodes = set()
    for node, degree in node_degree.items():
        if degree % 2 == 1:
            odd_nodes.add(node)
    return odd_nodes

def is_connected(graph):
    """ Indicate whether the specified graph is connected. """
    if len(graph) == 0:
        return True
    all_nodes = set(x[0] for x in graph).union(set(x[1] for x in graph))
    connected_set = set(graph[0])
    while True:
        nodes_added = False
        for edge in graph:
            n1, n2 = edge
            if n1 in connected_set and n2 not in connected_set:
                connected_set.add(n2)
                nodes_added = True
            elif n2 in connected_set and n1 not in connected_set:
                connected_set.add(n1)
                nodes_added = True
        if not nodes_added:
            break
    return connected_set == all_nodes

def would_disconnect(graph, edge):
    """ Indicate whether removing the specified edge would disconnect the graph. """
    new_graph = []
    for old_edge in graph:
        if old_edge != edge:
            new_graph.append(old_edge)
    return not is_connected(new_graph)


graph = [(1, 2), (2, 3), (3, 1)]
print find_eulerian_tour(graph)

graph = [(1, 2), (2, 3), (3, 6), (6, 5), (2, 5), (4, 5), (1, 4)]
print find_eulerian_tour(graph)

graph = [(1, 2), (2, 3), (3, 1)]
print find_eulerian_tour(graph)

graph = [(1, 2), (2, 3), (3, 6), (6, 5), (2, 5), (4, 5), (1, 4)]
print find_eulerian_tour(graph)

graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
print find_eulerian_tour(graph)

graph = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
print find_eulerian_tour(graph)
