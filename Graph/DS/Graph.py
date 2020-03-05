from Graph.DS.Vertex import Vertex


class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.vertices_count = 0

    def __len__(self):
        return len(self.vertices)

    def add_vertex_from_key(self, key):
        new_vertex = Vertex(key)
        self.add_vertex(new_vertex)

        return new_vertex

    def add_vertex(self, new_vertex):
        self.vertices_count += 1
        self.vertices[new_vertex.get_label()] = new_vertex

    def get_vertex(self, key):
        return self.vertices[key] if key in self.vertices else None

    def __contains__(self, key):
        return key in self.vertices

    def add_edge_from_keys(self, from_key, to_key, cost=0):
        if from_key not in self.vertices:
            self.add_vertex_from_key(from_key)

        if to_key not in self.vertices:
            self.add_vertex_from_key(to_key)

        self.vertices[from_key].add_neighbor(self.vertices[to_key], cost)

    def add_edge_from_vertices(self, from_vertex, to_vertex, cost=0):
        if from_vertex.get_label() not in self.vertices:
            self.add_vertex_from_key(from_vertex)

        if to_vertex.get_label() not in self.vertices:
            self.add_vertex_from_key(to_vertex)

        from_vertex.add_neighbor(to_vertex, cost)
