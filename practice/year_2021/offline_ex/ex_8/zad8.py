from zad8testy import runtests
from math import ceil

# lecture pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta siecią autostrad, tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na
# którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii
# prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len =
# √((x1 − x2)^2 + (y1 − y2)^2).
# Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
# Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie
# i jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady.
# Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej
# w km).
# Proszę zaimplementować funkcję highway(A), która dla danych położeń miast wyznacza minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady.
# Przykład Dla tablicy A =[(10,10),(15,25),(20,20),(30,40)] wynikiem jest 7 (Autostrady
# pomiędzy miastami 0-1, 0-2, 1-3).

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):

    x = find(x)
    y = find(y)

    if x == y:
        return

    if x.rank < y.rank:
        x.parent = y

    else:
        y.parent = x
        if x.rank == y.rank:
            x.rank += 1

def kruskal(V, E, i_edge, curr_best):

    vert = [Node(i) for i in V]
    union(vert[E[i_edge][0]], vert[E[i_edge][1]])
    min_diff = 0
    left = i_edge - 1
    right = i_edge + 1
    flag_left = True
    flag_right = True
    curr_min_edge = curr_max_edge = E[i_edge][2]
    edge_counter = 1

    while True:

        if min_diff > curr_best:
            return float("inf")

        while flag_left != False:
            if left < 0:
                flag_left = False
                break
            else:
                while find(vert[E[left][0]]) == find(vert[E[left][1]]):
                    left -= 1
                    if left < 0:
                        flag_left = False
                        break
                else:
                    break

        while flag_right != False:
            if right >= len(E):
                flag_right = False
                break
            else:
                while find(vert[E[right][0]]) == find(vert[E[right][1]]):
                    right += 1
                    if right >= len(E):
                        flag_right = False
                        break
                else:
                    break


        if flag_left == True and flag_right == False:
            union(vert[E[left][0]], vert[E[left][1]])
            curr_min_edge = E[left][2]
            min_diff = max(min_diff, curr_max_edge - curr_min_edge)
            left -= 1
            edge_counter += 1

        elif flag_left == False and flag_right == True:
            union(vert[E[right][0]], vert[E[right][1]])
            curr_max_edge = E[right][2]
            min_diff = max(min_diff, curr_max_edge - curr_min_edge)
            right += 1
            edge_counter += 1

        elif flag_left == True and flag_right == True:

            if abs(E[right][2] - E[i_edge][2]) < abs(E[left][2] - E[left][2]):
                union(vert[E[right][0]], vert[E[right][1]])
                curr_max_edge = E[right][2]
                min_diff = max(min_diff, curr_max_edge - curr_min_edge)
                right += 1
                edge_counter += 1

            else:
                union(vert[E[left][0]], vert[E[left][1]])
                curr_min_edge = E[left][2]
                min_diff = max(min_diff, curr_max_edge - curr_min_edge)
                left -= 1
                edge_counter += 1

        elif edge_counter == len(V) - 1:
            return min_diff

        else:
            return min_diff

def distance(A, B):
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** .5


def edges_list(A):
    E = []
    n = len(A)
    for i in range(n - 1):
        for j in range(i + 1, n):
            E.append((i, j, ceil(distance(A[i], A[j]))))

    return E

def highway(A):

    n = len(A)
    V = list(range(n))
    E = edges_list(A)
    E.sort(key=lambda e: e[2])
    curr_best = float("inf")

    for i_edge in range(len(E)):
        curr_best = min(kruskal(V, E, i_edge, curr_best), curr_best)

    return curr_best

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )



