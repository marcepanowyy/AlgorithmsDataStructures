# Mamy dany graf G = (V, E) z wagami w: E → N-{0} (dodatnie liczby naturalne). Chcemy znalezc scieżkę
# z wierzchołka u do v tak, by iloczyn wag był minimalny.

# logarytmujemy kazda krawedz log10(a)
# odpalamy dijkstre

from queue import PriorityQueue
from math import log10

def modify(G):

    n = len(G)
    for u in range(n):
        s = len(G[u])
        for e in range(s):
            G[u][e] = G[u][e][0], log10(G[u][e][1]), G[u][e][1]

    return G

def get_solution(G, parents, s, t):
    if parents[t] == None: return [s]
    return [t] + get_solution(G, parents, s, parents[t])

def dijkstra(G, s, t):

    n = len(G)
    G = modify(G)
    weights = [float("inf")] * n
    parents = [None] * n
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()
        # We will find the minimum total weight path only once so the
        # code below this if statement will be executed only once
        if min_w < weights[u]:
            weights[u] = min_w
            parents[u] = parent
            # Break a loop if we found a shortest path to the specified target
            if u == t: break
            # Add all the neighbours of the u vertex to the priority queue
            for v, weight, _ in G[u]:
                if weights[v] == float("inf"):
                    pq.put((weights[u] + weight, v, u))

    # weights informuje nas ile min trzeba przebyc, zeby dostac sie do itego wierzcholka
    # parent pozwala odtworzyc sciezke
    return get_solution(G, parents, s, t)[::-1]

G = [[[1,3], [3,50], [4,12]],
     [[0,3], [2,4]],
     [[1,4], [4,6], [7,1]],
     [[0,50], [4,3], [5,4], [10,100]],
     [[0,12], [2,6], [3,3], [5,10], [6,6]],
     [[3,4], [4,10], [6,1], [9,20]],
     [[4,6], [5,1], [7,6], [9,50]],
     [[2,1], [6,6], [8,3]],
     [[7,3]],
     [[5,20], [6,50]],
     [[3,100]]]

# print(dijkstra(G, 0, 9))