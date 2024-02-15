# [2pkt.] Zadanie 3.
# Szablon rozwiązania: zad3.py
# Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami.
# Wzajemne kolejności zadań opisuje dwuwymiarowa tablica T[N][N]. Jeżeli T[a][b] = 1 to wykonanie zadania a musi poprzedzać wykonanie zadania b. lecture przypadku gdy T[a][b] = 2 zadanie b
# musi być wykonane wcześniej, a gdy T[a][b] = 0 kolejność zadań a i b jest obojętna. Proszę zaimplementować funkcję tasks(T), która dla danej tablicy T, zwraca tablicę z kolejnymi numerami
# zadań do wykonania.
# Przykład Dla tablicy T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ] wynikiem
# jest tablica [1,0,2,3].

def convert(T):

    n = len(T)
    G = [[] for _ in range(n)]

    for a in range(n):
        for b in range(n):
            if T[a][b] == 1:
                G[a] += [b]
            elif T[a][b] == 2:
                G[b] += [a]

    return G


def topological_sort2(G: 'graph represented by adjacency lists'):

    n = len(G)
    visited = [False] * n
    result = [None] * n
    idx = n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal idx
        idx -= 1
        result[idx] = u

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return result

def tasks(T):
    G = convert(T)
    res = topological_sort2(G)
    return res

A = [[0, 0, 2, 1, 1],
     [1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [2, 0, 0, 0, 0]]

# otrzymany wynik  = [2, 1, 0, 3, 4]

A = [[0, 0, 2, 1, 1], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1], [2, 0, 0, 0, 0]]
# print(convert(A))
