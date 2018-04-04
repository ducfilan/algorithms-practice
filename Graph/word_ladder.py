from Graph.DS.Graph import Graph
from Graph.DS.Vertex import Vertex
from Graph.DS.queue import Queue


def build_graph(words):
    d = {}
    g = Graph()

    for word in words:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.add_edge(word1, word2)

    return g


def bfs(start):
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


def find_shortest(start, end):
    shortest_distance = None

    start.set_distance(0)
    start.set_predecessor_vertex(None)

    vertices_queue = Queue()
    vertices_queue.enqueue(start)

    while vertices_queue.size() > 0:
        current_vertex = vertices_queue.dequeue()

        for neighbor in current_vertex.get_connections():
            if neighbor.get_color() == 'black':
                continue

            neighbor_distance = current_vertex.get_distance() + 1

            if neighbor == end and (not shortest_distance or neighbor_distance < shortest_distance):
                shortest_distance = neighbor_distance

            neighbor.set_color('grey')
            neighbor.set_distance(neighbor_distance)
            neighbor.set_predecessor_vertex(current_vertex)

            vertices_queue.enqueue(neighbor)

        current_vertex.set_color('black')

    return shortest_distance


g = build_graph(["FOOL", "POOL", "POLL", "POLE", "PALE", "SALE", "SAGE"])
print(find_shortest(g.get_vertex("FOOL"), g.get_vertex("SAGE")))
