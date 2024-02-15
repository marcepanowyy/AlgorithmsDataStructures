# Krawedz zmniejszajaca dystans

# Dany jest graf wazony z dodatnimi wagami G. Dana jest tez lista E krawedzi, ktore
# nie naleza do grafu, ale sa krawedziami miedzy wierzcholkami z G. Dane sa rowniez dwa
# wierzcholki s i t. Podaj algorytm, ktory stwierdzi, ktora jedna krawedz z E nalezy wszczepic
# do G, aby jak najbardziej zmniejszyc dystans miedzy s i t. Jezeli zadna krawez nie poprawi dystansu miedzy
# s i t, to algorytm powinien to stwierdzic

# [nie bierzemy krawedzi, bierzemy krawedz]

from queue import PriorityQueue

# G1 - initial graph
# G2 - graph representing additional edges

def saving_edge(G1, G2, s, t):

    n = len(G1)
    weights = [[float("inf")] * 2 for _ in range(n)]
    parents = [[None] * 2 for _ in range(n)]
    which_edge_taken = [None] * n

    pq = PriorityQueue()
    pq.put((0, s, None, 0, None))
    pq.put((0, s, None, 1, None))

    while not pq.empty():
        min_w, u, parent, edge_taken, edge_id = pq.get()

        if min_w < weights[u][edge_taken]:

            if edge_taken: which_edge_taken[u] = edge_id
            weights[u][edge_taken] = min_w
            parents[u][edge_taken] = parent

            for v, weight in G1[u]:
                if weights[v][edge_taken] == float("inf") and not edge_taken:   # nie bierzemy dodatkowej krawedzi (mozemy jeszcze skorzystac)
                    pq.put((weights[u][0] + weight, v, u, 0, None))

                elif weights[v][edge_taken] == float("inf") and edge_taken:     # nie bierzemy dodatkowej krawedzi (skorzystalismy z tego wczesniej)
                    pq.put((weights[u][1] + weight, v, u, 1, edge_id))

            for v, weight in G2[u]:
                if weights[v][1] == float("inf") and not edge_taken:            # wykorzystujemy dodatkowa krawedz
                    pq.put((weights[u][0] + weight, v, u, 1, [u, v, weight]))

    # print(*weights, sep="\n")

    if weights[t][0] <= weights[t][1]:
        print("no additional edge needed to create shortest path")
        return None

    print("shortes path from", s, "to", t, "is", weights[t][1], "long!")
    print("used edge between vertices:", which_edge_taken[t][0], which_edge_taken[t][1], "with", which_edge_taken[t][2], "weight!")
    return weights[t][1], which_edge_taken[t]

G1 = [[[1, 2], [2, 100], [6, 10]],
      [[0, 2], [5, 8]],
      [[0, 100], [3, 3]],
      [[2, 3], [4, 45]],
      [[3, 45], [6, 5], [7, 5]],
      [[1, 8], [7, 6]],
      [[0, 10], [4, 5]],
      [[4, 5], [5, 6]]]

G2 = [[[2, 99], [5, 3]],
      [[4, 10], [6, 3]],
      [[0, 99]],
      [[6, 2], [7, 1]],
      [[1, 10]], [[0, 3]],
      [[1, 3], [3, 2]],
      [[3, 1]]]

# saving_edge(G1, G2, 0, 3)
# print()
# saving_edge(G1, G2, 0, 7)
# print()
# saving_edge(G1, G2, 0, 2)
# print()
# saving_edge(G1, G2, 0, 4)

G3 = [[[1, 2], [2, 100], [6, 10]],
      [[0, 2], [5, 8]],
      [[0, 100], [3, 3]],
      [[2, 3], [4, 45]],
      [[3, 45], [6, 5], [7, 50]],
      [[1, 8], [7, 6]],
      [[0, 10], [4, 5]],
      [[4, 50], [5, 6]]]

G4 = [[[2, 99], [5, 3]],
      [[4, 100], [6, 30]],
      [[0, 99]],
      [[6, 2], [7, 1]],
      [[1, 100]], [[0, 3]],
      [[1, 30], [3, 2]],
      [[3, 1]]]

# saving_edge(G3, G4, 0, 4)

