from collections import deque

# O(VE**2)

def bfs(graph, s, t, parents):

    n = len(graph)
    d = deque([])

    visited = [False] * n
    d.append(s)
    visited[s] = True

    while d:
        u = d.popleft()
        for v in range(n):
            w = graph[u][v]
            if not visited[v] and w > 0:
                d.append(v)
                visited[v] = True
                parents[v] = u

    return visited[t]

def get_bottleneck_value(graph, parents, s, t):

    if s == t: return float("inf")

    curr_v = t
    parent_v = parents[t]
    edge_w = graph[parent_v][curr_v]

    return min(edge_w, get_bottleneck_value(graph, parents, s, parent_v))

def update(graph, parents, curr_flow_val, s, t):

    if s == t: return

    curr_v = t
    parent_v = parents[t]
    graph[parent_v][curr_v] -= curr_flow_val
    graph[curr_v][parent_v] += curr_flow_val

    update(graph, parents, curr_flow_val, s, parent_v)

def edmonds_karp(graph, s, t):

    n = len(graph)
    parents = [None] * n
    max_flow = 0

    while bfs(graph, s, t, parents):

        curr_flow_val = get_bottleneck_value(graph, parents, s, t)
        max_flow += curr_flow_val
        update(graph, parents, curr_flow_val, s, t)

    return max_flow


