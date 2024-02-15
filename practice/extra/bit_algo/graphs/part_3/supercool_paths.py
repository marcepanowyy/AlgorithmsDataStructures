# Sciezki superfajne

# Dany jest graf wazony G. Sciezka superfajna, to taka, ktora jest nie tylko najkrotsza
# wagowo sciezka miedzy v i u, ale takze ma najmniejsza liczbe krawedzi (inaczej mowiac,
# szukamy najkrotszych sciezek w sensie liczby krawedzi wsrod najkrotszych sciezek w sensie
# wagowym). Podaj algorytm, ktory dla danego wierzcholka startowego s znajdzie superfajne
# sciezki do pozostalych wierzcholkow.

from queue import PriorityQueue

def dijkstra(G, s, t):

    n = len(G)
    weights = [float("inf")] * n
    parents = [None] * n
    edge_num = [float("inf")] * n
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()

        if min_w <= weights[u] and (edge_num[u] > (edge_num[parent] + 1 if parent != None else 0)):
            weights[u] = min_w
            edge_num[u] = edge_num[parent] + 1 if parent != None else 0
            parents[u] = parent

            for v, weight in G[u]:
                if weights[v] == float("inf"):
                    pq.put((weights[u] + weight, v, u))


    return edge_num[t], weights[t]

G1 = [[[1,3],[7,8]],
      [[0,3],[2,4]],
      [[1,4],[3,6],[8,10]],
      [[7,5],[4,2],[2,6]],
      [[3,2],[5,1]],
      [[4,1],[6,2]],
      [[5,2],[8,1]],
      [[0,8],[3,5]],
      [[2,10],[6,1]]]

# print(dijkstra(G1, 0, 6))