# [2pkt.] Zadanie 2.

# Dany jest graf nieskierowany G = (V, E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować i
# zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie
# z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź).

# Algorytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego
# poprawność i oszacować złożoność obliczeniową.

# Algorytm należy zaimplementować jako funkcję:

# def enlarge(G, s, t):
# ...

# która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą
# warunki zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list
# sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0.
# Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest
# krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma.

# Jeśli w grafie oryginalnie nie było ścieżki z s do t to funkcja powinna zwrócić None.

# Przykład. Dla argumentów:

# G = [[1, 2],
#      [0, 2],
#      [0, 1]]
# s = 0
# t = 2

# wynikiem jest np. krotka: (0, 2)

from zad2testy import runtests
from queue import Queue                 # lepiej uzyc deque tak jak w 6 zadaniu off

def bfs(G, s):

    n = len(G)
    visited = [False] * n
    distance = [float("inf")] * n

    distance[s] = 0
    queue = Queue()
    queue.put(s)

    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                queue.put(v)

    return distance

def inner_bfs(G, s, t, distance1, distance2, spl):

    n = len(G)
    visited = [False] * n
    vertex_dist = [[] for _ in range(spl+1)]
    vertex_dist[0] += [s]

    queue = Queue()
    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not visited[v] and distance1[v] + distance2[v] == spl:
                visited[v] = True
                vertex_dist[distance1[v]] += [v]
                queue.put(v)
    return vertex_dist

def enlarge(G, s, t):

    n = len(G)
    distance1 = bfs(G, s)
    distance2 = bfs(G, t)
    spl = int(distance1[t])                                      # shortest path length
    vertex_dist = inner_bfs(G, s, t, distance1, distance2, spl)  # arr with num of vertex with same lenght from vertexs s,
                                                                 # arr[1] - num of vertex from s with distance 1
    if vertex_dist[0] == vertex_dist[1] == 1:
        return (vertex_dist[0], vertex_dist[1])
    for i in range(1, spl+1):
        if len(vertex_dist[i]) == len(vertex_dist[i-1]) == 1:
            return (vertex_dist[i][0], vertex_dist[i-1][0])

    return None


# runtests(enlarge) # wszystko git