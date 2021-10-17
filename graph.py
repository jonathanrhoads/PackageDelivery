class Vertex:
    def __init__(self, label):
        '''
        Vertexes are used to hold information about the delivery addresses.
        :param label:
        '''
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None


class Graph:
    #  This graph class is used to hold the addresses as vertices and the distances between them as the
    #  edges connecting the vertices.
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        '''
        Adds an address as a vertex. If the address is already in the adjacency list as a key then it does nothing.
        O(1)
        :param new_vertex:
        :return:
        '''
        if new_vertex not in self.adjacency_list:
            self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        '''
        Adds the distance between the two points as an edge weight and adds the vertex as an adjacency vertex.
        O(1)
        :param from_vertex:
        :param to_vertex:
        :param weight:
        :return:
        '''
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        '''
        Ensures directed edges are added from point A to point B and vice versa.
        O(1)
        :param vertex_a:
        :param vertex_b:
        :param weight:
        :return:
        '''
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
