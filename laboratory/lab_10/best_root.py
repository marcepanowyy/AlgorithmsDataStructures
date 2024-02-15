# (Najlepszy korzeń)
# Dany jest acykliczny, spójny, nieskierowany, ważony graf T (czyli T jest tak naprawdę ważonym
# drzewem). Proszę wskazać algorytm, który znajduje taki wierzchołek t, z którego odległość do
# najdalszego wierzchołka jest minimalna.

# O(V(V+E))

def best_root(graph):

    n = len(graph)
    visited = [0] * n
    token = 1

    def dfs(u):
        visited[u] = token
        max_dist = 0
        for v, weight in graph[u]:
            if visited[v] != token:
                dist = dfs(v) + weight
                if dist > max_dist:
                    max_dist = dist
        return max_dist

    # Minimized value of a maximum distance
    min_max_dist = float('inf')
    best_u = 0
    for u in range(n):
        max_dist = dfs(u)
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            best_u = u
        token += 1

    return best_u, min_max_dist

graph = [[(1, 12)],
         [(0, 12), (2, 10), (3, 15), (4, -5)],
         [(1, 10)],
         [(1, 15)],
         [(1, -5), (5, 2), (6, 4)],
         [(4, 2)],
         [(4, 4), (7, -6)],
         [(6, -6), (8, 1), (9, 20), (10, 4)],
         [(7, 1)],
         [(7, 20)],
         [(7, 4)]]

# print(best_root(graph))