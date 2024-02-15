# Ściezki w DAGu

# Otrzymujemy na wejsciu w postaci listy krawedzi skierowany graf acykliczny (DAG)
# oraz pare wierzcholkow s i t. Naszym zadaniem jest obliczyc, ile jest mozliwych sciezek
# miedzy s i t.

G = [[1,2,3,4], [2], [3,5], [4,5], [5], []]

def count_paths(G, s, t):

    n = len(G)
    visited = [False] * n
    counts = [0] * n
    counts[t] = 1

    def dfs_visit(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)
            counts[u] += counts[v]

    dfs_visit(s)
    return counts[s]

print(count_paths(G, 0, 5))