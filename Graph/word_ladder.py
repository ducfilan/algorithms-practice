from Graph.DS.Graph import Graph
from Graph.DS.Vertex import Vertex
from Graph.DS.queue import Queue


def build_graph(words):
    d = {}
    g = Graph()

    for word in words:
        for i, c in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = []

        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.add_edge(word1, word2)

    return g


def bfs(g, start):
    start.set_distance(0)
    start.set_predecessor_vertex(None)

    vertices_queue = Queue()
    vertices_queue.enqueue(start)

    while vertices_queue.size() > 0:
        current_vertex = vertices_queue.dequeue()

        for neighbor in current_vertex.get_connections():
            neighbor.set_color('grey')
            neighbor.set_distance(current_vertex.get_distance() + 1)
            neighbor.set_predecessor_vertex(current_vertex)

            vertices_queue.enqueue(neighbor)

        current_vertex.set_color('black')
