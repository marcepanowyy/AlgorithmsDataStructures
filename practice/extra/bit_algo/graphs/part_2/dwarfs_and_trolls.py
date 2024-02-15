# Wyobrazmy sobie podziemny labirynt, zlozony z ogromnych jaskin polaczonych waskimi korytarzami.
# lecture jednej z jaskin krasonuludy zbudowaly swoja osade, a w kazdej z pozostalych jaskin mieszka znana
# krasnoludom ilosc trolli. Krasnoludy chca zaplanowac swoja obrone na wypadek ataku ze strony trolli.
# Zamierzaja w tym celu zakrasc sie i podlozyc ladunek wybuchowy pod jeden z korytarzy, tak, aby trolle
# mieszkajace za tym korytarzem nie mialy zadnej sciezki, ktora moglyby dotrzec do osady krasnoludow.
# Ktory korytarz nalezy wysadzic w powietrze, aby odciac dostep do krasoludzkiej osady najwiekszej
# liczbie trolli?

# O(V+E)

G1 = [[1, 2, 5], [0, 3, 5], [0], [1,9], [5, 8], [0, 1, 4, 6], [5, 7], [6], [4], [3]]
Trolls = [0, 100, 10, 15, 4, 2, 6, 100, 1, 44]     # pozycje trolli
undercroft = 5                                     # wierzcholek z komnata krasnoludow

def blow_up_bridge(graph, T, undercroft):

    n = len(graph)
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
                T[u] += T[v]
            elif parents[u] != v:
                low[u] = min(low[u], times[v])   # przy sieganiu wprzod (krawedz wsteczna)

    dfs_visit(graph, undercroft)

    B = []

    for i in range(n):
        if times[i] == low[i] and parents[i] != None:
            B.append((parents[i], i))                               # most postaci (parent_vertex, vertex)

    bridge_id = -1
    max_= 0
    for i in range(len(B)):
        if T[B[i][1]] > max_:
            max_ = T[B[i][1]]
            bridge_id = i

    ans_bridge = B[bridge_id]

    print("remove bridge between vertices", ans_bridge)
    print("to prevent dwarfs from", max_, "trolls!")
    return ans_bridge

# blow_up_bridge(G1, Trolls, undercroft)

