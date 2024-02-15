# Max Association In Bipartite Graph

# Problem maksymalnego skojarzenia w grafie dwudzielnym

# BG = (U, V, E) - graf dwudzielny

# skojarzenie - zbior krawedzi, taki, ze zadne dwie nie maja wspolnego wierzcholka

BG1 = [[1, 3, 5], [0], [3], [0, 2, 4], [3, 5], [0, 4, 6], [5]]
BG2 = [[1, 3, 5], [0], [3], [0, 2, 4], [3, 5], [0, 4, 6], [5, 7], [6]]

from bipartite import bipartite
from ResidualNetwork.EdmondsKarp import edmonds_karp

def create_graph(graph):

    colours = bipartite(graph)
    n = len(graph)
    new_graph = [[0] * (n+2) for _ in range(n+2)]  # wierzcholek n jest zrodlem, n+1 ujsciem

    for u in range(n):
        if colours[u] == 0:
            for v in graph[u]:
                new_graph[u][v] = 1                # ustawiamy skierowane krawedzie od zbioru X (0) do zbiory Y (1)

            new_graph[n][u] = 1                    # ustawiamy skierowane krawedzie od zrodla do zbioru X (0)

        else:
            new_graph[u][n+1] = 1                  # ustawiamy skierowane krawedzie od zbioru Y (1) do ujscia


    return new_graph


def max_matching(BG):

    graph = create_graph(BG)
    n = len(graph) - 2
    return edmonds_karp(graph, n, n+1)

# print(max_matching(BG1))
# print(max_matching(BG2))


