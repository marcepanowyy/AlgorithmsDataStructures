# Lotniska

# Dostajemy na wejsciu liste trojek (miastoA, miastoB, koszt). Kazda z nich oznacza
# ze mozemy zbudowac droge miedzy miastem A i B za podany koszt. Ponadto, w dwolonym miescie
# mozemy zbudowac lotnisko za koszt K, niezalezny od miasta. Na poczatku w zadnym miescie nie
# ma lotniska, podobnie miedzy zadnymi dwoma miastami nie ma wybudowanej drogi.
# Naszym celem jest zbudowac lotniska i drogi za minimalny laczny koszt, tak, aby kazde miasto
# mialo dostep do lotniska.

# Miasto ma dostep do lotniska, jesli:
# 1) Jest w nim lotnisko lub
# 2) Mozna z niego dojechac do innego miasta, w ktorym jest lotnisko]

# Jesli istnieje wiecej nz jedno rozwiazanie o minimalnym koszcie, nalezy wybrac to
# z najwieksza iloscia lotnisk.

# szukamy MST dopoki koszty sa mniejsze niz K, potem budujemy lotniska na wyspach

class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self
        self.airplane = False

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):

    x = find(x)
    y = find(y)

    if x == y:
        return

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

# Minimalne Drzewo Rozpinajace (Minimal Spanning Tree) MST O(ElogE)

def airplanes(G, K):

    E = []
    n = len(G)
    max_ = 0

    for i in range(n):
        max_ = max(max_, G[i][0], G[i][1])

    vertices = [Node(i) for i in range(max_+1)]
    G = sorted(G, key=lambda x: x[2])
    cost = 0

    for e in G:
        u, v, w = e[0], e[1], e[2]
        if find(vertices[u]) != find(vertices[v]) and w < K:
            E.append(e)
            union(vertices[u], vertices[v])
            cost += w

            if not find(vertices[u]).airplane:
                find(vertices[u]).airplane = True
                cost += K

        else: break

    Islands = []

    for i in range(max_+1):
        if not find(vertices[i]).airplane:
            find(vertices[i]).airplane = True
            cost += K
            Islands.append(i)

    print("minimum cost:", cost)
    print("connect these edges:", E)
    print("islands left, build additional airfields at vertices:", Islands)
    return cost

G = [(0,1,8), (1,2,1), (1,3,6), (3,5,2), (3,4,10), (6,7,3)]

# airplanes(G, 5)