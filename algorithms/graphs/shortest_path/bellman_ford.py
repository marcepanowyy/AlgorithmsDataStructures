# obliczanie najkrotszych sciezek w sytuacji gdy wagi moga byc ujemne

# 1 - n

# dla listy sasiedztwa O(V*E)


def bellman_ford(G, s):

    n = len(G)
    inf = float("inf")
    parents = [None] * n
    distance = [inf] * n
    distance[s] = 0

    def relax(distance, parents, u, v, weight):
        if distance[u] + weight < distance[v]:
            distance[v] = distance[u] + weight
            parents[v] = u

    for i in range(n-1):                          # n-1 iteracji, kazda przybliza nas do rozwiazania
        for u in range(n):
            for v, weight in G[u]:
                relax(distance, parents, u, v, weight)

    for u in range(n):                            # sprawdzamy czy nie ma ujemych cykli
        for v, w in G[u]:
            if distance[u] + w < distance[v]:
                return None

    return distance, parents

G1 = [[[1,6],[2,5],[3,5]],
     [[4,-1]],
     [[1,-2],[4,1]],
     [[2,-2],[5,-1]],
     [[6,3]],
     [[6,3]],
     []]

# print(bellman_ford(G, 0))

G2 = [[[1,1]],
      [[2,3]],
      [[4,8], [3,-10]],
      [[1,4]],
      []]

print(bellman_ford(G2, 0))


def convert(L):
    n = len(L)
    G = [[None] * n for _ in range(n)]
    for u in range(n):
        for v, weight in L[u]:
            G[u][v] = weight
    return G

def describeGraphWithEdgesValues(G):
    for i in range(len(G)):
        for v, weight in G[i]:
            print("krawedz z", i, "do", v, "o wartosci:", weight)
        print("\n")

G = [[[1,6],[2,5],[3,5]], [[4,-1]],[[1,-2],[4,1]],[[2,-2],[5,-1]],[[6,3]],[[6,3]],[]]

# describeGraphWithEdgesValues(G)
# G = convert(G)
# print(G)


# dla macierzy sasiedztwa
# O(V*E)

def Bellman_Ford(G, s):

    n = len(G)
    inf = float("inf")
    parents = [None] * n
    distance = [inf] * n
    distance[s] = 0

    def relax(distance, parents, u, v, weight):
        if distance[u] + weight < distance[v]:
            distance[v] = distance[u] + weight
            parents[v] = u

    for i in range(n-1):
        for u in range(n):
            for v in range(n):
                if G[u][v] != None:
                    relax(distance, parents, u, v, G[u][v])

    for u in range(n):
        for v in range(n):
            if G[u][v] != None:
                if distance[v] > distance[u] + G[u][v]:
                    return None

    return distance, parents

G = [[None, 6, 5, 5, None, None, None],
     [None, None, None, None, -1, None, None],
     [None, -2, None, None, 1, None, None],
     [None, None, -2, None, None, -1, None],
     [None, None, None, None, None, None, 3],
     [None, None, None, None, None, None, 3],
     [None, None, None, None, None, None, None]]

# print(Bellman_Ford(G, 0))
