# Dany jest graf G =(V, E), gdzie każda krawędź ma wagę ze zbioru {1, . . . , |E|} (wagi krawędzi
# są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków x i y sprawdza, czy
# istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach.

# ch wie czy dobrze, ale dziala na jednym przykladzie wiec git XD

def decreasing_edges(graph, s, t):

    n = len(graph)
    parents = [None] * n
    visited = [False] * n
    prevs = [float("-inf")] * n

    def dfs_visit(u, prev, t):
        for neighbour in range(n):
            if graph[u][neighbour] != 0 and prev > graph[u][neighbour]:
                prevs[neighbour] = graph[u][neighbour]
                parents[neighbour] = u
                dfs_visit(neighbour, graph[u][neighbour], t)
                if parents[t] != None:
                    return

    for neighbour in range(n):
        if graph[s][neighbour] != 0:
            prevs[neighbour] = graph[s][neighbour]
            dfs_visit(neighbour, graph[s][neighbour], t)
            if parents[t] != None:
                return True

    return False

G1 = [[0, 1000, 10000, 8, 0, 0, 0, 0, 0, 0],
     [1000, 0, 0, 0, 0, 0, 5, 0, 0, 0],
     [10000, 0, 0, 0, 100, 0, 0, 0, 0, 0],
     [8, 0, 0, 0, 9, 7, 0, 0, 0, 0],
     [0, 0, 100, 9, 0, 5, 3, 30, 0, 0],
     [0, 0, 0, 7, 5, 0, 0, 0, 0, 0],
     [0, 5, 0, 0, 3, 0, 0, 0, 0, 5],
     [0, 0, 0, 0, 30, 0, 0, 0, 6, 10],
     [0, 0, 0, 0, 0, 0, 0, 6, 0, 0],
     [0, 0, 0, 0, 0, 0, 5, 10, 0, 0]]

G2 = [[0, 1000, 10000, 8, 0, 0, 0, 0, 0, 0],
     [1000, 0, 0, 0, 0, 0, 5, 0, 0, 0],
     [10000, 0, 0, 0, 100, 0, 0, 0, 0, 0],
     [8, 0, 0, 0, 9, 7, 0, 0, 0, 0],
     [0, 0, 100, 9, 0, 5, 3, 30, 0, 0],
     [0, 0, 0, 7, 5, 0, 0, 0, 0, 0],
     [0, 5, 0, 0, 3, 0, 0, 0, 0, 5],
     [0, 0, 0, 0, 30, 0, 0, 0, 6, 40],
     [0, 0, 0, 0, 0, 0, 0, 6, 0, 0],
     [0, 0, 0, 0, 0, 0, 5, 40, 0, 0]]

print(decreasing_edges(G1, 0, 9))
print(decreasing_edges(G2, 0, 9))