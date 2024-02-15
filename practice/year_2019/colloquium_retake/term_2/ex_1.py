# [2pkt.] Zadanie 1.
# Szablon rozwiązania: zad1.py
# Każdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Korzeniem tego drzewa może być dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która
# przyjmuje nieskierowany, spójny i acyckliczny graf G (reprezentowany w postaci listy sąsiedztwa) i
# wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym wierzchołku drzewa była możliwie najmniejsza. Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić dowolny z
# nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij
# poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
# Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki
# numerujemy od 0. Argumentem best root(L) jest lista postaci:
# L = [l0,l1, . . . ,ln−1],
# gdzie li to lista zawierająca numery wierzchołków będących sąsiadami i−tego wierzchołka. Można
# przyjąć (bez weryfikacji), że lista opisuje graf spełniający warunki zadania. lecture szczególności, graf
# jest spójny, acykliczny, oraz jeśli a ∈ lb to b ∈ la (graf jest nieskierowany). Nagłówek funkcji powinien
# mieć postać:
# def best_root(L):
# ...
# Przykład. Dla listy sąsiedztwa postaci:
# L = [ [ 2 ],
# [ 2 ],
# [ 0, 1, 3],
# [ 2, 4 ],
# [ 3, 5, 6 ],
# [ 4 ],
# [ 4 ] ]
# funkcja powinna zwrócić wartość 3.

# interesuje nas srednica drzewa, na srodku srednicy bedzie lezal nasz wierzcholek

def find_max_path(graph, s):     # or tree diameter

    # zaczynajac od jakiegos wierzcholka s, szukamy najdluzszej sciezki z s do wierzcholka x. (interesuje nas rowniez
    # indeks wierzcholka x). Tradycyjnie dfs z tablica parentow zeby znac odleglosci

    visited = [False] * len(graph)
    parent = [None] * len(graph)
    dist = [float("inf")] * len(graph)
    parent[s] = None
    dist[s] = 0

    def dfs_visit(u):
        nonlocal graph, visited, parent, dist
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dist[v] = dist[parent[v]]+1
                dfs_visit(v)

    dfs_visit(s)

    # szukamy wierzcholka z ktorego odl jest najwieksza
    index_max = max(range(len(dist)), key = dist.__getitem__)

    # zerujemy wszystkie dotychczasowe wartosci parent oraz dist i visited

    visited = [False] * len(graph)
    parent = [None] * len(graph)
    dist = [float("inf")] * len(graph)
    dist[index_max] = 0

    # wywolujemy kolejny raz dfs_visit zaczynajac od wierzcholka o indeksie znalezionym linijke wczesniej

    dfs_visit(index_max)

    # szukamy indeksu ktory ma najwieksza odleglosc (drugi raz). Jest to poczatek naszej przykladowej najdluzszej sciezki
    index_max = index_max = max(range(len(dist)), key = dist.__getitem__)

    res = []

    def get_solution(parent, index_max):
        nonlocal res
        if parent[index_max] != None:
            get_solution(parent, parent[index_max])
        res.append(index_max)

    get_solution(parent, index_max)

    return res  # jezeli interesuje nas srednica to wystarczy nalozyc funkcje len na res

L =  [[ 2 ],
     [ 2 ],
     [ 0, 1, 3],
     [ 2, 4 ],
     [ 3, 5, 6 ],
     [ 4 ],
     [ 4 ]]

def best_root(G):

    diameter = find_max_path(G, 0)
    n = len(diameter)
    return diameter[n//2]

# L1 = [ [ 2 ], [ 2 ], [ 0, 1, 3], [ 2, 4 ],
#        [ 3, 5, 6 ], [ 4 ], [ 4 ] ]
# R1 = 3
#
# L2 = [ [ 2, 4 ], [ 3 ], [ 0 ], [ 1, 4 ], [ 0, 3 ] ]
# R2 = 4
#
# L3 = [ [ 2, 3 ], [ 3, 4, 5, 6 ], [ 0 ],
#        [ 0, 1 ], [ 1 ], [ 1 ], [ 1 ] ]
# R3 = 3
#
# L4 = [ [ 2 ], [ 2 ], [ 0, 1, 3, 4, 5, 6 ],
#        [ 2 ], [ 2 ], [ 2 ], [ 2 ] ]
# R4 = 2

# print(best_root(L1))
# print(best_root(L2))
# print(best_root(L3))
# print(best_root(L4))


# ROZW MATIEGO

""" O(V + E) - 3 razy DFS """

# from zad1testy import runtests

def is_connected(G: 'undirected weighted graph represented by adjacency lists'):
    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)

    dfs(0)

    return all(visited)


def max_val_idx(A):
    max_i = 0
    for i in range(1, len(A)):
        if A[i] > A[max_i]:
            max_i = i
    return max_i


def diam_dist(G: 'undirected weighted acyclic graph represented by adjacency lists'):
    n = len(G)
    inf = float('inf')
    # Find the first diameter end vertex
    dist = [inf] * n
    visited = [0] * n
    token = 1

    def dfs(u):
        visited[u] = token
        for v in G[u]:
            if visited[v] != token:
                dist[v] = dist[u] + 1
                dfs(v)

    # Find the first diameter end vertex
    dist[0] = 0
    dfs(0)
    diam_u = max_val_idx(dist)

    # Find distances of all vertices from the first diameter end vertex
    # and the second diameter end vertex
    token += 1
    dist[diam_u] = 0
    dfs(diam_u)
    diam_v = max_val_idx(dist)
    dist1 = dist[:]  # Copy all distances from the first diameter vertex

    # Find all distances from the second diameter end vertex
    token += 1
    dist[diam_v] = 0
    dfs(diam_v)
    dist2 = dist[:]  # Copy all distances from the second diameter vertex

    return dist1, dist2


def best_root(L: 'undirected weighted acyclic graph represented by adjacency lists'):
    inf = float('inf')
    # This case will occur if a graph is not connected
    # (then the max distance will be infinity beacause for every vertex
    # there is at least one verex in another component and each vertex
    # then has its max distance equal to infinity)
    if not is_connected(L):
        return -1

    n = len(L)
    dist1, dist2 = diam_dist(L)
    # Find a vertex of the lowest max dist
    best_u = None
    min_dist = inf
    for u in range(n):
        max_dist = max(dist1[u], dist2[u])
        if max_dist < min_dist:
            min_dist = max_dist
            best_u = u

    return best_u


# runtests(best_root)