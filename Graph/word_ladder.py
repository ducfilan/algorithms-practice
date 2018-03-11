from Graph.DS.Graph import Graph
from Graph.DS.Vertex import Vertex


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
