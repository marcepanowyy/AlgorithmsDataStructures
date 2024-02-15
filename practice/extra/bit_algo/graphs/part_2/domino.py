# Domino
# Mamy pewien uklad klockow domino. Otrzymujemy go w postaci par [a, b]. Jezeli
# przewrocimy klocek z to klocek b tez sie przewroci. Chcemy znalezc minimalna
# liczbe klockow, ktore trzeba przewrocic recznie, aby wszystkie domina były przewrocone

# spojne skladowe grafu (najprosciej dfs) O(V+E)

Dominos = [[1,2], [2,3], [3,8], [5,6], [10,12]]

def create(E):

    max_= 0
    for v1, v2 in E:
        max_ = max(max_, v1, v2)
    max_ += 1

    G = [[] for _ in range(max_)]

    for v1, v2 in E:
        G[v1].append(v2)
        G[v2].append(v1)

    return G

def count_connected_components(G):  #O(V+E)

    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)

    count = 0
    for u in range(n):
        if not visited[u] and G[u]:
            count += 1
            dfs(u)

    return count

def dominos_knock(Dominos):
    G = create(Dominos)
    return count_connected_components(G)

# print(dominos_knock(Dominos))
