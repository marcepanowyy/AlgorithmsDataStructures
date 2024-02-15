# takie jak zad.2 z II kolosa 2020/2021

# Paweł Konop

from zad6testy import runtests
from collections import deque

def bfs(G, s):

    n = len(G)
    visited = [False] * n
    distance = [float("inf")] * n

    distance[s] = 0
    d = deque([])
    d.append(s)

    visited[s] = True

    while d:
        u = d.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                d.append(v)

    return distance

def inner_bfs(G, s, t, distance1, distance2, spl):

    n = len(G)
    visited = [False] * n
    vertex_dist = [[] for _ in range(spl+1)]
    vertex_dist[0] += [s]

    d = deque([])
    d.append(s)
    visited[s] = True

    while d:
        u = d.popleft()
        for v in G[u]:
            if not visited[v] and distance1[v] + distance2[v] == spl:
                visited[v] = True
                vertex_dist[distance1[v]] += [v]
                d.append(v)
    return vertex_dist

def longer(G, s, t):

    n = len(G)
    distance1 = bfs(G, s)
    distance2 = bfs(G, t)
    spl = int(distance1[t])                                      # shortest path length
    vertex_dist = inner_bfs(G, s, t, distance1, distance2, spl)  # arr with num of vertex with same lenght from vertexs s,
                                                                 # arr[1] - num of vertex from s with distance 1
    if vertex_dist[0] == vertex_dist[1] == 1:
        return (vertex_dist[0], vertex_dist[1])
    for i in range(1, spl+1):
        if len(vertex_dist[i]) == len(vertex_dist[i-1]) == 1:
            return (vertex_dist[i][0], vertex_dist[i-1][0])

    return None

runtests(longer, all_tests=True)

