def find_bridges(G):

    n = len(G)
    low = [0] * n
    times = [0] * n
    bridges = []
    time = 0

    def dfs(u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time

        for v in G[u]:
            if not times[v]:
                dfs(v, u)
                if low[v] < low[u]: low[u] = low[v]          # cykl

            elif v != parent:
                if times[v] < low[u]: low[u] = times[v]      # krawedz wsteczna

        if times[u] == low[u] and parent >= 0:
            bridges.append((parent, u))

    for i in range(n):
        if not times[i]:
            dfs(i, -1)

    return bridges



# 1. Wykonaj DFS, dla kazdego v zapisujac jego czas odwiedzenia d(v)
# 2. Dla kazdego v obliczamy low(v)

# low(v) = min(d(v), min(d(u), low(w))

# u to takie wierzcholki, ze mamy krawedz wsteczna z v do u
# czyli  krawedz po ktorej nie mozemy przejsc bo wierzcholek u zostal
# odwiedzony wczesniej

# w jest dzieckiem v w drzewie dfs

# mosty to krawedzie {v, p(v)} p(v) - ojciec w drzewie DFS
# gdzie d(v) = low(v)

# low - identyfikator cyklu

# O(V+E)

def bridges(graph):

    n = len(graph)
    visited = [False] * n
    parents = [None] * n
    times = [-1] * n
    low = [float("inf")] * n
    time = 1

    def dfs_visit(graph, u):

        nonlocal time
        times[u] = time
        low[u] = min(low[u], times[u])
        time += 1
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                parents[v] = u
                dfs_visit(graph, v)
                low[u] = min(low[u], low[v])     # przy cofaniu sie
            elif parents[u] != v:
                low[u] = min(low[u], times[v])   # przy sieganiu wprzod


    for u in range(n):
        if not visited[u]:
            dfs_visit(graph, u)

    B = []

    for i in range(n):
        if times[i] == low[i] and parents[i] != None:
            B.append((parents[i], i))

    return B

G1 = [[1,4], [0,2], [1,3,4], [2,5,6], [0,2,7], [3,6], [3,5], [4]]
G2 = [[1], [0,2], [1,3], [2]]
G3 = [[1,2], [0,2,3], [0,1], [1,4,5], [3], [3]]

# print(bridges(G1))
# print(bridges(G2))
# print(bridges(G3))



def bridges2(graph):

    n = len(graph)
    tin = [0] * n
    low = [0] * n
    vis = [0] * n
    ans = []

    def dfs(u, parent, timer):

        vis[u] = 1
        tin[u] = low[u] = timer

        timer += 1

        for v in graph[u]:
            if v == parent:
                continue
            if vis[v] == 0:
                dfs(v, u, timer)

                low[u] = min(low[u], low[v])

                if low[v] > tin[u]:
                    ans.append([v, u])
            else:
                low[u] = min(low[u], tin[v])

    timer = 0

    for i in range(n):
        if vis[i] == 0:
            dfs(i, -1, timer)
    return ans

# print(bridges2(G3))

# bridges3

def find_bridges(G: 'graph represented by adjacency lists'):
    n = len(G)
    low = [0] * n
    times = [0] * n
    bridges = []
    time = 0

    def dfs(u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time

        for v in G[u]:
            # when there is no visit time, a vertex hasn't been yet visited
            if not times[v]:
                dfs(v, u)
                # If we have a cycle, we must update the low value of the parent vertex
                if low[v] < low[u]: low[u] = low[v]
            # v cannot be a parent of u as it's obvious it will always be visited before
            # and connected to the vertex u which doesn't imply that we have a back edge
            elif v != parent:
                # We have a back edge (we try to enter a vertex which was entered before)
                if times[v] < low[u]: low[u] = times[v]

        # We will start from parent -1 as the first vertex has no parent
        if times[u] == low[u] and parent >= 0:
            bridges.append((parent, u))

    # Check all possible starting vertices as a graph doesn't have to be consistent
    for i in range(n):
        if not times[i]:
            dfs(i, -1)

    return bridges


def undirected_graph_list(E: 'array of edges', n: 'number of vertices'):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G


# xxxxxxxx


