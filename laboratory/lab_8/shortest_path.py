# Proszę zaimplementować algorytm bfs tak, żeby znajdował najkrótsze ścieżki w grafie i następnie,
# żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego do wskazanego wierzchołka.

from collections import deque

def get_solution(parents, v):
    if parents[v] == None: return [v]
    return [v] + get_solution(parents, parents[v])

def shortest_path(graph, s, t):

    n = len(graph)
    d = deque([])
    visited = [False] * n
    parents = [None] * n
    distance = [float("inf")] * n

    d.append(s)
    visited[s] = True
    distance[s] = 0

    while d:
        u = d.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parents[v] = u
                distance[v] = distance[u] + 1
                d.append(v)

    res = get_solution(parents, t)[::-1]
    min_dist = distance[t]
    print("vertex path order:", res)
    print("min distance:", min_dist)

G = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]
s, t = 0, 12

# shortest_path(G, s, t)