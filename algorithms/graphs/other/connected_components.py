def count_connected_components(G: 'graph represented using adjacency lists'):  #O(V+E)

    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)

    count = 0
    for u in range(n):
        if not visited[u] and G[u]:
            count += 1
            dfs(u)

    return count