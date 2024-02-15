def floyd_warshall(graph):

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

    return D