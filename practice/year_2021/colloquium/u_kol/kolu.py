from kolutesty import runtests
from collections import deque

def get_degree_arr(depends):                     # tworzy tablice stopni wierzcholkow krawedzi do nich wchodzacych
                                                 # arr[i] - # ilosc wchodzacych krawedzi do wierzcholka i
    n = len(depends)
    graph = [[] for _ in range(n)]
    degree_arr = [0] * n

    for i, arr in enumerate(depends):
        for k in arr:
            degree_arr[k] += 1

    return degree_arr


def bfs(graph, degree_arr, disk):

    n = len(graph)
    dist = [float("inf")] * n
    visited = [False] * n
    parents = [None] * n
    d = deque([])

    for i in range(n):                  # dodaje wierzcholki, ktore nie maja krawedzi wchodzacych
        if not degree_arr[i]:
            d.append(i)
            dist[i] = 0
            visited[i] = True

    while d:

        u = d.popleft()

        if parents[u] != None:
            dist[u] = dist[parents[u]] + (1 if disk[parents[u]] != disk[u] else 0)

        for v in graph[u]:

            degree_arr[v] -= 1

            if not visited[v] and degree_arr[v] <= 0:
                visited[v] = True
                parents[v] = u

                if disk[v] == disk[u]: d.appendleft(v)        # jesli ta sama stacja dyskow to dodajemy na lewo, zeby zminimalizowac koszty
                else: d.append(v)

    return dist[u]

def swaps(disk, depends):

    degree_arr = get_degree_arr(depends)
    return bfs(depends, degree_arr, disk)

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(swaps, all_tests = True)