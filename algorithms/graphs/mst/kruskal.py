# Kruskal dla reprezentacji Grafu w postaci [(0,1,4),...] - krawedz z 0 do 1 o wadze 4

class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):

    x = find(x)
    y = find(y)

    if x == y:
        return

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

# Minimalne Drzewo Rozpinajace (Minimal Spanning Tree) MST O(ElogE)

def kruskal(G):
    E = []
    n = len(G)
    vertices = [Node(i) for i in range(n)]
    G = sorted(G, key=lambda x: x[2])
    for e in G:
        u, v = e[0], e[1]
        if find(vertices[u]) != find(vertices[v]):
            E.append(e)
            union(vertices[u], vertices[v])
    return E


G = [(0,1,1),
     (1,2,3),
     (1,4,7),
     (3,4,12),
     (2,3,7),
     (2,6,1),
     (3,6,8),
     (3,5,2),
     (4,5,4),
     (5,7,10),
     (5,8,6),
     (7,8,5)]

# print(kruskal(G))

# Kruskal dla reprezentacji macierzowej

def KRUSKAL(G):
    V = len(G)
    #struktura find/union
    parent = [i for i in range(V)]
    rank = [0]*V
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x,y):
        a = find(x)
        b = find(y)
        if rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[a] = b
            if rank[a] == rank[b]:
                rank[b] += 1

    # tworzymy tablicę krawędzi V^2 (w listach sąsiedztwa dodajemy tylko gdy i > j, mamy E <= V^2)
    E = []
    for i in range(V):
        for j in range(i):
            if G[i][j] > 0:
                E.append((i,j,G[i][j]))
    E = sorted(E, key= lambda weight: weight[2]) # ElogE

    #tworzymy tablicę do wyniku i wstawiamy do niej elementy. E * logarytm iterowany z E
    A = []
    for e in E:
        if find(e[0]) != find(e[1]):
            A.append(e)
            union(e[0], e[1])
    return A

G = [[0,2,0,0,0,6,1],
     [2,0,3,0,0,0,0],
     [0,3,0,1,0,0,2],
     [0,0,1,0,7,0,0],
     [0,0,0,7,0,8,5],
     [6,0,0,0,8,0,0],
     [1,0,2,0,5,0,0]]

# print(KRUSKAL(G))

