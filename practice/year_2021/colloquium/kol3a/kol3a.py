# szukamy minimalnej wartosci z dwoch wartosci
# 1. sciezka z a do b bez wykorzystania portali
# 2. sciezka z a do najblizszego portalu + sciezka z b do najblizszego portalu

# ElogV wzorcowka

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 0.21 sek.
# Status testów: A A A A A A A A A A


from kol3atesty import runtests
from queue import PriorityQueue

def create_graph(n, E, S):

    new_graph = [[] for _ in range(n)]

    for u, v, weight in E:
        new_graph[u].append([v, weight])
        new_graph[v].append([u, weight])

    for i in range(n):
        new_graph[i] = [new_graph[i], False]

    for odd in S:
        new_graph[odd][1] = True

    return new_graph

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


def find_min(graph, n, a):

    weights = [float("inf")] * n
    pq = PriorityQueue()
    pq.put((0, a, graph[a][1]))

    while not pq.empty():
        min_w, u, is_odd = pq.get()

        if min_w < weights[u]:
            weights[u] = min_w

            if is_odd: return min_w

            for v, weight in graph[u][0]:
                if weights[v] == float("inf"):

                    if graph[v][1]:
                        pq.put((weights[u] + weight, v, True))
                    else:
                        pq.put((weights[u] + weight, v, False))

    return float("inf")

def spacetravel(n, E, S, a, b):

    graph = create_graph(n, E, S)
    res = min(dijkstra(graph, a, b, n), find_min(graph, n, a) + find_min(graph, n, b))
    return res if res != float("inf") else None

# runtests(spacetravel, all_tests=True)
