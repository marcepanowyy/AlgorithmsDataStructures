# (Skojarzenie w drzewie)

# Prosze podac algorytm, ktory majac na wejsciu drzewo oblicza skojarzenie o
# maksymalnej licznosci Czy algorytm dalej bedzie dzialac, jesli kazda krawedz
# bedzie miec dodatnia wage i szukamy skojarzenia o maksymalnej sumie wag?

# mozna skorzystac z algorytmu na szukanie skojarzenia o maks. licznosci w
# grafie dwudzielnym (drzewo z def. jest grafem dwudzielnym):
# tworzymy sztuczne zrodlo i ujscie, odpowiednio laczymy wierzcholki
# (oczywiscie krawedzie to wagi, ktore oznaczaja pojemnosc), odpalamy algorytm
# znajdujacy maksymalny przeplyw.

# jednak istnieje szybszy sposob podobny do problemu
# maximum sum of non-adjacent nodes

# nie moje rozw

def max_association(T, root_idx): # najliczniejsze skojarzenie

    n = len(T)
    G = [-1] * n
    F = [-1] * n

    def f(x):
        # Maximum number of disjoint edges in the x node's subtree
        if F[x] < 0:
            F[x] = max(g(x), 0)
            diff = 0
            for y in T[x]:
                diff = max(diff, -f(y) + g(y) + 1)
            F[x] += diff
        return F[x]

    def g(x):
        # Maximum number of disjoint edges in the x node's subtree
        # when we don't take any of edges which x is connected with
        if G[x] < 0:
            G[x] = 0
            for y in T[x]:
                G[x] += f(y)
        return G[x]

    return f(root_idx)


def max_weight_association(T, root_idx): # skojarzenie o najwiekszej sumie wag

    n = len(T)
    G = [-1] * n
    F = [-1] * n

    def f(x):
        # Maximum number of disjoint edges in the x node's subtree
        if F[x] < 0:
            F[x] = max(g(x), 0)
            diff = 0
            for y, weight in T[x]:
                diff = max(diff, -f(y) + g(y) + weight)
            F[x] += diff
        return F[x]

    def g(x):
        # Maximum number of disjoint edges in the x node's subtree
        # when we don't take any of edges which x is connected with
        if G[x] < 0:
            G[x] = 0
            for y, _ in T[x]:
                G[x] += f(y)
        return G[x]

    return f(root_idx)

