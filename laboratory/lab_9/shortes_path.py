# (Najkrósze ścieżki w DAGu) Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich
# innych w acyklicznym grafie skierowanym?

def shortest_paths(graph, s):

    n = len(graph)
    visited = [False] * n
    distance = [float("inf")] * n
    res = []

    distance[s] = 0

    def dfs_visit(graph, u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v[0]]:
                dfs_visit(graph, v[0])

        res.append(u)

    for u in range(n):
        if not visited[u]:
            dfs_visit(graph, u)

    res = res[::-1]
    idx = res.index(s)

    for i in range(idx, len(res)):
        for v in graph[i]:
            if distance[v[0]] > distance[i] + v[1]:
                distance[v[0]] = distance[i] + v[1]
    return distance


G1 =    [[(1, 3), (2, 6)],
         [(2, 2), (3, 1), (5, 8)],
         [(4, 7), (3, 5)],
         [(5, 2), (4, 5)],
         [(5, 3)],
         []]

# print(shortest_paths(G1, 3))