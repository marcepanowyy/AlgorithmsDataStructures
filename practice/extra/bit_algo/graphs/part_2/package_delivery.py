# Dostarczanie przesyłek

# Bitocja jest kraina zawierajaca N miast, N-1 dwukierunkowych drog i uklad drog tworzy
# graf spojny. Majac liste K miast do ktorych musimy dostarczyc przesyłki i mogac wystartowac
# i zakonczyc trase w dowolnym miescie, podaj minimalny dystans, ktory musimy przebyc,
# zeby zrealizowac to zadanie

# graf to drzewo es

def undirected_graph_list(E):
    n = len(E) + 1
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G


def map_graph(G: 'graph represented by adjacency lists', C: 'array of cities to visit'):
    n = len(G)
    k = len(C)

    visits = [0] * n
    for i in range(k):
        visits[C[i]] = 2  # Mark cities which will be visited

    def dfs(u):
        found_to_visit = visits[u] == 2
        visits[u] = 1
        for v in G[u]:
            if visits[v] == 0 or visits[v] == 2:
                if dfs(v):
                    found_to_visit = True

        if not found_to_visit:
            visits[u] = -1

        return found_to_visit

    dfs(C[0])

    for u in range(n):
        if visits[u] == -1:
            G[u] = []
        else:
            # We must also remove edges which join cities
            # on a path with unvisited cities
            edges = []
            for v in G[u]:
                if visits[v] == 1:
                    edges.append(v)
            G[u] = edges


def diameter_helper(G, begin_u):
    n = len(G)
    visited = [False] * n
    max_u = max_dist = 0

    def dfs(u, dist):
        nonlocal max_u, max_dist
        if dist > max_dist:
            max_dist = dist
            max_u = u

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v, dist + 1)
        return dist

    dfs(begin_u, 0)

    return max_dist, max_u


def tree_diameter(G: 'graph represented by adjacency lists'):
    n = len(G)
    for u in range(n):
        if G[u]: break
    _, u = diameter_helper(G, u)
    diam, v = diameter_helper(G, u)
    return diam, u, v


def min_dist(G: 'graph represented by adjacency lists', C: 'array of cities to visit'):
    n = len(G)

    map_graph(G, C)

    total_dist = 0
    for u in range(n):
        total_dist += len(G[u])

    diam, begin_city, end_city = tree_diameter(G)
    total_dist -= diam

    return total_dist, begin_city, end_city

E = [(3,2),(2,4),(2,1), (1,5), (1,0), (0,6), (6,7), (6,8), (6,9), (8,10)]
C = [3, 4, 7]
G = undirected_graph_list(E)

dist, begin_city, end_city = min_dist(G, C)
print('Minimum distance:', dist)
print('Start at city:', begin_city)
print('End at city:', end_city)