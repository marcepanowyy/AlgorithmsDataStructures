# Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać z miasta (wierzchołka) s do
# miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką samą jednostkową opłatę.
# Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby opłat. lecture ogólności
# graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.

from collections import deque

def edges_01(graph, s):

    n = len(graph)
    cost = [float("inf")] * n
    visited = [False] * n

    d = deque([])
    d.append(s)
    cost[s] = 0

    while d:
        u = d.popleft()
        for v in range(n):
            if graph[u][v] != -1 and not visited[v]:
                cost[v] = min(cost[v], cost[u] + graph[v][u])
                if graph[u][v] == 0:
                    d.appendleft(v)
                else:
                    d.append(v)
                visited[u] = True

    return cost[-1]


graph = [[-1, 1, 0, 1, -1, -1, -1, -1],
         [1, -1, 1, -1, 0, 0, -1, -1],
         [0, 1, -1, -1, -1, 1, -1, -1],
         [1, -1, -1, -1, -1, -1, 1, -1],
         [-1, 0, -1, -1, -1, -1, -1, 1],
         [-1, 0, 1, -1, -1, -1, 1, -1],
         [-1, -1, -1, 1, -1, 1, -1, 1],
         [-1, -1, -1, -1, 1, -1, 1, -1],]

# print(edges_01(graph, 0))