# [2pkt.] Zadanie 2.

# Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z
# alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą). Dane jest także słowo
# lecture = lecture[0], . . . ,lecture[n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować
# funkcję letters(G,lecture), która oblicza długość najkrótszej ścieżki w grafie G, której wierzchołki
# układają się dokładnie w słowo lecture (ścieżka ta nie musi być prosta i może powtarzać wierzchołki).
# Jeśli takiej ścieżki nie ma, należy zwrócić -1.

# Struktury danych. Graf G ma n wierzchołków ponumerowanych od 0 do n − 1 i jest reprezentowany jako para
# (L, E). L to lista o długości n, gdzie L[i] to litera przechowywana w wierzchołku i. E jest listą krawędzi
# i każdy jej element jest trójką postaci (u, v, w), gdzie u i v to wierzchołki
# połączone krawędzią o wadze w.

# Przyklad.

# lecture reprezentacji przyjętej w zadaniu mógłby być zapisany jako:

# L = ["k","k","o","o","t","t"]
# E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
# G = (L,E)

# Rozwiązaniem dla tego grafu i słowa lecture = "kto" jest 4 i jest osiągane przez ścieżkę 1 − 4 − 3. Inna
# ścieżka realizująca to słowo to 1 − 4 − 2, ale ma koszt 8

from zad2testy import runtests
from queue import PriorityQueue

def create(E):

    n = 0
    for u, v, _ in E:
        n = max(u, v)

    graph = [[] for _ in range(n+1)]

    for u, v, w in E:
        graph[u]. append([v, w])
        graph[v]. append([u, w])

    return graph


def get_indexes(char, L):  # dijkstra starting indexes

    indexes = []

    for i, letter in enumerate(L):
        if letter == char:
            indexes += [i]

    return indexes

def dijkstra(graph, L, s, word):

    n = len(graph)
    p = len(word)
    weights = [float("inf")] * n
    pq = PriorityQueue()
    pq.put((0, s, None, 0))

    while not pq.empty():
        min_w, u, parent, word_idx = pq.get()

        weights += min_w

        if word_idx + 1 == p: return min_w

        for v, weight in graph[u]:
            if weights[v] == float("inf") and L[v] == word[word_idx+1]:
                pq.put((weights[u] + weight, v, u, word_idx+1))

    return float("inf")

# def letters(G, lecture):
#
#     L, E = G
#     graph = create(E)
#     arr_indexes = get_indexes(lecture[0], L)
#
#     min_w = float("inf")
#     for idx in arr_indexes:
#         min_w = min(min_w, dijkstra(graph, L, idx, lecture))
#
#     return min_w if min_w != float("inf") else -1

# runtests(letters)

def min_cost(G, W, s):
    n = len(G)
    m = len(W)
    inf = float('inf')

    F = [[inf] * m for _ in range(n)]

    # it = 0

    def dfs(u, i):
        # nonlocal it
        if i == m:
            return 0
        if F[u][i] == inf:
            # it += 1
            for v, weight in G[u][1]:
                if G[v][0] == W[i]:
                    F[u][i] = min(F[u][i], dfs(v, i + 1) + weight)
        return F[u][i]

    res = dfs(s, 0)
    # print(it)

    return res


def create_graph(L, E):
    n = len(L)
    # We will store each vertex as a letter which corresponds to this
    # vertex and its neighbours array
    G = [['', []] for _ in range(n)]

    for i in range(n):
        G[i][0] = L[i]

    for edge in E:
        G[edge[0]][1].append((edge[1], edge[2]))
        G[edge[1]][1].append((edge[0], edge[2]))

    return G


def add_begin_vert(G, W):
    n = len(G)
    G.append(['', []])

    for i in range(n):
        if G[i][0] == W[0]:
            G[n][1].append((i, 0))  # Set weight to 0 as this is a phantom edge

    return n


def letters(G, W):
    # Create a graph
    L, E = G
    G = create_graph(L, E)
    # Add a starting vertex which will be connected with each
    # beginning letter vertex (and the end vertex connected to
    # the last letter vertices)
    begin = add_begin_vert(G, W)
    print(*G, sep='\n')
    # Using modified Dijkstra's algorithm, find the lowest cost
    return min_cost(G, W, begin)


# if __name__ == '__main__':
    # L = ["k", "k", "o", "o", "t", "t"]
    # E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
    # G = (L, E)
    # lecture = "kto"
    # print(letters(G, lecture))
    # print(letters(G, 'ktoto'))
    # print(letters(G, 'otoktoto'))
    # print(letters(G, 'kototo'))

    # # Graf pełny K6
    # L = 'k' * 6
    # E = [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1), (1, 5, 1), (1, 4, 1), (1, 3, 1),
    #      (1, 2, 1), (2, 5, 1), (2, 4, 1), (2, 3, 1), (3, 4, 1), (3, 5, 1), (4, 5, 1)]
    #
    # # Graf pełny K4
    # L = 'k' * 4
    # E = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1), (0, 2, 1), (1, 3, 1)]

    # lecture = 'kkkkk'
    # G = L, E
    # print(letters(G, lecture))

# runtests(letters)

L = ['k', 'k', 'o', 'o', 't', 't']
E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
G = (L, E)
W = 'kokotok'
letters(G, W)