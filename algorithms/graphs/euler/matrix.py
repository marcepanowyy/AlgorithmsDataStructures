# Ze sprawdzeniem, czy istnieje ścieżka lub cykl Eulera i zwróceniem odpowiednio ścieżki lub cyklu.

def undirected_graph_matrix(E: 'array of edges', n: 'number of vertices'):
    M = [[0] * n for _ in range(n)]
    # Store information which vertices are connected with an edge
    for edge in E:
        M[edge[0]][edge[1]] = M[edge[1]][edge[0]] = 1
    return M


def is_consistent(G: 'graph represented using adjacency matrix'):
    n = len(G)
    visited = [False] * n

    def dfs(i):
        visited[i] = True
        for j in range(n):
            if G[i][j] and not visited[j]:
                dfs(j)

    dfs(0)
    return all(visited)


# Checks if a graph has either an euler cycle or an euler path
# Returns:
# 0 - if there is neither euler cycle nor euler path in a graph,
# 1 - if there is euler cycle,
# 2 - if there is euler path.

def is_eulerian(G: 'graph represented using adjacency matrix'):
    if not is_consistent(G): return 0, -1
    n = len(G)
    odd_count = 0
    begin_vertex = 0
    # Check for each vertex if its degree is even
    for i in range(n):
        deg = 0
        for j in range(n):
            if G[i][j]: deg += 1
        # If a degree of a vertex is odd, increment a number of odd degree vertices
        # and check if we exceeded the maximum number of odd degree vertices
        if deg % 2:
            begin_vertex = i
            odd_count += 1
            if odd_count > 2:
                return 0, -1
    if odd_count == 0: return 1, begin_vertex
    if odd_count == 2: return 2, begin_vertex
    return 0, -1


# Generate either an euler cycle or an euler path
def euler(G: 'graph represented using adjacency matrix'):
    # Check if a graph has an euler cycle or an euler path
    g_type, begin_i = is_eulerian(G)
    if g_type == 0: return [], g_type

    n = len(G)
    result = []

    def dfs(i):
        for j in range(n):
            # Is still not visited
            if G[i][j] == 1:
                # Remove an edge (by replacing 1 with -1)
                G[i][j] = G[j][i] = -1  # I assume the graph is not directed
                dfs(j)
        result.append(i)

    # Run dfs algorithm to search for the euler cycle
    dfs(begin_i)

    # Restore original values of edges (replace -1 with 1)
    for i in range(n):
        for j in range(n):
            G[i][j] = abs(G[i][j])

    return result, g_type