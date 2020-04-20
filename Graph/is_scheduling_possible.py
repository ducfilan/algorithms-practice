# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.
#
# Example 1:
#
# Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
# Output: true
# Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
# before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2]

from collections import deque


class TasksScheduler:
    def __init__(self, tasks_count, tasks_prerequisites):
        self.tasks_count = tasks_count
        self.in_vertice_edge = self._build_in_vertice(tasks_prerequisites)
        self.out_vertice_edge = self._build_out_vertice(tasks_prerequisites)

    def _build_in_vertice(self, edges):
        in_vertice_edge = {}

        for edge in edges:
            if edge[1] in in_vertice_edge:
                in_vertice_edge[edge[1]].add(edge[0])
            else:
                in_vertice_edge[edge[1]] = set([edge[0]])

        return in_vertice_edge

    def _build_out_vertice(self, edges):
        out_vertice_edge = {}

        for edge in edges:
            if edge[0] in out_vertice_edge:
                out_vertice_edge[edge[0]].add(edge[1])
            else:
                out_vertice_edge[edge[0]] = set([edge[1]])

        return out_vertice_edge

    def _get_source_vertice(self):
        in_vertice = set(self.in_vertice_edge.keys())
        out_vertice = self.out_vertice_edge.keys()

        source_vertice = deque(
            vertex for vertex in out_vertice if vertex not in in_vertice
        )

        return source_vertice

    def is_tasks_schedulable(self):
        if self.tasks_count <= 0:
            return False

        sorted_order = []

        source_vertice = self._get_source_vertice()

        while source_vertice:
            vertex = source_vertice.popleft()
            sorted_order.append(vertex)

            if vertex in self.out_vertice_edge:
                connected_vertice = self.out_vertice_edge[vertex]

                for connected_vertex in connected_vertice:
                    self.in_vertice_edge[connected_vertex].remove(vertex)

                    if len(self.in_vertice_edge[connected_vertex]) == 0:
                        source_vertice.append(connected_vertex)

        if len(sorted_order) != self.tasks_count:
            return False

        return True


scheduler = TasksScheduler(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])

print(scheduler.is_tasks_schedulable())
