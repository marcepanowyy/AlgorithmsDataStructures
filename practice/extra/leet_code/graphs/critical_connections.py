# Critical Connections in a Network

# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server
# connections forming a network where connections[i] = [ai, bi] represents a connection between
# servers ai and bi. Any server can reach other servers directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

# Return all critical connections in the network in any order.

def create_graph(connections, n):

    graph = [[] for _ in range(n)]

    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    return graph

def critical_connections(connections, n):

    graph = create_graph(connections, n)
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
