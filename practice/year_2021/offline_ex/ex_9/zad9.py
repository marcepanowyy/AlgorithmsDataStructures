# lecture pewnym państwie znajdują się miasta, połączone siecią jednokierunkowych rurociągów, każdy o
# określonej przepustowości. Złoża ropy zostały wyczerpane, jednak w jednym z miast odkryto niewyczerpane
# źródło nowego rodzaju paliwa. Postanowiono zbudować dwie fabryki w różnych miastach
# oczyszczające nowe paliwo. Z pewnych względów fabryki te nie mogą znajdować się w mieście,
# w którym odkryto nowe złoża i nowe paliwo będzie transportowane istniejącą siecią rurociągów.
# Należy wskazać dwa miasta w których należy zbudować fabryki aby zmaksymalizować produkcję
# oczyszczonego paliwa.

# Proszę zaimplementować funkcję maxflow(G,s), która dla istniejącej sieci rurociągów G i miasta,
# w którym odkryto złoże s, zwróci maksymalną łączną przepustowość do dwóch miast w których
# należy zbudować fabryki. Miasta są ponumerowane kolejnymi liczbami 0, 1, 2, ... Sieć rurociągów
# opisuje lista trójek: (miasto w którym rozpoczyna się rurociąg, miasto w którym się kończy rurociąg,
# przepustowość rurociągu)

# Przykład Dla sieci G = [(0,1,7),(0,3,3),(1,3,4),(1,4,6),(2,0,9),(2,3,7),(2,5,9),
# (3,4,9),(3,6,2),(5,3,3),(5,6,4),(6,4,8)] oraz miasta s=2 wynikiem jest 25 (miasta 4 i 5).

# modifikuję listę krawędzi na graf V x V okreslajacy zbior polaczen miedzy wierzcholkami.
# Dodaję dodatkowy wierzcholek. Nastepnie, dla kazdej pary dwoch wierzcholkow (u, v)
# takich, ze (u != v i u != s i v != s). Lacze wierzcholki u, v z dodatkowym wierzcholkiem x i
# wyznaczam optymalny przeplyw algorytmem edmondsa karpa zaczynajac ze zrodla s, konczac na
# wierzcholku x, ktory jest tak naprawde ujsciem. Rozwazajac kazda pare wierzcholkow (u, v)
# wyznaczam rozwiazanie.

from zad9testy import runtests
from collections import deque

def create_graph(G):

    n = len(G)
    m = max(max(G, key=lambda x: x[0])[0], max(G, key=lambda x: x[1])[1])
    m += 2

    new_G = [[0] * m for _ in range(m)]
    for u, v, w in G:
        new_G[u][v] = w

    return new_G


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
    new_graph = [row[:] for row in graph]
    parents = [None] * n
    max_flow = 0

    while bfs(new_graph, s, t, parents):

        curr_flow_val = get_bottleneck_value(new_graph, parents, s, t)
        max_flow += curr_flow_val
        update(new_graph, parents, curr_flow_val, s, t)

    return max_flow

def maxflow(graph, s):

    graph = create_graph(graph)     # with additional vertex
    n = len(graph) - 1
    max_flow = 0

    for i in range(n-1):
        graph[i][n] = float("inf")
        for j in range(i+1, n-1):
            if i != s != j:
                graph[j][n] = float("inf")
                max_flow = max(max_flow, edmonds_karp(graph, s, n))
                graph[j][n] = 0
        graph[i][n] = 0

    return max_flow

runtests(maxflow, all_tests=True)
