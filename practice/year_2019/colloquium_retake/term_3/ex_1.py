# # [2pkt.] Zadanie 1.
# # Szablon rozwiązania: zad1.py
# # Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego, który odpowiada mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak
# # krawędzi). lecture niektórych wierzchołkach są stacje paliw, podana jest ich lista P. Pełnego baku wystarczy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest tankowany do pełna.
# # Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej
# # trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych
# # na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej
# # odległość d bez tankowania).
# # Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj
# # złożoność obliczeniową.
# # Przykład Dla tablic

G = [[-1, 6,-1, 5, 2],
     [-1,-1, 1, 2,-1],
     [-1,-1,-1,-1,-1],
     [-1,-1, 4,-1,-1],
     [-1,-1, 8,-1,-1]]

P = [0,1,3]

# funkcja jak dojade(G, P, 5, 0, 2) powinna zwrócić [0,3,2]. Dla tych samych tablic funkcja
# jak dojade(G, P, 6, 0, 2) powinna zwrócić [0,1,2], natomiast jak dojade(G, P, 3, 0, 2)
# powinna zwrócić None.

from queue import PriorityQueue


def convert(Matrix, P, d):

    n = len(Matrix)
    L = [[]  for _ in range(n)]
    Fuel = [0] * n
    for i in range(n):
        for j in range(n):
            if Matrix[i][j] != -1:
                L[i].append([j, Matrix[i][j]])
        if i < len(P):
            Fuel[P[i]] = d

    return L, Fuel


def jak_dojade(G, P, d, s, t):

    G, Fuel = convert(G, P, d)

    print(G)
    print(Fuel)

    n = len(G)
    inf = float('inf')

    weights = [inf] * n
    parents = [None] * n

    pq = PriorityQueue()

    pq.put((0, s, None, Fuel[s]))

    while not pq.empty():

        min_w, u, parent, fuel_left = pq.get()

        if min_w < weights[u]:

            weights[u] = min_w
            parents[u] = parent
            if u == t: continue

            for v, weight in G[u]:

                if weights[v] == inf and fuel_left-weight >= 0:
                    if Fuel[v]:
                        pq.put((weights[u] + weight, v, u, d))                                # if there is a station in vertex, we fill up (tank is full)
                    else:
                        pq.put((weights[u] + weight, v, u, fuel_left-weight))

    path = []

    def get_solution(parents, end_vertex):
        nonlocal path
        if parents[end_vertex] != None:
            get_solution(parents, parents[end_vertex])
        path.append(end_vertex)

    get_solution(parents, t)

    if len(path) <= 1:
        return -1
    return path

G =[[-1, 5, -1, 2],
    [-1, -1, -1, -1],
    [5, -1, -1, 5],
    [2, 2, -1, -1]]
P = [2, 0]
d =  6
a =  2
b =  1
# otrzymany wynik  = [2, 0, 1]
# oczekiwana dlugosc trasy = 9
# Dlugosc otrzymanej trasy = 10
# Za dluga trasa!
# Blad!

print(jak_dojade(G,P,6,2,1))


# from math import inf
#
# def min_index(D, V):
#     ans = inf
#     x = -1
#     y = -1
#     for i in range(len(D)):
#         for j in range(len(D[i])):
#             if not V[i][j] and D[i][j] < ans:
#                 x = i
#                 y = j
#                 ans = D[i][j]
#     return x, y
#
#
# def jak_dojade(G, P, d, a, b):
#     n = len(G)
#     S = [False] * n
#     D = [[inf] * (d + 1) for _ in range(n)]
#     V = [[False] * (d + 1) for _ in range(n)]
#     parent = [[None] * (d + 1) for _ in range(n)]
#
#     for p in P:
#         S[p] = True
#
#     D[a][d] = 0
#
#     for _ in range(d * n):
#         x, y = min_index(D, V)
#         if x == -1:
#             break
#
#         if S[x]:
#             fuel = d
#         else:
#             fuel = y
#
#         for v in range(n):
#             if G[x][v] != -1 and G[x][v] <= fuel and not V[v][fuel - G[x][v]]:
#                 if D[v][fuel - G[x][v]] > D[x][y] + G[x][v]:
#                     D[v][fuel - G[x][v]] = D[x][y] + G[x][v]
#                     parent[v][fuel - G[x][v]] = [x, y]
#
#         V[x][y] = True
#
#     ind = 0
#     for i in range(1, d + 1):
#         if D[b][ind] > D[b][i]:
#             ind = i
#
#     curr = b
#     ans = []
#     while parent[curr][ind] is not None:
#         ans.append(curr)
#         curr, ind = parent[curr][ind]
#
#     ans.append(a)
#     ans.reverse()
#
#     if ans == [a]:
#         return None
#
#     return ans
#

import copy

G1 = [[-1, 5, -1, 2], [-1, -1, -1, -1], [5, -1, -1, 5], [2, 2, -1, -1]]
P1 = [2, 0]
L1 = 9
# a=2, b=1, d=6

G2 = [[-1, 2, -1, -1, 3], [2, -1, 2, -1, -1], [-1, 2, -1, 2, -1], [-1, -1, 2, -1, 3], [3, -1, -1, 3, -1]]
P2 = [0, 4]
L2 = 6

# print(jak_dojade(G2, P2, 3, 0, 3))

# a=0, b=3, d=4

G3 = [[-1, 3, -1, 5, -1, 2], [3, -1, 4, -1, -1, -1], [-1, 4, -1, 6, -1, -1], [-1, -1, 6, -1, 2, -1],
      [-1, 5, -1, 2, -1, 3], [2, -1, -1, -1, 3, -1]]
P3 = [0, 4, 5]
L3 = -1
# a=5, b=2, d=5


TESTS = [(G1, P1, 6, 2, 1, L1),
         (G2, P2, 4, 0, 3, L2),
         (G3, P3, 5, 5, 2, L3)]


def isok(G, P, d, a, b, path, exp_len):
    if exp_len < 0 and path == None:
        print("Brak sciezki, zgodnie z oczekiwaniem")
        return True
    if exp_len >= 0 and path == None:
        print("Rozwiazanie nie zwrocilo sciezki, mimo ze taka istnieje")
        return False

    if path[0] != a:
        print("Rozwiazanie zwraca bledny poczatek sciezki")

    tank = d
    sol_len = 0
    v = a
    for u in path[1:]:
        if G[v][u] < 0:
            print("Nie istnieje krawedz z %d to %d" % (v, u))
            return False
        tank -= G[v][u]
        sol_len += G[v][u]
        if tank < 0:
            print("Zabraklo benzyny na krawedzi z %d do %d" % (v, u))
            return False
        v = u
        if v in P:
            tank = d

    print("Dlugosc otrzymanej trasy =", sol_len)
    if sol_len > exp_len:
        print("Za dluga trasa!")
        return False

    return True


def runtests(f):
    OK = True
    for (G, P, d, a, b, L) in TESTS:
        res = f(copy.deepcopy(G), copy.deepcopy(P), d, a, b)
        print("----------------------")
        print("G =")
        for i in range(len(G)): print(G[i])
        print("P =", P)
        print("d = ", d)
        print("a = ", a)
        print("b = ", b)
        print("otrzymany wynik  =", res)
        print("oczekiwana dlugosc trasy =", L)

        if not isok(G, P, d, a, b, res, L):
            print("Blad!")
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")


# runtests(jak_dojade)