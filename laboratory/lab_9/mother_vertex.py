# Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli każdy inny wierzchołek można
# osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który stwierdza czy dany graf
# zawiera dobry początek.

# przyklad, dla grafu

G1 = [[1,2], [3], [], [], [1], [2,6], [0,4]]

# dobrym poczatkiem jest wierzcholek 5
# do wierzcholka 0 docieramy 5->6->0
# do wierzcholka 1 docieramy 5->6->4->1
# do wierzcholka 2 docieramy 5->2
# do wierzcholka 3 docieramy 5->6->4->1->3
# do wierzcholka 4 docieramy 5->6->4
# do wierzcholka 5 docieramy 5->5
# do wierzcholka 6 docieramy 5->6

def dfs_visit(graph, u, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs_visit(graph, v, visited)

def mother_vertex(graph):

    n = len(graph)
    visited1 = [False] * n
    visited2 = [False] * n
    m_vertex = 0

    for u in range(n):
        if not visited1[u]:
            m_vertex = u
            dfs_visit(graph, u, visited1)

    dfs_visit(graph, m_vertex, visited2)

    for i in range(n):
        if not visited2[i]:
            return None
    return m_vertex

# print(mother_vertex(G1))

G2 = [[1], [], [0,3], []]

# print(mother_vertex(G2))