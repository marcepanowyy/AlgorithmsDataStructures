# Zadanie 1. Proszę zaimplementować algorytm Dijkstry
# (dla wybranej przez prowadzącego reprezentacji grafu).

from queue import *

def dijkstra(G, s, t):

    n = len(G)
    inf = float('inf')
    weights = [inf] * n
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
            # if u == t: break
            # Add all the neighbours of the u vertex to the priority queue
            for v, weight in G[u]:
                if weights[v] == inf:
                    pq.put((weights[u] + weight, v, u))

    # weights informuje nas ile min trzeba przebyc, zeby dostac sie do itego wierzcholka
    # parent pozwala odtworzyc sciezke

    return parents, weights

