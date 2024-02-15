### Implementacja DFS dla grafu w postaci macierzowej O(V**2)

def dfs(graph):

    n = len(graph)
    visited = [False] * n

    def dfs_visit(u):
        visited[u] = True
        for neighbour in range(n):
            if graph[u][neighbour] != 0 and not visited[neighbour]:
                visited[u] = True                                           # tam gdzie nie ma krawedzi jest 0
                dfs_visit(neighbour)

    for u in range(n):                                                      # w razie gdyby byl niespojny xd
        if not visited[u]:
            dfs_visit(u)


G1 = [[0,1,0,0,0,0,0],
      [1,0,1,0,0,0,0],
      [0,1,0,1,1,0,0],
      [0,0,1,0,1,0,0],
      [0,0,1,1,0,1,0],
      [0,0,0,0,1,0,1],
      [0,0,0,0,0,1,0]]

dfs(G1)
