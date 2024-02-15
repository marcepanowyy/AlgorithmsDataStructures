# szukamy minimalnej wartosci z dwoch wartosci
# 1. sciezka z a do b bez wykorzystania szybowca
# 2. sciezka z a do najblizszego lotniska + sciezka z b do najblizszego lotniska

# ElogV wzorcowka

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 0.15 sek.
# Status testów: A A A A A A A A A A


from kol3btesty import runtests
from queue import PriorityQueue

def create_graph(graph, A, n):

    for i in range(n):
        graph[i] = [graph[i], A[i]]

    return graph

def dijkstra(graph, a, b, n):

    weights = [float("inf")] * n
    pq = PriorityQueue()
    pq.put((0, a))

    while not pq.empty():
        min_w, u = pq.get()

        if min_w < weights[u]:
            weights[u] = min_w

            if u == b: return min_w

            for v, weight in graph[u][0]:
                if weights[v] == float("inf"):
                    pq.put((weights[u] + weight, v))

    return float("inf")


def find_min(graph, n, a, A):

    weights = [float("inf")] * n
    pq = PriorityQueue()
    pq.put((0, a, False))
    pq.put((A[a], a, True))

    while not pq.empty():
        min_w, u, used_szybowiec = pq.get()

        if used_szybowiec: return min_w

        if min_w < weights[u]:
            weights[u] = min_w

            for v, weight in graph[u][0]:
                if weights[v] == float("inf"):

                        pq.put((weights[u] + weight, v, False))
                        pq.put((weights[u] + weight + graph[v][1], v, True))

    return float("inf")

def airports(G, A, s, t):

    n = len(G)
    graph = create_graph(G, A, n)
    res = min(dijkstra(graph, s, t, n), find_min(graph, n, s, A) + find_min(graph, n, t, A))
    return res if res != float("inf") else None

runtests(airports, all_tests=True)
