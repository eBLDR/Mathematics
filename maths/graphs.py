class Vertex:
    def __init__(self, id_):
        self.id_ = id_
        self.incident_edges = set()

    def __str__(self):
        return f"v{self.id_}"

    @property
    def degree(self):
        return len(self.incident_edges)

    def connect_edge(self, edge):
        self.incident_edges.add(edge)

    def disconnect_edge(self, edge):
        if edge in self.incident_edges:
            self.incident_edges.remove(edge)

    def is_isolated(self):
        return len(self.incident_edges) == 0

    def get_adjacent(self):
        adjacent_vertices = set()
        for edge in self.incident_edges:
            for vertex in edge.endpoints:
                if vertex != self:
                    adjacent_vertices.add(vertex)

        return adjacent_vertices


class EdgeBase:
    def __init__(self, id_):
        self.id_ = id_
        self.endpoints = set()

    def __str__(self):
        vertex_str = ""
        if isinstance(self.endpoints, set):
            vertex_str = "{"
            for vertex in self.endpoints:
                vertex_str += vertex.__str__()
            vertex_str += "}"
        elif isinstance(self.endpoints, tuple):
            vertex_str = f"({self.endpoints[0].__str__()}, {self.endpoints[1].__str__()})"
        return f"e{self.id_}: {vertex_str}"


class Edge(EdgeBase):
    def __init__(self, id_, vertex_1, vertex_2):
        super().__init__(id_)
        self.endpoints = {vertex_1, vertex_2}


class DirectedEdge(EdgeBase):
    def __init__(self, id_, vertex_1, vertex_2):
        super().__init__(id_)
        self.endpoints = (vertex_1, vertex_2)


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def display_vertices(self):
        return [vertex.__str__() for vertex in self.vertices]

    def display_edges(self):
        return [edge.__str__() for edge in self.edges]

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def get_vertex_by_id(self, vertex_id):
        for vertex in self.vertices:
            if vertex.id_ == vertex_id:
                return vertex

    def get_isolated(self):
        isolated = set()
        for vertex in self.vertices:
            if vertex.is_isolated():
                isolated.add(vertex)

        return isolated

    def add_edge(self, edge):
        self.edges.add(edge)

    # TODO
    # def generate_edges_from_edge_endpoint_mapping(self, edge_endpoint_mapping):
    #     """ Generates all edges given an edge endpoint mapping. """

    def generate_edges_from_vertices_adjacent_mapping(self, vertices_adjacent_mapping: dict[int, list[int]]):
        """ Generates all edges given a vertices' adjacent mapping. """
        edge_id = 1

        for vertex_id in vertices_adjacent_mapping:
            vertex_start = self.get_vertex_by_id(vertex_id)
            if not vertex_start:
                continue

            for adjacent_vertex_id in vertices_adjacent_mapping[vertex_id]:
                vertex_end = self.get_vertex_by_id(adjacent_vertex_id)
                if not vertex_end:
                    continue

                edge = DirectedEdge(edge_id, vertex_start, vertex_end)
                vertex_start.connect_edge(edge)
                vertex_end.connect_edge(edge)
                if edge not in self.edges:
                    self.add_edge(edge)
                    edge_id += 1

    def find_path(self, start_vertex: Vertex, end_vertex: Vertex, path: list[Vertex] = None):
        """ Find a path from start_vertex to end_vertex in graph. """
        if start_vertex not in self.vertices:
            return None

        if not path:
            path = []

        path = path + [start_vertex]

        if start_vertex == end_vertex:
            return path

        for vertex in start_vertex.get_adjacent():
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path=path)
                if extended_path:
                    return extended_path

        return

    def find_all_paths(self, start_vertex: Vertex, end_vertex: Vertex, path: list[Vertex] = None):
        """ Find all paths from start_vertex to end_vertex in graph. """
        if start_vertex not in self.vertices:
            return None

        if not path:
            path = []

        path = path + [start_vertex]

        if start_vertex == end_vertex:
            return [path]

        paths = []

        for vertex in start_vertex.get_adjacent():
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path=path)

                for p in extended_paths:
                    paths.append(p)

        return paths


def main():
    # Definitions
    number_of_vertices = 7
    # number_of_edges = 9

    vertices_adjacent_mapping = {
        1: [3],
        2: [3, 5],
        3: [1, 2, 4, 5],
        4: [3],
        5: [3, 2],
        6: [],
        7: [1],
    }

    vertex_ids = list(range(1, number_of_vertices + 1))

    graph = Graph()

    for i in vertex_ids:
        graph.add_vertex(Vertex(i))

    print(f"Vertices: {graph.display_vertices()}")
    print(f"Isolated vertices: {graph.get_isolated()}")

    graph.generate_edges_from_vertices_adjacent_mapping(vertices_adjacent_mapping)

    print(f"Edges: {graph.display_edges()}")

    start_vertex_id = 7
    end_vertex_id = 5
    start_vertex = graph.get_vertex_by_id(start_vertex_id)
    end_vertex = graph.get_vertex_by_id(end_vertex_id)

    print(f"Find path from {start_vertex_id} to {end_vertex_id}")
    path = graph.find_path(start_vertex=start_vertex, end_vertex=end_vertex)
    print([vertex.__str__() for vertex in path])

    print(f"Find all paths from {start_vertex_id} to {end_vertex_id}")
    all_paths = graph.find_all_paths(start_vertex=start_vertex, end_vertex=end_vertex)
    for path in all_paths:
        print([vertex.__str__() for vertex in path])


if __name__ == '__main__':
    main()
