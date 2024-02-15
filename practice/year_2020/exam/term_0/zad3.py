from zad3testy import runtests
from queue import PriorityQueue

def convert(graph):

    n = len(graph)
    new_graph = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if graph[u][v]:
                new_graph[u].append([v, graph[u][v]])
                new_graph[v].append([u, graph[u][v]])

    return new_graph

def jumper(G, s, t):

    n = len(G)
    G = convert(G)
    weights = [[float("inf")] * 3 for _ in range(n)]   # weights[u][0] - mozemy skorzystac z dwumilowych butow,
    parents = [[None] * 3 for _ in range(n)]           # weights[u][1] - jeszcze nie mozemy
    pq = PriorityQueue()                               # weights[u][2] - przed momentem skoczylismy

    pq.put((0, s, None, 1, 0))                            # 1 - mozemy wykorzystac dwumilowe buty
    pq.put((0, s, None, 0, 0))                            # 0 - nie mozemy
    pq.put((0, s, None, -1, 0))                           # -1 - przed momentem skoczylismy

    def id(i):
        if i == -1: return 2
        if i == 0: return 1
        if i == 1: return 0

    while not pq.empty():

        min_w, u, parent, can_jump, prev_edge = pq.get()

        i = id(can_jump)                         # tylko, zeby polapac sie gdzie wpisac do tablicy

        if min_w < weights[u][i]:
            weights[u][i] = min_w
            parents[u] = parent

            if u == t: break

            if can_jump == 1:                                                                           # jesli mozemy skoczyc:

                for v, weight in G[u]:
                    if weights[v][0] == float("inf"):
                        pq.put((weights[u][1] + weight, v, u, 1, weight))                               # a) nie wykorzystujemy butow
                    if weights[v][1] == float("inf"):
                        pq.put((weights[u][0] - prev_edge + max(prev_edge, weight), v, u, -1, weight))  # b) wykorzystujemy buty

            elif can_jump == 0:                                                                         # jesli jeszcze nie mozemy skoczyc:

                for v, weight in G[u]:                                                                  # a) nie wykorzystujemy butoww
                    if weights[v][0] == float("inf"):
                        pq.put((weights[u][1] + weight, v, u, 1, weight))
            else:                                                                                       # jesli przed momentem skoczylismy:
                for v, weight in G[u]:
                    if weights[v][1] == float("inf"):                                                   # a) czekamy
                        pq.put((weights[u][2] + weight, v, u, 0, weight))


    # print(weights[t])
    return min(weights[t])

# runtests(jumper)


def jumper_asia(G, s, w):

    n = len(G)
    D = [[float("inf")] * 2 for _ in range(n)]
    D[s][0] = D[s][1] = 0

    for parent in range(n):
        for u in range(n):
            for v in range(n):

                if G[parent][u] > 0 and G[u][v] > 0 and parent != u and parent != v and v != u: # skaczemy
                    if D[v][1] > D[parent][0] + max(G[parent][u], G[u][v]):
                        D[v][1] = D[parent][0] + max(G[parent][u], G[u][v])

                if G[u][v] > 0 and u != v:                                                      # idziemy normalnie
                    if D[v][0] > G[u][v] + min(D[u][0],D[u][1]):
                        D[v][0] = G[u][v] + min(D[u][0], D[u][1])


    return min(D[w])

# runtests(jumper_asia)
