# Proszę zaimplementować algorytm sprawdzający czy graf jest dwudzielny (czyli zauważyć, że to
# 2-kolorowanie i użyć DFS lub bfs).

from collections import deque

def bipartite_graph(graph, s):

    n = len(graph)
    d = deque([])
    colors = [-1] * n         # -1 kolor nie zostal przydzielony, 0 - kolor bialy, 1 kolor czarny

    d.append(s)
    colors[s] = 1

    while d:
        u = d.popleft()
        for v in graph[u]:
            if colors[v] == -1:
                colors[v] = 1 - colors[u]
                d.append(v)
            elif colors[u] == colors[v]:
                return False

    return True

G1 = [[1,2,3],[0,4],[0,5],[0,6],[1,7],[2,7],[3,7],[4,5,6]]
G2 = [[1],[0,2,3],[1,3],[1,2]]

# print(bipartite_graph(G1, 0))
# print(bipartite_graph(G2, 0))

