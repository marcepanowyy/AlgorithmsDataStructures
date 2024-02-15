# Przewodnik chce przewieźć grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych
# miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. Mamy daną listę trójek postaci
# (x, y, c), gdzie x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich turystów i musi ich podzielić na grupki tak, żeby
# każda grupka mogła przebyć trasę bez rozdzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), żeby wszyscy
# dostali się z A do B.


from queue import PriorityQueue
from math import ceil


def create(G):

    s = len(G)
    n = max(G, key=lambda x: x[0])
    n = max(n)
    new_G = [[] for _ in range(n+1)]

    for i in range(s):
        u = G[i][0]
        v = G[i][1]
        weight = G[i][2]
        new_G[u].append([v, weight])
        new_G[v].append([u, weight])

    return new_G


def get_solution(parents, s, t):
    if t == s: return [s]
    return [t] + get_solution(parents, s, parents[t])

def tour_guide(G, s, t, K):

    G = create(G)
    n = len(G)
    limit = [0] * n
    limit[0] = float("inf") # mozemy przepuscic inf ludzi przez wierzcholek startowy
    parents = [None] * n
    pq = PriorityQueue()

    for v, c in G[s]:
        if limit[v] == 0:
            pq.put((-min(limit[s], c), v, s))

    while not pq.empty():
        max_limit, u, parent = pq.get()
        max_limit *= (-1)

        if max_limit > limit[u]:
            limit[u] = max_limit
            parents[u] = parent
            if u == t: break

            for v, c in G[u]:
                if limit[v] == 0:
                    pq.put((-min(limit[u], c), v, u))

    final_limit = limit[t]
    route = get_solution(parents, s, t)[::-1]

    res = ceil(K/final_limit)
    print("route to be executed:", route)
    print("gotta divide into", res, "groups")

    return parents, limit


G1 = [(0,1,3), (0,2,1), (0,3,8), (1,2,6), (1,5,5), (2,4,6), (5,4,3), (5,7,7), (4,7,7), (6,7,7), (3,6,1), (3,4,8)]

# tour_guide(G1, 0, 7, 15)

