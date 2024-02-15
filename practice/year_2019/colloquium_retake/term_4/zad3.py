# [2pkt.] Zadanie 3.

# Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b
# jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a] −
# T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej
# do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić
# wartość -1.

# Przykład Dla tablicy T = [123,890,688,587,257,246] wynikiem jest liczba 767, a dla tablicy
# T = [587,990,257,246,668,132] wynikiem jest liczba -1

from zad3testy import runtests
from queue import PriorityQueue

def is_connected(m, n):

    A, B = [0] * 10, [0] * 10

    while m != 0:
        A[m % 10] += 1
        m //= 10

    while n != 0:
        B[n % 10] += 1
        n //= 10

    for i in range(10):
        if A[i] and B[i]:
            return True

    return False

def create(T):

    n = len(T)

    graph = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if u != v and is_connected(T[u], T[v]):
                graph[u].append([v, abs(T[u] - T[v])])

    return graph


def find_cost(T):

    n = len(T)
    s = min(range(len(T)), key=T.__getitem__)
    t = max(range(len(T)), key=T.__getitem__)
    graph = create(T)

    weights = [float("inf")] * n
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()

        if min_w < weights[u]:
            weights[u] = min_w

            if u == t: return min_w

            for v, weight in graph[u]:
                if weights[v] == float("inf"):
                    pq.put((weights[u] + weight, v, u))

    return -1

# runtests(find_cost)
