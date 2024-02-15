# Uogolnienie problemu najkrotszych sciezek

# Oprocz dlugosci krawedzi, graf ma przypisane koszty wierzcholkow. Zdefiniujmy koszt sciezki
# jako sume kosztow jej krawedzi oraz sume kosztow wierzcholkow wraz z koncami

# jak znalezc najtansze sciezki miedzy wierzcholkiem startowym a wszystkimi pozostalymi?

# podaj rozw dla grafu skierowanego, jak i nieskierowanego

from queue import PriorityQueue

def dijkstra(G, s, vert_weights):

    n = len(G)
    weights = [float("inf")] * n
    parents = [None] * n
    pq = PriorityQueue()
    pq.put((vert_weights[s], s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()

        if min_w < weights[u]:
            weights[u] = min_w
            parents[u] = parent

            for v, weight in G[u]:
                if weights[v] == float("inf"):
                    pq.put((weights[u] + weight + vert_weights[v], v, u))


    return weights

G = [[[1, 4], [2, 3]],
     [[0, 4], [2, 8], [4, 1]],
     [[0, 3], [1, 8], [3, 6]],
     [[2, 6], [4, 22], [6, 5]],
     [[1, 1], [3, 22], [5, 2]],
     [[4, 2], [6, 8]],
     [[3, 5], [5, 8]]]

vert_weights = [12, 5, 3, 1, 1, 100, 15]

# print(dijkstra(G, 0, 5, vert_weights))
# print(dijkstra(G, 0, 6, vert_weights))


# dla mozliwych ujemnych wartosci

def bellman_ford(G, s, vert_weights):

    n = len(G)
    parents = [None] * n
    distance = [float("inf")] * n
    distance[s] = vert_weights[s]

    def relax(distance, parents, u, v, weight):
        if distance[u] + weight + vert_weights[v] < distance[v]:
            distance[v] = distance[u] + weight + vert_weights[v]
            parents[v] = u

    for i in range(n-1):                          # n-1 iteracji, kazda przybliza nas do rozwiazania
        for u in range(n):
            for v, weight in G[u]:
                relax(distance, parents, u, v, weight)

    # for u in range(n):                            # sprawdzamy czy nie ma ujemych cykli
    #     for v, w in G[u]:
    #         if distance[u] + w < distance[v]:
    #             return None

    return distance

# print(bellman_ford(G, 0, vert_weights))