# Second Minimum Time to Reach Destination

# A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled
# from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each
# edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is
# connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge
# is time minutes.

# Each vertex has a traffic signal which changes its color from green to red and vice versa every 'change'
# minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex
# only when the signal is green. You cannot wait at a vertex if the signal is green.

# The second minimum value is defined as the smallest value strictly larger than the minimum value.

# For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
# Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

# Notes:

# You can go through any vertex any number of times, including 1 and n.
# You can assume that when the journey starts, all signals have just turned green.

from collections import deque

def create_graph(n, edges):

    graph = [[] for _ in range(n+1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return graph


def bfs(graph, s, t):

    n = len(graph)

    steps = [[float("inf")] * 2 for _ in range(n)]          # steps[i][0] - min steps, steps[i][1] - second min steps
    d = deque([])

    d.append((0, s))
    steps[s][0] = 0

    while d:

        dist, u = d.popleft()
        if steps[t][1] == dist: return dist

        for v in graph[u]:

            if steps[v][1] == float("inf"):

                if steps[v][0] == float("inf"):
                    steps[v][0] = dist + 1
                    d.append((dist + 1, v))

                elif dist + 1 > steps[v][0]:
                    steps[v][1] = dist + 1
                    d.append((dist + 1, v))

    return None

def second_minimum(n, edges, time, change):

    graph = create_graph(n, edges)
    second_min, cost = bfs(graph, 1, n), 0

    for i in range(second_min):                                         # symulacja czerwonych swiatel
        if cost % (2 * change) >= change:
            cost = (cost // (2 * change) + 1) * (2 * change)
        cost += time

    return cost


n, time, change = 5, 3, 5
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]

# print(second_minimum(n, edges, time, change))






