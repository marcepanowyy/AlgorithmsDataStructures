# Na osi liczbowej znajduje się N punktów większych od M = 10^K. Z punktu A można przeskoczyć
# na punkt B wtedy i tylko wtedy gdy A%10^K == B//10^K. Proszę zaimplementować funkcję:
# def order(L, K):
# ...
# porządkującą punkty, tak aby możliwe było przejście od najwcześniejszego punktu w tym porządku,
# kolejno przez wszystkie punkty, do ostatniego. Funkcja otrzymuje listę wartości określającą położenie
# punktów na osi liczbowej i powinna zwrócić listę punktów w kolejności ich odwiedzania. Jeżeli
# uporządkowanie punktów nie jest możliwe, funkcja powinna zwrócić None.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
# użytego algorytmu.

# Przykład. Dla danych:

# L = [56,15,31,43,54,35,12,23]
# K = 1

# przykładowym, prawidłowym wynikiem jest lista:
# L = [12,23,31,15,54,43,35,56]

# liczby to krawedzie, szukamy sciezki eulera (zrobilem pod koniec slownikiem XDD)

from zad2testy import runtests

def conditionEulerianPath(IN, OUT):

    n = len(IN)
    c1, c2 = 0, 0

    for i in range(n):
        if IN[i] - OUT[i] == 1:
            c1 += 1
            end_node = i
        if OUT[i] - IN[i] == 1:
            c2 += 1
            start_node = i

    if c1 > 1 or c2 > 1:
        return None

    if c1 == 0 and c2 == 0:
        return 0

    for i in range(n):
        if i != end_node and i != start_node and IN[i] != OUT[i]:
            return None

    return start_node

def count_degrees(G):

    n = len(G)
    IN, OUT = [0] * n, [0] * n

    for u in range(n):
        for v in G[u]:
            OUT[u] += 1
            IN[v] += 1

    return conditionEulerianPath(IN, OUT)


class Vertex:
    def __init__(self):
        self.id = None
        self.next = None


def create(G):

    n = len(G)
    modified_G = []
    edges = 0

    for u in range(n):
        head = Vertex()
        tail = head
        for v in G[u]:
            new_vertex = Vertex()
            new_vertex.id = v
            tail.next = new_vertex
            tail = tail.next
            edges += 1
        modified_G.append(head.next)

    return modified_G, edges


def eulerian_path(G):

    start_node = count_degrees(G)
    if start_node == None: return start_node
    solution_path = []

    modified_G, no_edges = create(G)

    def dfs_visit(modified_G, u):

        while modified_G[u] != None:

            v = modified_G[u].id
            modified_G[u] = modified_G[u].next
            dfs_visit(modified_G, v)

        solution_path.append(u)

    dfs_visit(modified_G, start_node)

    if len(solution_path) != no_edges+1: return False               # graf nie byl spojny
    return solution_path

def create_new_graph(edges):

    m = max(max(edges, key=lambda x: x[0])[0], max(edges, key=lambda x: x[1])[1])
    new_graph = [[] for _ in range(m+1)]

    for u, v in edges:
        new_graph[u].append(v)

    return new_graph

def order(L, k):

    m = 10 ** k
    my_dict = {}
    edges = []

    for num in L:
        edges.append([num % m, num // m])
        my_dict[num % m, num // m] = num

    new_graph = create_new_graph(edges)
    path = eulerian_path(new_graph)[::-1]
    res = []

    n = len(path)
    for i in range(1, n):
        res.append(my_dict[path[i-1], path[i]])

    return res[::-1]

# runtests(order)