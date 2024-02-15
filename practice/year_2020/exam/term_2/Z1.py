# Dany jest zbior przedzialow domknietych I = {[a1,b1,], ... [an, bn]} gdzie kazdy przedzial zaczyna sie i konczy na liczbie naturalnej (wliczajac 0). Dane sa
# takze dwie liczby naturalne x i y. Da przedzialy mozna skleic (czyli zamienic na prezdzial bedacy ich suma mnogosciowa), jesli maja dokladnie jeden punkt wspolny.
# Jesli pewne prezdzialy mozna posklejac tak, ze powstanie z nich prezdzial [x,y], to mowimy, ze sa przydatne. Prosze napisac funkcje

# def intuse(I, x, y)

# ktora zwraca liste numerow wszystkich przydatnych prezdzialow. Zbior I jest reprezentowany jako lista par opisjacych przedzialy. Prosze oszacowac zloznosc czasowa
# i pamieciowa uzytego algorytmu

# przyklad. Dla danych:
#
# I = [(3,4), (2,5), (1,3), (4,6), (1,4)]
# x = 1
# y = 6

# prawidlowym wynikiem wywoalania intuse(I, x, y) jest dowolna permutacja listy [0,2,3,4]

# Michał Madeja
# Algorytm w pierwszej kolejności tworzy niepowtarzalną, posortowaną tablicą trans (translacji), wykorzystywaną do mapowania początków i końców
# przedziałów do indeksów.  Dzięki binarySearch słownik ten działa w O(log n). Wielkość słowinika jest rzędu n (dzięki słownikowi nie jest rzędu y).
# Na podstawie trans i listy krawędzi I tworzona jest macierz (listy sąsiedztwa, z dołączonym indeksem krawędzi z pierwotnej tablicy). Krawędź z i do j
# oznacza że istnieje przedział od trans[i] do trans[j].
# Rozwiązaniem problemu są krawędzie należące do wszystkich ścieżek z trans.index(x) do trans.index(y) w stworzonym grafie.
# Zmodyfikowany DFS do znalezienia wszystkich ścieżek z x do y.
# Czasowa: O(n*logn)
# Pamięciowa: O(n)


def DFS(G, x, y):
    n = len(G)
    visited = [False for _ in range(n)]
    onPathArr = [False for _ in range(n)]
    result = []

    def DFSVisit(G, u):
        nonlocal result
        visited[u] = True

        for [v, idx] in G[u]:
            if not visited[v]:
                if v == y:
                    result.append(idx)
                    DFSVisit(G, v)
                    onPathArr[v] = True
                    onPathArr[u] = True
                elif v > y:
                    DFSVisit(G, v)
                else:
                    DFSVisit(G, v)
                    if onPathArr[v]:
                        result.append(idx)
                        onPathArr[u] = True
            else:
                if onPathArr[v]:
                    result.append(idx)
                    onPathArr[u] = True

    DFSVisit(G, x)
    return result


# G = [[],
#      [3,4],
#      [5],
#      [1,4],
#      [1,6],
#      [2],
#      [4]]



def intuse0(I, x, y):
    trans = []
    for pair in I:
        trans.extend(pair)

    trans.sort()

    maxVal = max(trans)
    for i in range(len(trans) - 1):
        if trans[i] == trans[i + 1]:
            trans[i] = maxVal
    trans.sort()

    while trans[-2] == maxVal:
        trans.pop()

    m = len(trans)
    M = [[] for _ in range(m)]

    def binarySerch(x):
        l = 0
        r = m - 1

        while l <= r:
            mid = (r + l) // 2
            if x == trans[mid]:
                return mid
            elif x < trans[mid]:
                r = mid - 1
            elif x > trans[mid]:
                l = mid + 1
        return None

    for i in range(len(I)):
        pair = I[i]
        M[binarySerch(pair[0])].append([binarySerch(pair[1]), i])

    xAdr = binarySerch(x)
    yAdr = binarySerch(y)
    if xAdr != None and yAdr != None:
        return DFS(M, xAdr, yAdr)
    else:
        return []


# runtests(intuse)

I = [(3,4), (2,5), (1,3), (4,6), (1,4)]
x = 1
y = 6

# intuse(I, x, y)

# my sol (bledne)

# def create_graph(I):
#     n = len(I)
#     max_ = -float("inf")
#     for i in range(n):
#         max_ = max(max_, I[i][0], I[i][1])
#     G = [[] for _ in range(max_+1)]
#
#     for i in range(n):
#         for j in range(n):
#             if I[i][0]=
#
#             G[I[i][0]].append((I[i][1], i))         # przedzial (1,3) to krawedz 1-3, druuga wartosc jest id krawedzi (numer przedzialu)
#             G[I[i][1]].append((I[i][0], i))
#
#     return G
#
# from queue import *
#
# def intuse(I, s, t):
#
#     G = create_graph(I)
#     n = len(G)
#     inf = float('inf')
#     visited = [False] * n
#     parents = [[] for _ in range(n)]
#     q = Queue()
#     q.put((s, None, -1))
#
#     while not q.empty():
#         u, parent, id= q.get()
#         visited[u] = True
#         parents[u].append((parent, id))
#
#         if u == t: continue
#
#         for v, id in G[u]:
#             if not visited[v]:
#                 q.put((v, u, id))
#
#     res = []
#
#     def go_straight(u, id):
#         nonlocal res, s
#
#         if id not in res: res.append(id)
#
#         if u != s:
#             new_u, id = parents[u].pop()
#             go_straight(new_u, id)
#
#
#
#     for i in range(len(parents[t])):
#         u, id = parents[t].pop()
#         go_straight(u, id)
#
#
#
#     return res
#
# # runtests(intuse)
#
# I = [(4, 4), (4, 10), (2, 15), (6, 16), (3, 8), (2, 14), (6, 21), (3, 1), (0, 5), (7, 15), (3, 19), (2, 17), (4, 24), (7, 10), (5, 8), (4, 21), (6, 22), (9, 27), (2, 18),
#    (1, 6), (5, 14), (5, 13), (0, 18), (10, 16), (9, 24), (11, 24), (5, 7), (6, 14), (1, 7), (3, 19), (11, 18), (6, 9), (11, 19), (9, 27), (7, 11), (13, 17), (10, 24), (8, 16), (11, 25),
#    (11, 25), (11, 26), (12, 30), (4, 9), (5, 11), (10, 20), (6, 12), (14, 33), (13, 18), (8, 25), (15, 26)]
# x = 1
# y = 10
#
# # "hint":[13,28]
#
# intuse(I, x, y)
