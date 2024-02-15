### Implementacja DFS dla grafu w postaci list sasiedztwa


G1 = [[1], [0,2,4], [1,3], [2,4], [1,3]]
G2 = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]

def dfs_falis(graph):

    n = len(graph)
    visited = [False] * n
    parents = [None] * n
    time = 0

    def dfs_visit(graph, u):
        nonlocal time
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                parents[v] = u
                dfs_visit(graph, v)
        time += 1

    for u in range(n):                   # dla niekoniecznie niespojnego grafu
        if not visited[u]:
            dfs_visit(graph, u)


