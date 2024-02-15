# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there
# is an edge between nodes ai and bi in the tree.

# Return an array answer of length n where answer[i] is the sum of the distances between
# the ith node in the tree and all other nodes.

G = [[1, 2], [0], [0, 3, 4, 5], [2], [2], [2]]

def dfs(graph, root):

    n = len(graph)
    visited = [False] * n
    parents = [None] * n
    distance = [float("inf")] * n
    subtree_nodes = [1] * n             # including current node
    distance[root] = 0

    def dfs_visit(graph, u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                distance[v] = distance[u] + 1
                parents[v] = u
                dfs_visit(graph, v)
                subtree_nodes[u] += subtree_nodes[v]

    dfs_visit(graph, root)
    root_dist = sum(distance)
    return root_dist, parents, subtree_nodes

def dfs_count(graph, root):

    n = len(graph)
    root_dist, parents, subtree_nodes = dfs(graph, root)
    res_arr = [float("inf")] * n
    res_arr[root] = root_dist
    visited = [False] * n

    def dfs_res(graph, u):
        nonlocal n
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                closer_nodes = subtree_nodes[v]
                further_nodes = n - closer_nodes
                res_arr[v] = res_arr[parents[v]] - closer_nodes + further_nodes
                dfs_res(graph, v)

    dfs_res(graph, 0)
    return res_arr

def sum_of_distances(graph):
    return dfs_count(graph, 0)

# print(sum_of_distances(G))