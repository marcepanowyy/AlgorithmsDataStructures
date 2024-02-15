# Dany jest nieskierowany graf G = (V, E) oraz dwa wierzcholki, s i t. Prosze
# zaimplementowac funkcje:

# def paths(G, s, t):
#   ...

# ktora zwraca liczbe krawedzi e takich, ze e wystepuje na pewnej najkrotszej sciezce z s do t.
# Graf dany jest jako lista list sasiedztwa w postaci [(v0, w0), ...], gdzie vi to numer
# wierzcholka, wi to waga krawedzi prowadzacej do wierzcholka vi. Wagi krawedzi sa dodatnie.

# Funkcja powinna byc mozliwie jak najszybsza. Prosze oszacowac zlozonosc czasowa i pamieciowa
# uzytego algorytmu

# Przyklad. Dla listy sasiedztwa postaci:

# G = [[(1,2),(2,4)],
#      [(0,2),(3,11),(4,3)],
#      [(0,4),(3,13)],
#      [(1,11),(2,13),(5,17),(6,1)],
#      [(1,3),(5,5)],
#      [(3,17),(4,5),(7,7)],
#      [(3,1),(7,3)],
#      [(5,7),(6,3)]]

# s = 0, t = 7

# funkcja powinna zwrocic wartosc 7. Krawedzie 0-1, 1-4, 4-5, 5-7, 1-3, 3-6, 6-7

from queue import PriorityQueue
from zad3testy import runtests

def paths(graph, s, t):

    n = len(graph)
    weights = [float("inf")] * n
    parents = [[] for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()

        if min_w <= weights[u]:
            weights[u] = min_w
            parents[u] += [parent]

            if u == t: continue

            for v, weight in graph[u]:
                if weights[v] == float("inf"):
                    pq.put((weights[u] + weight, v, u))


    edges = [[0] * n for _ in range(n)]
    counter = 0

    def fill_graph(s, t):

        nonlocal counter
        if s == t: return

        while parents[t]:
            v = parents[t].pop()
            if not edges[t][v]:
                edges[t][v] = 1
                counter += 1

            fill_graph(s, v)

    fill_graph(s, t)
    return counter

# runtests(paths)
