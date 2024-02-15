def find_max_path(graph):     # or tree diameter

    # zaczynajac od wierzcholka s, szukamy najdluzszej sciezki z s do wierzcholka x. (interesuje nas rowniez
    # indeks wierzcholka x). Tradycyjnie dfs z tablica parentow zeby znac odleglosci

    visited = [False] * len(graph)
    parent = [None] * len(graph)
    dist = [float("inf")] * len(graph)
    parent[0] = None
    dist[0] = 0

    def dfs_visit(u):
        nonlocal graph, visited, parent, dist
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dist[v] = dist[parent[v]]+1
                dfs_visit(v)

    dfs_visit(0)

    # szukamy wierzcholka z ktorego odl jest najwieksza
    index_max = max(range(len(dist)), key = dist.__getitem__)

    # zerujemy wszystkie dotychczasowe wartosci parent oraz dist i visited

    visited = [False] * len(graph)
    parent = [None] * len(graph)
    dist = [float("inf")] * len(graph)
    dist[index_max] = 0

    # wywolujemy kolejny raz dfs_visit zaczynajac od wierzcholka o indeksie znalezionym linijke wczesniej

    dfs_visit(index_max)

    # szukamy indeksu ktory ma najwieksza odleglosc (drugi raz). Jest to poczatek naszej przykladowej najdluzszej sciezki
    index_max = index_max = max(range(len(dist)), key = dist.__getitem__)

    res = []

    def get_solution(parent, index_max):
        nonlocal res
        if parent[index_max] != None:
            get_solution(parent, parent[index_max])
        res.append(index_max)

    get_solution(parent, index_max)

    return res  # jezeli interesuje nas srednica to wystarczy nalozyc funkcje len na res

# G = [[1,2,3,4],[0,5],[0,7],[0],[0,8,9],[1,6],[5],[2],[4],[4]]
# print(find_max_path(G, 0))


# find_max_path(G)