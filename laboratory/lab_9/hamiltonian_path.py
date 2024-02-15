# (ścieżka Hamiltona w DAGu) Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie
# wierzchołki w grafie, przez każdy dokładnie raz. lecture ogólnym grafie znalezienie ścieżki Hamiltona jest pro-
# blemem NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym
# grafie skierowanym.

# sortowanie topologiczne

def check_HP_DAG(G):

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

    for i in range(n-1):
        if result[i+1] not in G[result[i]]:
            return False

    return True


G1 = [[1,3,4], [2,3], [3], [4,5], [], []]

# print(check_HP_DAG(G1))

G2 = [[1,3,4], [2,3], [3], [4,5], [], [], [4]]

# print(check_HP_DAG(G2))

G3 = [[1,3,4], [2,3], [3], [4], []]

# print(check_HP_DAG(G3))
