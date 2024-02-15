# Ze sprawdzeniem, czy istnieje ścieżka lub cykl Eulera i zwróceniem odpowiednio ścieżki lub cyklu.

def undirected_graph_list(E: 'array of edges', n: 'number of vertices'):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G


def is_consistent(G: 'graph represented using adjacency list'):
    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)

    dfs(0)
    return all(visited)


# Checks if a graph has either an euler cycle or an euler path
# Returns:
# 0 - if there is neither euler cycle nor euler path in a graph,
# 1 - if there is euler cycle,
# 2 - if there is euler path.

def is_eulerian(G: 'graph represented using adjacency list'):
    if not is_consistent(G): return 0, -1
    n = len(G)
    odd_count = 0
    begin_vertex = 0
    # Check for each vertex if its degree is even
    for u in range(n):
        if len(G[u]) % 2:
            odd_count += 1
            begin_vertex = u
    if odd_count == 0: return 1, begin_vertex
    if odd_count == 2: return 2, begin_vertex
    return 0, -1


# Generate either an euler cycle or an euler path
def euler(G: 'graph represented using adjacency list'):
    # Check if a graph has an euler cycle or an euler path
    g_type, begin_u = is_eulerian(G)
    if g_type == 0: return [], g_type

    n = len(G)
    result = []
    visited = [[False] * n for _ in range(n)]

    def dfs(u):
        for v in G[u]:
            if not visited[u][v]:
                visited[u][v] = visited[v][u] = True
                dfs(v)
        result.append(u)

    dfs(begin_u)

    return result, g_type

E1 = [(0,1), (1,2), (2,3), (3,4), (4,0), (0,2), (1,3), (2,4), (3,0), (4,1)]
E2 = [(0,1), (1,2), (2,3), (3,4), (4,0), (0,2), (1,3), (2,4), (3,0)]

G1 = undirected_graph_list(E1, 5)
G2 = undirected_graph_list(E1, 5)

# print(euler(G1))
# print(euler(G2))

