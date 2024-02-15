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