# takie jak zad.3 z II kolosa 2020/2021 tylko bez poczatkowego bfs

# Paweł Konop

# Algorytm zachlanny
# wydluzamy zasieg dodajac do obecnej wartosci zasiegu
# wartosc maksymalna na odcinku [0, range] zwiekszajac zasieg,
# dopoki range >= n-1

# nlogn

from zad5testy import runtests
from queue import PriorityQueue

def plan(T):

    n = len(T)
    res = [0]
    radius = T[0]
    pointer = 1
    pq = PriorityQueue()

    if radius >= n - 1:
        return res

    while pointer != n-1:
        while pointer <= radius and pointer != n-1:
            if T[pointer] != 0:
                pq.put((-T[pointer], pointer))
            pointer += 1

        extra_range, index = pq.get()
        extra_range *= (-1)
        res.append(index)
        radius += extra_range
        if radius >= n-1:
            res.sort()
            return res

    return None

runtests(plan, all_tests = True)