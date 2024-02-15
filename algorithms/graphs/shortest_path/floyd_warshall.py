# szukanie najkrotszej odleglosci z kazdego wiezrcholka do pozostalych

# n - n

# korzystamy z wierzcholkow wewnetrznych wykorzystujac dp

# O(V^3) przy grafie w ktorym mozliwe sa ujemne krawedzie (V wywołan dijkstry tez by mialo v^3, ale nie uwzglednia ujemych krawedzi)

# interesuje nas w zasadzie tylko reprezentacja macierzowa

# D[u][v] - dlugosc najkrotszej sciezki z u do v

def floyd_warshall(graph: 'graph represented by adjacency matrix'):

    n = len(graph)
    D = [[float("inf")] * n for _ in range(n)]

    for u in range(n):                             # warunki poczatkowe
        for v in range(n):
            if graph[u][v]:
                D[u][v] = graph[u][v]
            elif u == v:
                D[u][v] = 0

    for t in range(n):                             # D(t)[u][v] - dl. najkrotszej sciezki z u do v, jesli mozna po drodze korzystac z
        for u in range(n):                         # wierzcholków v0, v1, v2, ..., vt
            for v in range(n):
                if D[u][t] + D[t][v] < D[u][v]:
                    D[u][v] = D[u][t] + D[t][v]

    for t in range(n):                             # sprawdzamy czy nie ma ujemnych cykli
        for u in range(n):
            for v in range(n):
                if graph[u][t] + graph[t][v] < graph[u][v]:
                    graph[u][v] = float("-inf")

    return D

inf = float("inf")

G1 = [[0, 6, 5, 5, inf, inf, inf],
      [inf, 0, inf, inf, -1, inf, inf],
      [inf, -2, 0, inf, 1, inf, inf],
      [inf, inf, -2, 0, inf, -1, inf],
      [inf, inf, inf, inf, 0, inf, 3],
      [inf, inf, inf, inf, inf, 0, 3],
      [inf, inf, inf, inf, inf, inf, 0]]


# print(*floyd_warshall(G1), sep='\n')

G2 = [[0, 3, inf, 7],
      [8, 0, 2, inf],
      [5, inf, 0, 1],
      [2, inf, inf, 0]]

# print(*floyd_warshall(G2), sep='\n')
