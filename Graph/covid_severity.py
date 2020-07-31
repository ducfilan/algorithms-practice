# The corona virus situation in Japan is becoming more complex since the number of infectious cases is increasing fast.
#
# For the purpose of statistical investigation, there are two terms to care about: Infectious cluster and Severity
#
# An infectious cluster is a group of people who have had direct or indirect contact with each other. For example,
# person A has direct contact with person B and C, person B has direct contact with person D. Therefore, 4 people
# A, B, C, D are considered to belong to the same infectious cluster.
# The severity of the infectious cluster is the sum of the severity indexes of all people in a group. The greater
# the sum of severity indexes in a cluster, the more seriously the COVID affects social health.
# The severity index of each person is specified as follows:
#
# F0 (person who tested positive for Covid): 10
# F1 (person who had direct contact with F0): 5
# F2 (person who had direct contact with F1): 3
# F3 (person who had direct contact with F2 or another F3): 1
# Fx (person who did not have contact with F0, F1, F2 or F3): 0
# If a person can be more than one F, he/she is considered to be the F with the highest severity index.
#
# Example:
#
# A, D were tested positive for COVID.
# Person A had direct contact with person B.
# Person C had direct contact with person B, D and E.
# Person F had direct contact with person E and G.
# The indexes of A, B, C, D, E, F, G are as follows:
# A, D (F0): 10
# B, C (F1): 5
# E (F2): 3
# F, G (F3): 1
# The severity level of this group is: 10 + 10 + 5 + 5 + 3 + 1 + 1 = 35
# Note:
# Person C had direct contact with person B(F1) -> person C is considered as F2
# Person C had direct contact with person D(F0) -> person C is considered as F1
# Because F1's severity index is higher than F2's severity index, person C is F1
#
# Given that the number of people in a cluster is n, the contact tracing information in that cluster is represented
# as a matrix a and array b represents the list of people testing positive for COVID.
# Help the Japanese government classify n people into infectious clusters and the level of severity of each cluster.
# Return the result sorted in descending order.
#
# Example
#
# For n = 10, a = [[1, 2], [1, 3], [2, 4], [4, 6], [2, 8], [6, 9], [7, 10]], b = [3, 8, 5], the output should be
# covidSeverity(n, a) = [35, 10, 0].
# Explanation:
# n = 10 -> the number of people in the given area is 10.
# a = [[1, 2], [1, 3], [2, 4], [4, 6], [2, 8], [6, 9], [7, 10]] ->The 1st person was exposed to the 2nd and the 3rd
# person; the 2nd had direct contact with the 4th and 8th person; the 4th person had direct contact with the 6th person;
# the 6th person had direct contact with the 9th person; the 7th person had direct contact with the 10th person.
# b = [3, 8, 5] -> the 3rd, 8th and 5th person tested positive for COVID
# Below is the diagram of contact tracing of people in the cluster:
# We have 3 infectious clusters:
#
# (3-F0, 1-F1, 2-F1, 4-F2, 6-F3, 9-F3, 8-F0) with the level of severity is 35
# (5-F0) with the level of severity is 10
# (7-Fx, 10-Fx) with the level of severity is 0
# The final result is covidSeverity(a,b) = [35, 10, 0]


class Vertex:
    def __init__(self, lbl, severity):
        self.lbl = lbl
        self.vertices_connected_to = {}
        self.severity = severity
        self.visited = False

    def add_neighbor(self, v):
        self.vertices_connected_to[v.lbl] = v


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex_from_key(self, key, severity):
        new_vertex = Vertex(key, severity)
        self.add_vertex(new_vertex)

        return new_vertex

    def add_vertex(self, new_vertex):
        self.vertices[new_vertex.lbl] = new_vertex

    def add_edge(self, from_key, to_key):
        if from_key not in self.vertices:
            self.add_vertex_from_key(from_key, 0)

        if to_key not in self.vertices:
            self.add_vertex_from_key(to_key, 0)

        self.vertices[from_key].add_neighbor(self.vertices[to_key])


def next_severity(c):
    if c == 10:
        return 5
    if c == 5:
        return 3
    if c == 3:
        return 1
    if c == 1:
        return 1
    if c == 0:
        return 0


g = Graph()


def covidSeverity(n, a, b):
    global g
    f0 = set(b)

    for i in range(1, n + 1):
        g.add_vertex_from_key(i, 10 if i in f0 else 0)

    for x, y in a:
        g.add_edge(x, y)
        g.add_edge(y, x)

    for f0i in f0:
        fill_sev(f0i)

    res = []
    for vv in g.vertices.values():
        if not vv.visited:
            vv.visited = True
            res.append(find_cluster(vv, 0))

    return sorted(res, reverse=True)


def fill_sev(f0i):
    vis = {f0i}

    while vis:
        n = vis.pop()
        for v in g.vertices[n].vertices_connected_to.values():
            if v != n:
                old_v_sev = v.severity
                v.severity = max(v.severity, next_severity(g.vertices[n].severity))
                if old_v_sev < v.severity:
                    vis.add(v.lbl)


def find_cluster(sv, s):
    vis = {sv}

    s += sv.severity

    while vis:
        n = vis.pop()
        for v in n.vertices_connected_to.values():
            if not v.visited:
                v.visited = True
                vis.add(v)
                s += v.severity

    return s


print(covidSeverity(10, [[1, 2], [1, 3], [2, 4], [4, 6], [2, 8], [6, 9], [7, 10]], [3, 8, 5]))
