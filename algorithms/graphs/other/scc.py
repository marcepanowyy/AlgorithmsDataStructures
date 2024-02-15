# Strongly Connected Components

# 1. Wykonaj DFS dla grafu wejsciowego zapisujac czasy PRZETWORZENIA!!! (nie odwiedzenia!)
# 2. Odwroc kolejnosc krawedzi
# 3. wykonaj kolejny DFS w kolejnosci malejacych czasow przetworzenia

def create(G):

    n = len(G)
    modified_G = [[] for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            modified_G[v].append(u)

    return modified_G

def dfs_times(G):

    n = len(G)
    visited = [False] * n
    times = [0] * n
    time = 0

    def dfs_visit(G, u):
        nonlocal time
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G, v)
        times[u] = time
        time += 1

    for u in range(n):                   # dla niekoniecznie niespojnego grafu
        if not visited[u]:
            dfs_visit(G, u)

    return times

def SSS(G):

    n = len(G)
    times = dfs_times(G)
    modified_G = create(G)
    visited = [False] * n
    colours = [0] * n             # ten sam kolor oznacza ze wierzcholki sa w tej samej SSS

    for i in range(n):
        times[i] = i, times[i]

    times.sort(key=lambda x: x[1], reverse=True)

    def dfs_visit(G, u, colour):
        visited[u] = True
        colours[u] = colour
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G, v, colour)

    colour = 0

    for i in range(n):
        if not visited[times[i][0]]:
            dfs_visit(modified_G, times[i][0], colour)
            colour += 1

    return colours

G = [[1,4], [2,3], [0,7], [4], [5], [3,6], [3], [9], [7,6], [10], [8]] # przyklad jak na wykladzie
SSS(G)

