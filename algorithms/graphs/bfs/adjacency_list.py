### Implementacja bfs dla grafu w postaci list sasiedztwa O(V+E)

# from queue import Queue

# z kolejka dwustronna szybciej

from collections import deque

def bfs(graph, s):

    n = len(graph)
    d = deque([])
    visited = [False] * n
    parents = [None] * n

    d.append(s)
    visited[s] = True

    while d:
        u = d.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parents[v] = u
                d.append(v)

G1 = [[1], [0,2,4], [1,3], [2,4], [1,3]]
G2 = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]

bfs(G2, 0)

