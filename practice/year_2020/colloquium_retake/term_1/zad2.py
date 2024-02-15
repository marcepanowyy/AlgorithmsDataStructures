# Dany jest graf spójny nieskierowany G = (V, E) $. Proszę zaimplementować funkcję:
#
# def breaking(G):
#     ...
#
# która zwraca taki jego wierzchołek, że jego usunięcie (razem z incydentnymi krawędziami) powoduje, że graf rozpadnie się na
# jak najwięcej nie połączonych ze sobą części. Funkcja przyjmuje graf reprezentowany przez kwadratową, symetryczną macierz
# sąsiedztwa i zwraca numer wierzchołka, z założeniem numeracji od zera. Jeśli usunięcie żadnego wierzchołka nie spowoduje tego,
# że graf przestanie być spójnym, funkcja powinna zwracać None.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.

from zad2testy import runtests

def find_articulation_points(G: 'graph represented by adjacency matrix'):

    n = len(G)
    low = [0] * n
    times = [0] * n
    is_art = [False] * n
    time = 0

    def dfs(root, u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time
        out_deg = 0

        for v in range(n):
            if not G[u][v] or v == parent: continue
            if not times[v]:
                out_deg += dfs(root, v, u) + u == root
                low[u] = min(low[u], low[v])
                if times[u] <= low[v]:
                    is_art[u] = True
            else:
                low[u] = min(low[u], times[v])

        return out_deg

    # Check all possible starting vertices as a graph doesn't have to be consistent
    for u in range(n):
        if not times[u]:
            is_art[u] = dfs(u, u, -1) > 1

    return is_art


def number_components(G, is_art):
    n = len(G)
    numbers = [-1] * n
    token = 0

    def dfs(u):
        numbers[u] = token
        for v in range(n):
            if G[u][v] and numbers[v] < 0 and not is_art[v]:
                dfs(v)

    for u in range(n):
        if numbers[u] < 0:
            if not is_art[u]:
                dfs(u)
            else:
                numbers[u] = token
            token += 1

    return numbers


def breaking(G):
    n = len(G)
    is_art = find_articulation_points(G)
    c_num = number_components(G, is_art)
    print(c_num)
    # Look fo an articulation point which splits a graph into the
    # greatest number of separate components
    found_c = [0] * n
    token = 1

    max_count = 0
    best_u = None

    for u in range(n):
        if is_art[u]:
            count = 0
            for v in range(n):
                if G[u][v] and found_c[c_num[v]] < token:
                    found_c[c_num[v]] = token
                    count += 1
            if count > max_count:
                max_count = count
                best_u = u
        token += 1

    return best_u


# runtests(breaking)