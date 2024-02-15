def components(graph):

    n = len(graph)
    visited = [False] * n

    def dfs_visit(u):
        visited[u] = True
        for neighbour in range(n):
            if graph[u][neighbour] != 0 and not visited[neighbour]:
                visited[u] = True                                           # tam gdzie nie ma krawedzi jest 0
                dfs_visit(neighbour)

    c = 0

    for u in range(n):                                                      # w razie gdyby byl niespojny xd
        if not visited[u]:
            c += 1
            dfs_visit(u)

    return c

graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0]]

# print(components(graph))


