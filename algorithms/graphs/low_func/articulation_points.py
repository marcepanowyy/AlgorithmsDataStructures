def find_articulation_points(graph):

    n = len(graph)
    low = [0] * n
    times = [0] * n
    is_art = [False] * n
    time = 0

    def dfs(root, u, parent):

        nonlocal time, out_deg
        if parent == root: out_deg += 1
        time += 1
        low[u] = times[u] = time

        for v in graph[u]:

            if v == parent: continue

            if not times[v]:
                dfs(root, v, u)
                low[u] = min(low[u], low[v])

                if times[u] <= low[v]: is_art[u] = True

            else: low[u] = min(low[u], times[v])

    for u in range(n):
        if not times[u]:
            out_deg = 0
            dfs(u, u, -1)
            is_art[u] = out_deg > 1

    return [u for u in range(n) if is_art[u]]

G1 = [[1], [0,2], [1]]
G2 = [[1,2,3], [0,2], [0,1], [1,4,5], [3], [3]]
G3 = [[2], [2], [0,1,3], [2]]
G4 = [[1,3], [0,2], [1,3], [0,4], [3,5], [4,6,8], [5,7], [6,8,9], [5,7], [7,10,11], [9,11], [9,10]]

# print(find_articulation_points(G1))
# print(find_articulation_points(G2))
# print(find_articulation_points(G3))
# print(find_articulation_points(G4))